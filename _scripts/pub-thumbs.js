/**
 * pub-thumbs.js
 * Generates visually distinct SVG thumbnails for publications without cover images.
 * Each paper gets a unique color and shows venue abbreviation + year.
 */
(function () {
  // Color palettes — each tied to a visual theme
  const palettes = [
    { from: '#07377b', to: '#1060c8', accent: '#7ab8ff' },  // navy blue
    { from: '#0a4a2e', to: '#1a8a50', accent: '#5ddc95' },  // green
    { from: '#3a0a6b', to: '#7c3aed', accent: '#c4a0ff' },  // purple
    { from: '#7b3207', to: '#cc6010', accent: '#ffb566' },  // amber
    { from: '#0a5060', to: '#0d9ecc', accent: '#6ed5f5' },  // teal
    { from: '#6b0a40', to: '#c0156e', accent: '#ff75b8' },  // magenta
    { from: '#2a4a00', to: '#5a8a00', accent: '#a2e040' },  // lime
    { from: '#4a1a00', to: '#9a4010', accent: '#ffaa60' },  // rust
  ];

  // Known venue/journal abbreviations
  const venueMap = [
    ['ieee transactions', 'IEEE Trans'],
    ['ieee access', 'IEEE Acc'],
    ['ieee ', 'IEEE'],
    ['acm ccs', 'CCS'],
    ['acm ', 'ACM'],
    ['usenix security', 'USENIX Sec'],
    ['usenix', 'USENIX'],
    ['ndss', 'NDSS'],
    ['sp symposium', 'IEEE S&P'],
    ['network and distributed system', 'NDSS'],
    ['springer', 'Springer'],
    ['elsevier', 'Elsevier'],
    ['nature ', 'Nature'],
    ['science ', 'Science'],
    ['oxford', 'OUP'],
    ['wiley', 'Wiley'],
    ['mdpi', 'MDPI'],
    ['plos', 'PLOS'],
    ['frontiers', 'Frontiers'],
    ['arxiv', 'arXiv'],
    ['neurips', 'NeurIPS'],
    ['neural information', 'NeurIPS'],
    ['icml', 'ICML'],
    ['iclr', 'ICLR'],
    ['cvpr', 'CVPR'],
    ['aaai', 'AAAI'],
    ['computers', 'Comp.'],
    ['sensors', 'Sensors'],
    ['pubmed', 'PubMed'],
    ['applied sciences', 'App. Sci'],
    ['journal of', 'J.'],
    ['international journal', 'Int. J.'],
    ['information sciences', 'Inf. Sci'],
    ['expert systems', 'Expert Sys'],
    ['knowledge', 'KBS'],
    ['pattern recognition', 'Pat. Rec'],
    ['neural networks', 'Neural Net'],
    ['artificial intelligence', 'AI J.'],
    ['machine learning', 'ML J.'],
    ['security', 'Sec.'],
    ['cyber', 'Cyber'],
    ['biomedical', 'Biomed.'],
    ['medical', 'Med.'],
    ['health', 'Health'],
    ['cancer', 'Cancer'],
    ['brain', 'Brain'],
    ['neuro', 'Neuro'],
    ['clinical', 'Clin.'],
    ['computing', 'Comput.'],
    ['communications', 'Commun.'],
    ['systems', 'Syst.'],
    ['networks', 'Netw.'],
    ['data mining', 'DMKD'],
    ['big data', 'Big Data'],
    ['cloud', 'Cloud'],
    ['iot', 'IoT'],
  ];

  function hashStr(str) {
    let h = 5381;
    for (let i = 0; i < str.length; i++) {
      h = (Math.imul(h, 33) + str.charCodeAt(i)) | 0;
    }
    return Math.abs(h);
  }

  function extractAbbr(publisher) {
    if (!publisher || !publisher.trim()) return 'Publ.';
    const lower = publisher.toLowerCase();
    for (const [key, abbr] of venueMap) {
      if (lower.includes(key)) return abbr;
    }
    // Generate from capital letters of significant words
    const stopWords = new Set(['the', 'of', 'and', 'in', 'on', 'a', 'an', 'for', 'to', 'by']);
    const words = publisher.split(/[\s,;\/\-]+/)
      .filter(w => w.length > 1 && !stopWords.has(w.toLowerCase()));
    if (words.length >= 2) {
      return words.slice(0, 4).map(w => w[0].toUpperCase()).join('');
    }
    return publisher.trim().slice(0, 7);
  }

  // XOR-shift based pseudo-random points seeded by string
  function seededPoints(seed, count, maxX, maxY) {
    const points = [];
    let state = hashStr(seed) || 1;
    for (let i = 0; i < count; i++) {
      state ^= state << 13;
      state ^= state >> 17;
      state ^= state << 5;
      const x = Math.abs(state) % maxX;
      state ^= state << 13; state ^= state >> 17; state ^= state << 5;
      const y = Math.abs(state) % maxY;
      state ^= state << 13; state ^= state >> 17; state ^= state << 5;
      const r = 1.2 + (Math.abs(state) % 3);
      points.push({ x, y, r });
    }
    return points;
  }

  function makeSVG(title, publisher, year, tags) {
    const h = hashStr((title || '') + (publisher || ''));

    // Pick palette — use tags for hints if available
    let palIdx = h % palettes.length;
    if (tags) {
      const t = tags.toLowerCase();
      if (t.includes('security') || t.includes('privacy') || t.includes('cyber')) palIdx = 0;
      else if (t.includes('health') || t.includes('bio') || t.includes('medical')) palIdx = 1;
      else if (t.includes('ai') || t.includes('machine') || t.includes('learning')) palIdx = 2;
    }
    const pal = palettes[palIdx];
    const abbr = extractAbbr(publisher);

    // Generate stable decorative dots + connecting lines
    const pts = seededPoints(title || publisher || '', 16, 180, 100);
    const dotsSVG = pts.map(p =>
      `<circle cx="${p.x}" cy="${p.y}" r="${p.r.toFixed(1)}" fill="rgba(255,255,255,0.20)"/>`
    ).join('');

    // Connect nearby points
    const linesSVG = [];
    for (let i = 0; i < pts.length - 1; i++) {
      const dx = pts[i].x - pts[i + 1].x;
      const dy = pts[i].y - pts[i + 1].y;
      if (Math.sqrt(dx * dx + dy * dy) < 55) {
        linesSVG.push(
          `<line x1="${pts[i].x}" y1="${pts[i].y}" x2="${pts[i+1].x}" y2="${pts[i+1].y}" stroke="rgba(255,255,255,0.10)" stroke-width="1.2"/>`
        );
      }
    }

    // Truncate publisher for display (avoid XML issues — already xml_escaped by Liquid)
    const pubDisplay = publisher ? publisher.slice(0, 36) : '';

    // Abbreviation font size — smaller if long
    const abbrSize = abbr.length <= 4 ? 26 : abbr.length <= 7 ? 20 : 15;

    return [
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 140" role="img" aria-label="' + (abbr) + ' ' + year + '">',
      '<defs>',
      `<linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">`,
      `<stop offset="0%" stop-color="${pal.from}"/>`,
      `<stop offset="100%" stop-color="${pal.to}"/>`,
      '</linearGradient>',
      '</defs>',
      '<rect width="180" height="140" fill="url(#g)"/>',
      linesSVG.join(''),
      dotsSVG,
      // Lower panel
      '<rect x="0" y="95" width="180" height="45" fill="rgba(0,0,0,0.38)"/>',
      // Venue abbreviation (main visual element)
      `<text x="90" y="73" font-family="'Segoe UI',system-ui,Arial,sans-serif"`,
      `  font-size="${abbrSize}" font-weight="700" fill="white"`,
      `  text-anchor="middle" letter-spacing="1">${abbr}</text>`,
      // Publisher name (small, inside dark strip)
      `<text x="90" y="110" font-family="'Segoe UI',system-ui,Arial,sans-serif"`,
      `  font-size="9" fill="rgba(255,255,255,0.80)" text-anchor="middle">${pubDisplay}</text>`,
      // Year (colored accent)
      `<text x="90" y="128" font-family="'Segoe UI',system-ui,Arial,sans-serif"`,
      `  font-size="13" font-weight="600" fill="${pal.accent}" text-anchor="middle">${year}</text>`,
      '</svg>',
    ].join('');
  }

  function init() {
    document.querySelectorAll('.citation-thumb-gen').forEach(function (el) {
      const title  = el.dataset.title || '';
      const pub    = el.dataset.pub   || '';
      const year   = el.dataset.year  || '';
      const tags   = el.dataset.tags  || '';

      const svg    = makeSVG(title, pub, year, tags);
      const uri    = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);

      const img    = document.createElement('img');
      img.src      = uri;
      img.alt      = pub + (year ? ' · ' + year : '');
      img.loading  = 'lazy';
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
