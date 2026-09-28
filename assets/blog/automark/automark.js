/* AutoMark blog post: component explorer and radar plots. Requires data.js. */
(function () {
  'use strict';

  var DATA = window.AUTOMARK_DATA;
  var SVGNS = 'http://www.w3.org/2000/svg';

  // Radar axes follow the paper's radar: four attacks (TPR@1%FPR) and three quality deviations.
  // Index into the 8-value rows [clean, deletion, substitution, back-translation, paraphrase,
  // dPPL, dSB-2, dSB-3].
  var AXES = [
    { label: 'Deletion', index: 1, kind: 'tpr' },
    { label: 'Substitution', index: 2, kind: 'tpr' },
    { label: 'Back-trans.', index: 3, kind: 'tpr' },
    { label: 'Paraphrase', index: 4, kind: 'tpr' },
    { label: 'ΔPPL', index: 5, kind: 'dev' },
    { label: 'ΔSB-2', index: 6, kind: 'dev' },
    { label: 'ΔSB-3', index: 7, kind: 'dev' }
  ];
  var COLUMNS = ['Clean', 'Del.', 'Sub.', 'Trsl.', 'Para.', 'ΔPPL', 'ΔSB-2', 'ΔSB-3'];
  var AXIS_NAMES = ['Clean', 'Deletion', 'Substitution', 'Back-translation', 'Paraphrase',
    'ΔPPL', 'ΔSB-2', 'ΔSB-3'];
  // Quality axes use the smallest of these upper bounds that covers every plotted value.
  var NICE = [1, 2, 5, 10, 20, 40, 70, 100];

  // Validated categorical slots (all pairs, light surface); the first is the site blue.
  var SLOTS = [
    { color: '#0079AF', marker: 'circle' },
    { color: '#eb6834', marker: 'square' },
    { color: '#1baf7a', marker: 'triangle' },
    { color: '#4a3aa7', marker: 'diamond' }
  ];
  var REFERENCE = { color: '#8c8c8c', marker: 'none', dash: '5 4' };

  // ---- Helpers ---------------------------------------------------------------------------------

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    setAttrs(node, attrs);
    append(node, children);
    return node;
  }

  function svg(tag, attrs, children) {
    var node = document.createElementNS(SVGNS, tag);
    setAttrs(node, attrs);
    append(node, children);
    return node;
  }

  function setAttrs(node, attrs) {
    if (!attrs) return;
    Object.keys(attrs).forEach(function (key) {
      var value = attrs[key];
      if (value === null || value === undefined || value === false) return;
      if (key === 'html') node.innerHTML = value;
      else if (key === 'text') node.textContent = value;
      else if (key.slice(0, 2) === 'on') node.addEventListener(key.slice(2), value);
      else node.setAttribute(key, value === true ? '' : value);
    });
  }

  function append(node, children) {
    if (!children) return;
    (Array.isArray(children) ? children : [children]).forEach(function (child) {
      if (child === null || child === undefined || child === false) return;
      node.appendChild(typeof child === 'string' ? document.createTextNode(child) : child);
    });
  }

  // Integers for TPRs; one decimal for quality deviations below 10 (the paper's convention). Only
  // used for the held-out values, which are already rounded; ablation cells ship the paper's strings.
  function fmt(value, index) {
    if (value === null || value === undefined) return '\u2013';
    if (index >= 5 && value < 10) return value.toFixed(1);
    return String(Math.round(value));
  }

  function plainText(html) {
    var div = document.createElement('div');
    div.innerHTML = html;
    return div.textContent.replace(/ /g, ' ');
  }

  function markerPath(shape, x, y) {
    var s;
    if (shape === 'square') { s = 3.8; return 'M' + (x - s) + ' ' + (y - s) + 'h' + 2 * s + 'v' + 2 * s + 'h' + -2 * s + 'z'; }
    if (shape === 'triangle') { s = 5; return 'M' + x + ' ' + (y - s) + 'L' + (x + s * 0.92) + ' ' + (y + s * 0.62) + 'L' + (x - s * 0.92) + ' ' + (y + s * 0.62) + 'z'; }
    if (shape === 'triangle-down') { s = 5; return 'M' + x + ' ' + (y + s) + 'L' + (x + s * 0.92) + ' ' + (y - s * 0.62) + 'L' + (x - s * 0.92) + ' ' + (y - s * 0.62) + 'z'; }
    if (shape === 'diamond') { s = 5.2; return 'M' + x + ' ' + (y - s) + 'L' + (x + s) + ' ' + y + 'L' + x + ' ' + (y + s) + 'L' + (x - s) + ' ' + y + 'z'; }
    s = 4.1; // circle
    return 'M' + (x - s) + ' ' + y + 'a' + s + ' ' + s + ' 0 1 0 ' + 2 * s + ' 0a' + s + ' ' + s + ' 0 1 0 ' + -2 * s + ' 0';
  }

  // Line sample with marker, used in legends and table toggles.
  function swatch(style, width) {
    width = width || 30;
    var node = svg('svg', { width: width, height: 14, viewBox: '0 0 ' + width + ' 14', 'aria-hidden': 'true' });
    node.appendChild(svg('line', {
      x1: 1, y1: 7, x2: width - 1, y2: 7, stroke: style.color, 'stroke-width': 2,
      'stroke-dasharray': style.dash || null
    }));
    if (style.marker && style.marker !== 'none') {
      node.appendChild(svg('path', {
        d: markerPath(style.marker, width / 2, 7), fill: '#fff', stroke: style.color, 'stroke-width': 1.6
      }));
    }
    return node;
  }

  function niceMax(value) {
    for (var i = 0; i < NICE.length; i++) if (value <= NICE[i] + 1e-9) return NICE[i];
    return Math.ceil(value / 10) * 10;
  }

  // ---- Radar -----------------------------------------------------------------------------------

  function Radar(host, label) {
    this.W = 480;
    this.H = 436;
    this.cx = 240;
    this.cy = 220;
    this.R = 140;
    this.groups = {};
    this.frame = null;
    this.flashTimer = null;
    // Each axis maps [center, rim] linearly onto the radius. `scales` is what is currently drawn
    // (interpolated during animations); update() sets `scalesTo`.
    this.scales = AXES.map(function (axis) { return axis.kind === 'tpr' ? { center: 0, rim: 100 } : { center: 10, rim: 0 }; });

    this.root = el('div', { class: 'am-radar' });
    this.svg = svg('svg', { viewBox: '0 0 ' + this.W + ' ' + this.H, role: 'img', 'aria-label': label });
    this.gridLayer = svg('g');
    this.seriesLayer = svg('g');
    this.svg.appendChild(this.gridLayer);
    this.svg.appendChild(this.seriesLayer);
    this.tip = el('div', { class: 'am-tip', role: 'presentation' });
    this.root.appendChild(this.svg);
    this.root.appendChild(this.tip);
    host.appendChild(this.root);
    this.drawGrid();
  }

  Radar.prototype.angle = function (i) {
    return -Math.PI / 2 + (2 * Math.PI * i) / AXES.length;
  };

  Radar.prototype.point = function (i, r) {
    var a = this.angle(i);
    return [this.cx + this.R * r * Math.cos(a), this.cy + this.R * r * Math.sin(a)];
  };

  Radar.prototype.drawGrid = function () {
    var self = this;
    [0.25, 0.5, 0.75, 1].forEach(function (r) {
      var pts = AXES.map(function (_, i) { return self.point(i, r).join(','); }).join(' ');
      self.gridLayer.appendChild(svg('polygon', { points: pts, class: 'am-grid-line' }));
    });
    this.rangeLabels = [];
    AXES.forEach(function (axis, i) {
      var end = self.point(i, 1);
      self.gridLayer.appendChild(svg('line', {
        x1: self.cx, y1: self.cy, x2: end[0], y2: end[1], class: 'am-grid-line'
      }));
      var a = self.angle(i);
      var cos = Math.cos(a);
      var sin = Math.sin(a);
      var anchor = cos > 0.2 ? 'start' : cos < -0.2 ? 'end' : 'middle';
      var p = self.point(i, 1.1);
      var dy = sin < -0.5 ? -24 : sin > 0.5 ? 8 : -8;
      var text = svg('text', { x: p[0], y: p[1] + dy, 'text-anchor': anchor, class: 'am-axis-label' }, axis.label);
      var range = svg('text', { x: p[0], y: p[1] + dy + 18, 'text-anchor': anchor, class: 'am-axis-range' });
      self.gridLayer.appendChild(text);
      self.gridLayer.appendChild(range);
      self.rangeLabels.push(range);
    });
    this.updateRanges();
  };

  Radar.prototype.updateRanges = function () {
    var self = this;
    AXES.forEach(function (axis, i) {
      var sc = self.scales[i];
      var text = Math.round(sc.center) + ' → ' + Math.round(sc.rim) + '%';
      if (self.rangeLabels[i].textContent !== text) self.rangeLabels[i].textContent = text;
    });
  };

  // Radius of each axis value under the currently drawn scales. Clamped so that a value outside an
  // intermediate range never flips through the center while the scales animate.
  Radar.prototype.radii = function (values) {
    var self = this;
    return values.map(function (v, i) {
      var sc = self.scales[i];
      return Math.max(0, Math.min(1.05, (v - sc.center) / (sc.rim - sc.center)));
    });
  };

  function axisValues(values) {
    return AXES.map(function (axis) { return values[axis.index]; });
  }

  // series: [{key, label, sub, color, dash, marker, values}]; later entries are drawn on top.
  Radar.prototype.update = function (series) {
    var self = this;
    // Every axis zooms on the plotted values. TPR axes span multiples of 10 with at least a 5-point
    // margin, so no marker sits on the center; quality axes run from a nice upper bound down to 0.
    this.scalesFrom = this.scales.map(function (sc) { return { center: sc.center, rim: sc.rim }; });
    this.scalesTo = AXES.map(function (axis) {
      var values = series.map(function (s) { return s.values[axis.index]; });
      var min = Math.min.apply(null, values);
      var max = Math.max.apply(null, values);
      if (axis.kind === 'tpr') {
        var center = Math.max(0, Math.floor((min - 5) / 10) * 10);
        var rim = Math.min(100, Math.ceil((max + 5) / 10) * 10);
        return { center: center, rim: Math.max(rim, center + 10) };
      }
      return { center: niceMax(max), rim: 0 };
    });
    this.flashRanges();

    var keep = {};
    series.forEach(function (s) {
      keep[s.key] = true;
      var g = self.groups[s.key];
      var target = axisValues(s.values);
      if (!g) {
        g = self.createGroup(s);
        g.vals = target.slice();
        g.node.style.opacity = '0';
        self.groups[s.key] = g;
        requestAnimationFrame(function () { g.node.style.opacity = ''; });
      }
      g.series = s;
      g.from = g.vals.slice();
      g.to = target;
      self.seriesLayer.appendChild(g.node); // re-append keeps the drawing order
    });
    Object.keys(this.groups).forEach(function (key) {
      if (!keep[key]) {
        self.seriesLayer.removeChild(self.groups[key].node);
        delete self.groups[key];
      }
    });
    this.hideTip();
    this.animate();
  };

  // Briefly color the range labels that change, so that the reader sees why the shapes move.
  Radar.prototype.flashRanges = function () {
    var self = this;
    AXES.forEach(function (axis, i) {
      var a = self.scalesFrom[i];
      var b = self.scalesTo[i];
      if (a.center !== b.center || a.rim !== b.rim) self.rangeLabels[i].classList.add('am-changed');
    });
    clearTimeout(this.flashTimer);
    this.flashTimer = setTimeout(function () {
      self.rangeLabels.forEach(function (label) { label.classList.remove('am-changed'); });
    }, 900);
  };

  Radar.prototype.createGroup = function (s) {
    var self = this;
    var node = svg('g', { class: 'am-series' });
    var poly = svg('polygon', {
      fill: s.color, 'fill-opacity': s.marker === 'none' ? 0 : 0.06, stroke: s.color,
      'stroke-width': s.marker === 'none' ? 1.6 : 2, 'stroke-linejoin': 'round',
      'stroke-dasharray': s.dash || null
    });
    node.appendChild(poly);
    var marks = [];
    var hits = [];
    AXES.forEach(function (axis, i) {
      if (s.marker !== 'none') {
        var m = svg('path', { fill: '#fff', stroke: s.color, 'stroke-width': 1.6 });
        node.appendChild(m);
        marks.push(m);
      }
      var hit = svg('circle', { r: 10, class: 'am-hit' });
      hit.addEventListener('mouseenter', function () { self.showTip(key(), i); });
      hit.addEventListener('mouseleave', function () { self.hideTip(); });
      node.appendChild(hit);
      hits.push(hit);
    });
    var group = { node: node, poly: poly, marks: marks, hits: hits, series: s };
    function key() { return group.series.key; }
    return group;
  };

  Radar.prototype.animate = function () {
    var self = this;
    if (this.frame) cancelAnimationFrame(this.frame);
    var start = null;
    var duration = 520;
    function lerp(a, b, e) { return a + (b - a) * e; }
    function step(ts) {
      if (start === null) start = ts;
      var t = Math.min(1, (ts - start) / duration);
      var e = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
      self.scales = self.scalesTo.map(function (to, i) {
        var from = self.scalesFrom[i];
        return { center: lerp(from.center, to.center, e), rim: lerp(from.rim, to.rim, e) };
      });
      self.updateRanges();
      Object.keys(self.groups).forEach(function (key) {
        var g = self.groups[key];
        g.vals = g.to.map(function (to, i) { return lerp(g.from[i], to, e); });
        self.place(g);
      });
      self.frame = t < 1 ? requestAnimationFrame(step) : null;
    }
    this.frame = requestAnimationFrame(step);
  };

  Radar.prototype.place = function (g) {
    var self = this;
    var pts = this.radii(g.vals).map(function (r, i) { return self.point(i, r); });
    g.poly.setAttribute('points', pts.map(function (p) { return p[0].toFixed(2) + ',' + p[1].toFixed(2); }).join(' '));
    pts.forEach(function (p, i) {
      if (g.marks[i]) g.marks[i].setAttribute('d', markerPath(g.series.marker, p[0], p[1]));
      g.hits[i].setAttribute('cx', p[0]);
      g.hits[i].setAttribute('cy', p[1]);
    });
  };

  Radar.prototype.highlight = function (key) {
    var self = this;
    Object.keys(this.groups).forEach(function (k) {
      self.groups[k].node.classList.toggle('am-faded', key !== null && k !== key);
    });
  };

  Radar.prototype.showTip = function (key, i) {
    var g = this.groups[key];
    if (!g) return;
    var s = g.series;
    var axis = AXES[i];
    this.tip.innerHTML = '';
    append(this.tip, [
      el('b', { html: s.label }), s.sub ? el('span', { class: 'am-legend-unit', text: ' · ' + s.sub }) : null,
      el('br'),
      AXIS_NAMES[axis.index] + (axis.kind === 'tpr' ? ' TPR: ' : ' deviation: '),
      el('span', { class: 'am-tip-val', text: (s.text ? s.text[axis.index] : fmt(s.values[axis.index], axis.index)) + '%' })
    ]);
    var box = this.root.getBoundingClientRect();
    var hit = g.hits[i].getBoundingClientRect();
    var x = hit.left + hit.width / 2 - box.left;
    var y = hit.top - box.top;
    this.tip.classList.add('am-on');
    var w = this.tip.offsetWidth;
    var left = Math.max(0, Math.min(box.width - w, x - w / 2));
    this.tip.style.left = left + 'px';
    this.tip.style.top = Math.max(0, y - this.tip.offsetHeight - 6) + 'px';
    this.highlight(key);
  };

  Radar.prototype.hideTip = function () {
    this.tip.classList.remove('am-on');
    this.highlight(null);
  };

  // ---- Component explorer ----------------------------------------------------------------------

  var FAMILY_NAMES = {
    shared: 'compatible with every family',
    fresh: 'fresh-race family',
    geometry: 'private-geometry family',
    skeleton: 'skeleton family'
  };
  var UNIT_NAMES = { token: 'Token', lexical: 'Lexical group' };

  var PRESETS = [
    { name: 'Context length', comp: 'fixed', configs: ['fixed-k0', 'fixed-k1', 'fixed-k3'] },
    { name: 'Adding true randomness', comp: 'copula', configs: ['copula-0.9', 'private-0.2', 'tail'] },
    { name: 'Fresh short contexts', comp: 'cascade', configs: ['fixed-k1', 'cascade', 'ladder-4-floor'] },
    { name: 'Residual clocks', comp: 'residualrace', configs: ['residualrace', 'signed-gumbel', 'sphere-residual'] },
    { name: 'Detectors', comp: 'position-evidence', configs: ['det-gaussian', 'det-excess', 'det-position-weighted'] },
    { name: 'Lexical group', comp: 'lexical', configs: ['core'], unit: 'lexical' }
  ];

  function Explorer(host) {
    var self = this;
    this.host = host;
    this.configs = {};
    this.comps = {};
    DATA.configs.forEach(function (c) { self.configs[c.id] = c; });
    DATA.components.forEach(function (c) { self.comps[c.id] = c; });
    this.state = { unit: 'token', comp: null, selected: [], preset: null };
    this.build();
    this.applyPreset(PRESETS[1]);
  }

  Explorer.prototype.build = function () {
    var self = this;
    this.unitButtons = {};
    var unit = el('div', { class: 'am-segmented', role: 'group', 'aria-label': 'Watermark unit' },
      ['token', 'lexical'].map(function (u) {
        var b = el('button', { type: 'button', text: UNIT_NAMES[u], onclick: function () { self.setUnit(u); } });
        self.unitButtons[u] = b;
        return b;
      }));
    this.presetButtons = PRESETS.map(function (p) {
      return el('button', { type: 'button', text: p.name, onclick: function () { self.applyPreset(p); } });
    });
    var toolbar = el('div', { class: 'am-toolbar' }, [
      el('div', { class: 'am-control' }, [el('span', { class: 'am-control-label', text: 'Unit' }), unit]),
      el('div', { class: 'am-control am-presets' },
        [el('span', { class: 'am-control-label', text: 'Examples' })].concat(this.presetButtons))
    ]);

    // Map of the components, one column per stage (Figure 2 of the paper).
    this.chips = {};
    var map = el('div', { class: 'am-map' }, DATA.stages.map(function (stage) {
      var chips = DATA.components.filter(function (c) { return c.stage === stage.id; }).map(function (c) {
        var dots = el('span', { class: 'am-chip-dots', 'aria-hidden': 'true' });
        var chip = el('button', {
          type: 'button', class: 'am-chip', 'data-family': c.family,
          title: plainText(c.name) + (c.prior ? ' (prior work)' : ''),
          onclick: function () { self.select(c.id, true); }
        }, [el('span', { class: 'am-chip-name' + (c.prior ? ' am-chip-prior' : ''), html: c.name + (c.prior ? '*' : '') }), dots]);
        self.chips[c.id] = { node: chip, dots: dots };
        return chip;
      });
      return el('div', { class: 'am-stage' }, [
        el('div', { class: 'am-stage-head', text: stage.name }),
        el('div', { class: 'am-chips' }, chips)
      ]);
    }));
    var key = el('div', { class: 'am-map-key' }, [
      el('span', {}, [el('i', { class: 'fresh' }), 'Fresh race']),
      el('span', {}, [el('i', { class: 'geometry' }), 'Private geometry']),
      el('span', {}, [el('i', { class: 'skeleton' }), 'Skeleton']),
      el('span', {}, [el('i'), 'Any family']),
      el('span', { text: '* Prior work' })
    ]);
    this.detail = el('div', { class: 'am-detail', 'aria-live': 'polite' });

    // Radar and its legend.
    var side = el('div', { class: 'am-side' });
    this.radar = new Radar(side, 'Radar plot of the selected configurations');
    this.legend = el('ul', { class: 'am-legend' });
    this.message = el('p', { class: 'am-message', role: 'status' });
    side.appendChild(this.legend);
    side.appendChild(this.message);
    side.appendChild(el('p', {
      class: 'am-side-note',
      html: 'Outward is better on every axis. Each axis rescales to cover the plotted values; ' +
        'the range under its label reads from center to rim.'
    }));

    // Map and detail on the left, radar on the right (sticky); the CSS puts the radar on top when narrow.
    append(this.host, [toolbar, el('div', { class: 'am-body' }, [el('div', {}, [map, key, this.detail]), side])]);
  };

  Explorer.prototype.setUnit = function (unit) {
    this.state.unit = unit;
    this.state.preset = null;
    this.render();
  };

  Explorer.prototype.select = function (compId, userAction) {
    this.state.comp = compId;
    if (userAction) this.state.preset = null;
    this.render();
  };

  Explorer.prototype.applyPreset = function (preset) {
    var self = this;
    this.state.unit = preset.unit || 'token';
    this.state.selected = preset.configs.map(function (id, i) {
      return { id: id, unit: self.state.unit, slot: i };
    });
    this.state.comp = preset.comp;
    this.state.preset = preset;
    this.message.textContent = '';
    this.render();
  };

  Explorer.prototype.findSelected = function (id, unit) {
    for (var i = 0; i < this.state.selected.length; i++) {
      var s = this.state.selected[i];
      if (s.id === id && s.unit === unit) return s;
    }
    return null;
  };

  Explorer.prototype.toggle = function (id, unit) {
    var existing = this.findSelected(id, unit);
    this.state.preset = null;
    this.message.textContent = '';
    if (existing) {
      this.state.selected.splice(this.state.selected.indexOf(existing), 1);
    } else {
      var used = this.state.selected.map(function (s) { return s.slot; });
      var slot = -1;
      for (var i = 0; i < SLOTS.length; i++) if (used.indexOf(i) < 0) { slot = i; break; }
      if (slot < 0) {
        this.message.textContent = 'Up to four configurations can be plotted at once. Remove one to add another.';
        return;
      }
      this.state.selected.push({ id: id, unit: unit, slot: slot });
    }
    this.render();
  };

  Explorer.prototype.render = function () {
    var self = this;
    var st = this.state;
    Object.keys(this.unitButtons).forEach(function (u) {
      self.unitButtons[u].setAttribute('aria-pressed', String(u === st.unit));
    });
    PRESETS.forEach(function (p, i) {
      self.presetButtons[i].setAttribute('aria-pressed', String(p === st.preset));
    });
    // Chips: current component and one dot per plotted configuration that uses it.
    Object.keys(this.chips).forEach(function (id) {
      var chip = self.chips[id];
      chip.node.setAttribute('aria-pressed', String(id === st.comp));
      chip.dots.innerHTML = '';
      st.selected.forEach(function (s) {
        // Same rule as the detail table: a configuration is listed under each of its components.
        if (self.configs[s.id].comps.indexOf(id) >= 0) chip.dots.appendChild(el('span', { style: 'background:' + SLOTS[s.slot].color }));
      });
    });
    this.renderDetail();
    this.renderSide();
  };

  Explorer.prototype.renderDetail = function () {
    var self = this;
    var st = this.state;
    var comp = this.comps[st.comp];
    var stage = DATA.stages.filter(function (s) { return s.id === comp.stage; })[0];
    var family = FAMILY_NAMES[comp.family];
    var rows = DATA.configs.filter(function (c) { return c.id !== 'core' && c.comps.indexOf(comp.id) >= 0; });
    var core = this.configs.core;
    var rescored = rows.some(function (c) { return c.rescored; });

    var head = el('thead', {}, [
      el('tr', {}, [
        el('th', { colspan: 2 }),
        el('th', { colspan: 5, class: 'am-group', text: 'TPR@1%FPR (%) ↑' }),
        el('th', { colspan: 3, class: 'am-group am-sep', text: 'Quality deviation (%) ↓' })
      ]),
      el('tr', {}, [el('th', { class: 'am-label', colspan: 2, text: 'Configuration' })].concat(
        COLUMNS.map(function (c, i) { return el('th', { class: i === 5 ? 'am-sep' : null, text: c }); })))
    ]);

    var body = el('tbody');
    [core].concat(rows).forEach(function (c) {
      var values = c[st.unit];
      var isReference = c.id === 'core' && st.unit === 'token';
      var cell;
      if (isReference) {
        cell = el('span', { title: 'Core scheme, always plotted as the dashed reference' }, swatch(REFERENCE, 26));
      } else {
        var sel = self.findSelected(c.id, st.unit);
        var style = sel ? SLOTS[sel.slot] : null;
        var name = plainText(c.label);
        var button = el('button', {
          type: 'button', class: 'am-plot', 'aria-pressed': String(!!sel),
          disabled: !values,
          title: !values ? 'Only evaluated with token units' : (sel ? 'Remove ' : 'Plot ') + name,
          'aria-label': (sel ? 'Remove ' : 'Plot ') + name,
          style: style ? 'color:' + style.color : null,
          onclick: function () { self.toggle(c.id, st.unit); }
        });
        if (style) {
          var mark = svg('svg', { width: 14, height: 14, viewBox: '0 0 14 14', 'aria-hidden': 'true' });
          mark.appendChild(svg('path', { d: markerPath(style.marker, 7, 7), fill: style.color, stroke: style.color, 'stroke-width': 1.2 }));
          button.appendChild(mark);
        } else {
          var plus = svg('svg', { width: 12, height: 12, viewBox: '0 0 12 12', 'aria-hidden': 'true' });
          plus.appendChild(svg('path', { d: 'M6 1.5v9M1.5 6h9', class: 'am-plus' }));
          button.appendChild(plus);
        }
        cell = button;
      }
      var tr = el('tr', { class: c.id === 'core' ? 'am-ref' : null }, [
        el('td', { class: 'am-toggle' }, cell),
        el('td', { class: 'am-label', html: c.id === 'core' ? 'Core scheme' : c.label + (c.rescored ? '†' : '') })
      ]);
      for (var i = 0; i < 8; i++) {
        tr.appendChild(el('td', { class: 'am-num' + (i === 5 ? ' am-sep' : ''), text: values ? c[st.unit + 'Text'][i] : '\u2013' }));
      }
      body.appendChild(tr);
    });

    var notes = [];
    if (rescored) notes.push('† Detector swap: rescores the texts of the corresponding generation, so only the TPRs change.');
    if (rows.some(function (c) { return !c.lexical; })) notes.push('– Not evaluated with this unit.');

    this.detail.innerHTML = '';
    append(this.detail, [
      el('div', { class: 'am-detail-head' }, [
        el('h4', { class: 'am-detail-title', html: comp.name }),
        el('span', { class: 'am-detail-meta', text: stage.name + (comp.prior ? ' · prior work' : '') + ' · ' + family })
      ]),
      el('p', { class: 'am-detail-desc', html: comp.desc }),
      el('div', { class: 'am-table-wrap' }, el('table', { class: 'am-table' }, [head, body])),
      notes.length ? el('p', { class: 'am-detail-foot', text: notes.join('  ') }) : null
    ]);
  };

  Explorer.prototype.renderSide = function () {
    var self = this;
    var st = this.state;
    var core = this.configs.core;
    var series = [{
      key: 'core|token', label: 'Core scheme', sub: 'Token', color: REFERENCE.color,
      dash: REFERENCE.dash, marker: 'none', values: core.token, text: core.tokenText
    }];
    st.selected.forEach(function (s) {
      var c = self.configs[s.id];
      series.push({
        key: s.id + '|' + s.unit, label: c.id === 'core' ? 'Core scheme' : c.label, sub: UNIT_NAMES[s.unit],
        color: SLOTS[s.slot].color, marker: SLOTS[s.slot].marker, values: c[s.unit], text: c[s.unit + 'Text']
      });
    });
    this.radar.update(series);

    this.legend.innerHTML = '';
    series.forEach(function (s, i) {
      var li = el('li', {
        onmouseenter: function () { self.radar.highlight(s.key); },
        onmouseleave: function () { self.radar.highlight(null); }
      });
      li.appendChild(swatch(s));
      if (i === 0) {
        li.appendChild(el('span', { class: 'am-legend-label' }, [
          'Core scheme', el('span', { class: 'am-legend-unit', text: '\u00a0· reference' })]));
      } else {
        var sel = st.selected[i - 1];
        var c = self.configs[sel.id];
        li.appendChild(el('button', {
          type: 'button', class: 'am-legend-label am-link', title: 'Show its component',
          onclick: function () { self.state.unit = sel.unit; self.select(c.id === 'core' ? 'lexical' : c.comps[0], true); }
        }, [el('span', { html: s.label }), el('span', { class: 'am-legend-unit', text: '\u00a0· ' + s.sub })]));
        li.appendChild(el('button', {
          type: 'button', class: 'am-remove', 'aria-label': 'Remove ' + plainText(s.label), html: '&times;',
          onclick: function () { self.toggle(sel.id, sel.unit); }
        }));
      }
      self.legend.appendChild(li);
    });
    if (!st.selected.length) {
      this.legend.appendChild(el('li', { class: 'am-empty', text: 'Use the + buttons in the table to plot configurations.' }));
    }
  };

  // ---- Held-out comparison ---------------------------------------------------------------------

  var SCHEMES = [
    { name: 'ConcordMark (high)', color: '#0079AF', marker: 'circle', on: true },
    { name: 'ConcordMark (low)', color: '#4a3aa7', marker: 'triangle-down', on: false },
    { name: 'RotationFirst', color: '#eb6834', marker: 'square', on: true },
    { name: 'TextSeal (high)', color: '#5f5f5f', marker: 'triangle', dash: '5 3', on: true },
    { name: 'SynthID', color: '#9a9a9a', marker: 'square', dash: '5 3', on: true },
    { name: 'AAR', color: '#9a9a9a', marker: 'diamond', dash: '1.5 3', on: false }
  ];

  function HeldOut(host) {
    var self = this;
    this.state = { model: 'Llama', language: 'english' };
    this.schemes = SCHEMES.map(function (s) { return Object.assign({}, s); });
    this.buttons = {};
    function segmented(label, field, options) {
      self.buttons[field] = {};
      return el('div', { class: 'am-control' }, [
        el('span', { class: 'am-control-label', text: label }),
        el('div', { class: 'am-segmented', role: 'group', 'aria-label': label }, options.map(function (o) {
          var b = el('button', {
            type: 'button', text: o[1],
            onclick: function () { self.state[field] = o[0]; self.render(); }
          });
          self.buttons[field][o[0]] = b;
          return b;
        }))
      ]);
    }
    var plot = el('div');
    this.radar = new Radar(plot, 'Radar plot of the held-out evaluation');
    this.legend = el('ul', { class: 'am-legend' });
    append(host, [
      el('div', {}, plot),
      el('div', {}, [
        el('div', { class: 'am-toolbar' }, [
          segmented('Model', 'model', [['Llama', 'Llama-3.1-8B'], ['Qwen', 'Qwen3.8-27B']]),
          segmented('Prompts', 'language', [['english', 'English'], ['chinese', 'Chinese']])
        ]),
        this.legend,
        el('p', { class: 'am-side-note', text: 'Select a scheme to show or hide it.' })
      ])
    ]);
    this.render();
  }

  HeldOut.prototype.render = function () {
    var self = this;
    var st = this.state;
    Object.keys(this.buttons).forEach(function (field) {
      Object.keys(self.buttons[field]).forEach(function (v) {
        self.buttons[field][v].setAttribute('aria-pressed', String(v === st[field]));
      });
    });
    var rows = {};
    DATA.heldout.forEach(function (r) { if (r.model === st.model) rows[r.scheme] = r[st.language]; });
    // Baselines are drawn first, below the agent schemes.
    var series = this.schemes.slice().reverse().filter(function (s) { return s.on; }).map(function (s) {
      return { key: s.name, label: s.name, color: s.color, dash: s.dash, marker: s.marker, values: rows[s.name] };
    });
    this.radar.update(series);
    this.legend.innerHTML = '';
    this.schemes.forEach(function (s) {
      var li = el('li', {
        class: s.on ? null : 'am-hidden-series',
        onmouseenter: function () { if (s.on) self.radar.highlight(s.name); },
        onmouseleave: function () { self.radar.highlight(null); }
      });
      li.appendChild(el('button', {
        type: 'button', class: 'am-toggle-series', 'aria-pressed': String(s.on),
        onclick: function () { s.on = !s.on; self.render(); }
      }, [swatch(s), el('span', { class: 'am-legend-label', text: s.name }),
        el('span', { class: 'am-legend-unit', text: 'Clean ' + fmt(rows[s.name][0], 0) + '%' })]));
      self.legend.appendChild(li);
    });
  };

  // ---- Boot ------------------------------------------------------------------------------------

  function boot() {
    var explorer = document.getElementById('am-explorer');
    if (explorer) { explorer.innerHTML = ''; new Explorer(explorer); }
    var heldout = document.getElementById('am-heldout');
    if (heldout) { heldout.innerHTML = ''; new HeldOut(heldout); }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
