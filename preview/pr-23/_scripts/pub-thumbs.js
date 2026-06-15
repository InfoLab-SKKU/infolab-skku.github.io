/**
 * pub-thumbs.js
 * Generates visually distinct SVG thumbnails for publications without cover images.
 * Displays a keyword word cloud extracted from the publication title.
 */
(function () {
  // Color palettes keyed to research domains
  const palettes = [
    { from: '#07377b', to: '#1060c8', accent: '#7ab8ff' },  // navy   – security / cyber
    { from: '#0a4a2e', to: '#1a8a50', accent: '#5ddc95' },  // green  – biomedical / health
    { from: '#3a0a6b', to: '#7c3aed', accent: '#c4a0ff' },  // purple – AI / ML
    { from: '#7b3207', to: '#cc6010', accent: '#ffb566' },  // amber  – misc
    { from: '#0a5060', to: '#0d9ecc', accent: '#6ed5f5' },  // teal   – misc
    { from: '#6b0a40', to: '#c0156e', accent: '#ff75b8' },  // magenta– misc
    { from: '#2a4a00', to: '#5a8a00', accent: '#a2e040' },  // lime   – misc
    { from: '#4a1a00', to: '#9a4010', accent: '#ffaa60' },  // rust   – misc
  ];

  // Stop words to strip before keyword extraction
  const STOP = new Set([
    'a','an','the','and','or','but','in','on','at','to','for','of','with','by','from',
    'is','are','was','were','be','been','being','have','has','had','do','does','did',
    'will','would','shall','should','may','might','must','can','could',
    'its','it','this','that','these','those',
    'using','used','based','via','through','across','into','over','under','between',
    'against','about','novel','new','approach','method','framework','system',
    'study','analysis','towards','toward','efficient','effective','comprehensive',
    'large','scale','real','world','robust','advanced','improved','improving',
    'enhanced','multi','cross','end','self','high','low','our','their','we','us',
    'two','one','three','four','five','six','seven','eight','nine','ten',
    'paper','work','survey','review','case','type','way',
  ]);

  // Domain-specific importance boosts (lower-cased stems)
  const BOOST = {
    // Cybersecurity
    malware: 4, ransomware: 4, phishing: 4, botnet: 4, rootkit: 4,
    security: 3, cyber: 3, attack: 3, detection: 3, intrusion: 3,
    privacy: 3, adversarial: 3, vulnerability: 3, exploit: 3, ids: 3,
    defense: 2, firewall: 3, encryption: 3, authentication: 3,
    deepfake: 4, spoofing: 3, evasion: 3, obfuscation: 3,
    // Graph / GNN / AI
    gnn: 4, xai: 4, llm: 4, gpt: 4, bert: 3, lstm: 3,
    graph: 3, neural: 3, transformer: 3, attention: 3, federated: 4,
    explainable: 3, generative: 3, convolutional: 3, diffusion: 3,
    learning: 2, deep: 2, classification: 2, reinforcement: 3,
    // Biomedical
    alzheimer: 4, cancer: 4, tumor: 3, alzheimers: 4,
    disease: 3, clinical: 3, brain: 3, diagnosis: 3, medical: 3,
    mri: 3, genomics: 3, imaging: 2, pathology: 3, radiology: 3,
    patient: 2, drug: 2, therapy: 2,
    // Tech & systems
    iot: 3, blockchain: 3, drone: 3, autonomous: 3,
    cloud: 2, network: 2, networks: 2, prediction: 2,
    optimization: 2, recommendation: 2, surveillance: 2,
    // Generic CS
    algorithm: 2, knowledge: 1, social: 1, data: 1, model: 1,
  };

  function hashStr(str) {
    let h = 5381;
    for (let i = 0; i < str.length; i++) {
      h = (Math.imul(h, 33) + str.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  function escXml(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  // Pull the most meaningful terms from a paper title
  function extractKeywords(title) {
    if (!title) return [];
    const words = title.replace(/[^a-zA-Z0-9\-]/g, ' ').split(/\s+/).filter(w => w.length >= 3);
    const seen = new Set();
    return words
      .filter(w => !STOP.has(w.toLowerCase()))
      .map(w => {
        const lower = w.toLowerCase();
        // Lightweight suffix stripping for boost lookup
        const stem = lower.replace(/(?:tion|ing|ment|ness|ity|ive|ous|ful|ers?|ed)$/, '');
        const boost = BOOST[lower] || BOOST[stem] || 0;
        // Score = domain boost + mild length preference (longer = more specific)
        return { word: w, score: boost + Math.min(w.length / 4, 2) };
      })
      .sort((a, b) => b.score - a.score)
      .filter(item => {
        const key = item.word.toLowerCase();
        if (seen.has(key)) return false;
        seen.add(key);
        return true;
      })
      .slice(0, 9)
      .map(item => item.word);
  }

  // Estimate rendered text width for mixed-case proportional fonts
  function approxWidth(word, size) {
    let w = 0;
    for (const ch of word) {
      w += /[A-Z]/.test(ch) ? size * 0.70 : size * 0.54;
    }
    return w;
  }

  // Pack keywords into rows and return SVG <text> elements
  function layoutWordCloud(keywords) {
    if (!keywords.length) {
      return '<text x="90" y="48" font-family="sans-serif" font-size="11" fill="rgba(255,255,255,0.6)" text-anchor="middle">—</text>';
    }

    // Font size by rank
    const sizeOf = i => (i === 0 ? 20 : i <= 2 ? 14 : i <= 5 ? 11 : 9);

    const W = 180, CLOUD_H = 90, PAD = 8, ROW_GAP = 5, WORD_GAP = 7;
    const available = W - PAD * 2;

    const items = keywords.map((word, i) => {
      const size = sizeOf(i);
      return { word, size, ew: approxWidth(word, size) };
    });

    // Greedy row packing (never split a single word onto overflow)
    const rows = [];
    let row = [], rowW = 0;
    for (const item of items) {
      const needed = rowW === 0 ? item.ew : rowW + WORD_GAP + item.ew;
      if (needed <= available || row.length === 0) {
        row.push(item);
        rowW = needed;
      } else {
        rows.push({ items: row, totalW: rowW });
        row = [item];
        rowW = item.ew;
      }
    }
    if (row.length) rows.push({ items: row, totalW: rowW });

    // Total cloud height
    const rowH = rows.map(r => Math.max(...r.items.map(i => i.size)));
    const totalH = rowH.reduce((s, h) => s + h, 0) + ROW_GAP * (rows.length - 1);

    // Vertical centering: baseline of first row
    let curY = rowH[0] + Math.max(4, (CLOUD_H - totalH) / 2);

    const parts = [];
    for (let ri = 0; ri < rows.length; ri++) {
      const { items: rowItems, totalW } = rows[ri];
      let cx = PAD + (available - totalW) / 2; // left edge of centered row

      for (const item of rowItems) {
        const midX = cx + item.ew / 2;
        const fill = item.size >= 18 ? 'white'
                   : item.size >= 12 ? 'rgba(255,255,255,0.92)'
                   : 'rgba(255,255,255,0.76)';
        const fw = item.size >= 18 ? 700 : item.size >= 12 ? 600 : 500;
        parts.push(
          `<text x="${midX.toFixed(1)}" y="${curY.toFixed(1)}"` +
          ` font-family="'Segoe UI',system-ui,Arial,sans-serif"` +
          ` font-size="${item.size}" font-weight="${fw}"` +
          ` fill="${fill}" text-anchor="middle">${escXml(item.word)}</text>`
        );
        cx += item.ew + WORD_GAP;
      }
      curY += rowH[ri] + ROW_GAP;
    }
    return parts.join('');
  }

  // XOR-shift seeded points for decorative background
  function seededPoints(seed, count, maxX, maxY) {
    const points = [];
    let s = hashStr(seed) || 1;
    for (let i = 0; i < count; i++) {
      s ^= s << 13; s ^= s >> 17; s ^= s << 5;
      const x = Math.abs(s) % maxX;
      s ^= s << 13; s ^= s >> 17; s ^= s << 5;
      const y = Math.abs(s) % maxY;
      s ^= s << 13; s ^= s >> 17; s ^= s << 5;
      const r = 1.2 + (Math.abs(s) % 3);
      points.push({ x, y, r });
    }
    return points;
  }

  function makeSVG(title, publisher, year, tags) {
    // Palette selection: semantic topics override hash
    let palIdx = hashStr((title || '') + (publisher || '')) % palettes.length;
    const combined = ((tags || '') + ' ' + (title || '')).toLowerCase();
    if (/malware|ransomware|phishing|cyber|security|attack|intrusion|ids|exploit|botnet|deepfake/.test(combined)) {
      palIdx = 0; // navy – security
    } else if (/alzheimer|cancer|tumor|clinical|medical|disease|brain|mri|genomic|radiology|pathology/.test(combined)) {
      palIdx = 1; // green – biomedical
    } else if (/neural|graph|gnn|transformer|explainable|federated|deep learning|llm|gpt|bert/.test(combined)) {
      palIdx = 2; // purple – AI/ML
    }
    const pal = palettes[palIdx];

    const keywords = extractKeywords(title);

    // Decorative dots + connecting lines
    const pts = seededPoints(title || publisher || '', 14, 180, 90);
    const dots = pts.map(p =>
      `<circle cx="${p.x}" cy="${p.y}" r="${p.r.toFixed(1)}" fill="rgba(255,255,255,0.14)"/>`
    ).join('');
    const lines = [];
    for (let i = 0; i < pts.length - 1; i++) {
      const dx = pts[i].x - pts[i + 1].x, dy = pts[i].y - pts[i + 1].y;
      if (Math.sqrt(dx * dx + dy * dy) < 50) {
        lines.push(
          `<line x1="${pts[i].x}" y1="${pts[i].y}" x2="${pts[i+1].x}" y2="${pts[i+1].y}"` +
          ` stroke="rgba(255,255,255,0.07)" stroke-width="1"/>`
        );
      }
    }

    const cloud = layoutWordCloud(keywords);
    const pubDisplay = escXml((publisher || '').slice(0, 36));
    const ariaLabel = escXml((keywords[0] || publisher || '') + ' ' + year);

    return [
      `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" role="img" aria-label="${ariaLabel}">`,
      '<defs>',
      `<linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">`,
      `<stop offset="0%" stop-color="${pal.from}"/>`,
      `<stop offset="100%" stop-color="${pal.to}"/>`,
      '</linearGradient>',
      '</defs>',
      '<rect width="180" height="140" fill="url(#g)"/>',
      lines.join(''),
      dots,
      // Dark strip at bottom
      '<rect x="0" y="95" width="180" height="45" fill="rgba(0,0,0,0.40)"/>',
      // Keyword word cloud (main visual)
      cloud,
      // Publisher name (inside strip)
      `<text x="90" y="110" font-family="'Segoe UI',system-ui,Arial,sans-serif"` +
      ` font-size="9" fill="rgba(255,255,255,0.78)" text-anchor="middle">${pubDisplay}</text>`,
      // Year in accent color
      `<text x="90" y="128" font-family="'Segoe UI',system-ui,Arial,sans-serif"` +
      ` font-size="13" font-weight="600" fill="${pal.accent}" text-anchor="middle">${escXml(year)}</text>`,
      '</svg>',
    ].join('\n');
  }

  function init() {
    document.querySelectorAll('.citation-thumb-gen').forEach(function (el) {
      const title = el.dataset.title || '';
      const pub   = el.dataset.pub   || '';
      const year  = el.dataset.year  || '';
      const tags  = el.dataset.tags  || '';

      const svg = makeSVG(title, pub, year, tags);
      const uri = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);

      const img = document.createElement('img');
      img.src       = uri;
      img.alt       = (pub || title) + (year ? ' · ' + year : '');
      img.loading   = 'lazy';
      img.className = 'citation-thumb-img';
      el.appendChild(img);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
