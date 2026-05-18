#!/usr/bin/env node
/*
  compress-images.js — bulk-optimize images under /images.

  Setup (one-time):
    npm init -y
    npm install sharp

  Usage:
    node tools/compress-images.js              # dry run, prints what would change
    node tools/compress-images.js --apply      # write WebP siblings + downscale large JPEGs

  What it does:
  - Generates a .webp sibling for every .jpg/.jpeg/.png > 200 KB
  - Caps very large photos at 1920 px on the longest edge (preserves aspect ratio)
  - Skips files where a fresher .webp already exists
  - Leaves originals in place so existing references keep working

  After running, you can opt into WebP-with-fallback in your markup like:
    <picture>
      <source srcset="/images/foo.webp" type="image/webp">
      <img src="/images/foo.jpg" alt="…" loading="lazy">
    </picture>
*/

const fs = require("fs");
const path = require("path");

let sharp;
try {
  sharp = require("sharp");
} catch (e) {
  console.error("sharp is not installed. Run: npm install sharp");
  process.exit(1);
}

const ROOT = path.join(__dirname, "..", "images");
const APPLY = process.argv.includes("--apply");
const MIN_SIZE_BYTES = 200 * 1024;   // 200 KB
const MAX_EDGE_PX = 1920;
const WEBP_QUALITY = 78;
const JPEG_QUALITY = 82;

const EXTS = new Set([".jpg", ".jpeg", ".png"]);

function* walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) yield* walk(full);
    else yield full;
  }
}

async function processFile(file) {
  const ext = path.extname(file).toLowerCase();
  if (!EXTS.has(ext)) return null;

  const stat = fs.statSync(file);
  if (stat.size < MIN_SIZE_BYTES) return null;

  const webpPath = file.replace(/\.(jpe?g|png)$/i, ".webp");
  const webpExists = fs.existsSync(webpPath);
  const webpFresh = webpExists && fs.statSync(webpPath).mtimeMs >= stat.mtimeMs;

  const meta = await sharp(file).metadata();
  const needsResize = Math.max(meta.width || 0, meta.height || 0) > MAX_EDGE_PX;

  const actions = [];
  if (!webpFresh) actions.push("webp");
  if (needsResize) actions.push("resize");

  if (actions.length === 0) return null;

  const result = {
    file: path.relative(path.join(__dirname, ".."), file),
    sizeKB: Math.round(stat.size / 1024),
    actions,
  };

  if (!APPLY) return result;

  const pipeline = sharp(file).rotate();
  if (needsResize) {
    pipeline.resize({
      width: MAX_EDGE_PX,
      height: MAX_EDGE_PX,
      fit: "inside",
      withoutEnlargement: true,
    });
  }
  if (!webpFresh) {
    await pipeline.clone().webp({ quality: WEBP_QUALITY }).toFile(webpPath);
  }
  if (needsResize) {
    const tmp = file + ".tmp";
    if (ext === ".png") {
      await pipeline.png({ compressionLevel: 9 }).toFile(tmp);
    } else {
      await pipeline.jpeg({ quality: JPEG_QUALITY, mozjpeg: true }).toFile(tmp);
    }
    fs.renameSync(tmp, file);
  }
  return result;
}

(async () => {
  if (!fs.existsSync(ROOT)) {
    console.error("images directory not found:", ROOT);
    process.exit(1);
  }
  const results = [];
  for (const file of walk(ROOT)) {
    try {
      const r = await processFile(file);
      if (r) results.push(r);
    } catch (e) {
      console.error("failed:", file, e.message);
    }
  }
  if (results.length === 0) {
    console.log("Nothing to do.");
    return;
  }
  console.log((APPLY ? "Processed" : "Would process") + " " + results.length + " file(s):");
  for (const r of results) {
    console.log("  " + r.actions.join("+") + " " + r.file + " (" + r.sizeKB + " KB)");
  }
  if (!APPLY) console.log("\nRe-run with --apply to write changes.");
})();
