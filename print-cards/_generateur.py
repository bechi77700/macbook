#!/usr/bin/env python3
"""
Genere des SVG print-ready avec le texte converti en courbes vectorielles.
Aucune dependance aux polices dans le fichier final.
"""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
import os

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
_cache = {}


def load(weight):
    if weight not in _cache:
        _cache[weight] = TTFont(os.path.join(FONT_DIR, f"Poppins-{weight}.ttf"))
    return _cache[weight]


def measure(text, weight, tracking=0.0):
    """Largeur du texte en unites em (1.0 = font-size). tracking en em."""
    f = load(weight)
    upm = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    gs = f.getGlyphSet()
    total = 0.0
    for i, ch in enumerate(text):
        gname = cmap.get(ord(ch))
        if gname is None:
            gname = ".notdef"
        total += hmtx[gname][0] / upm
        if i < len(text) - 1:
            total += tracking
    return total


def text_to_paths(text, weight, size, x, y, tracking=0.0, anchor="middle", fill="#FFFFFF"):
    """
    Retourne du markup SVG <path> pour le texte, converti en courbes.
    size = font-size dans les unites du document (mm)
    x, y = position ; y est la ligne de base
    anchor = start | middle | end
    """
    f = load(weight)
    upm = f["head"].unitsPerEm
    cmap = f.getBestCmap()
    hmtx = f["hmtx"]
    glyphset = f.getGlyphSet()

    width = measure(text, weight, tracking) * size
    if anchor == "middle":
        cursor = x - width / 2.0
    elif anchor == "end":
        cursor = x - width
    else:
        cursor = x

    scale = size / upm
    out = []
    for i, ch in enumerate(text):
        gname = cmap.get(ord(ch)) or ".notdef"
        if ch != " ":
            pen = SVGPathPen(glyphset)
            glyphset[gname].draw(pen)
            d = pen.getCommands()
            if d:
                # font Y monte, SVG Y descend -> scale(s, -s)
                out.append(
                    f'<g transform="translate({cursor:.4f},{y:.4f}) scale({scale:.6f},{-scale:.6f})">'
                    f'<path d="{d}" fill="{fill}"/></g>'
                )
        cursor += hmtx[gname][0] * scale
        if i < len(text) - 1:
            cursor += tracking * size

    return "\n    ".join(out)


def fit_size(text, weight, target_width, tracking=0.0):
    """Calcule le font-size pour que le texte fasse exactement target_width."""
    per_em = measure(text, weight, tracking)
    return target_width / per_em


# ============================================================
#  GEOMETRIE
#  Carte finale 148 x 105 mm + 3 mm de fond perdu = 154 x 111 mm
#  Les mesures viennent des visuels d'origine (1769 x 1245 px)
#  Conversion : px * (105 / 1245) + 3 mm de decalage fond perdu
# ============================================================
BLEED = 3.0
TRIM_W, TRIM_H = 148.0, 105.0
DOC_W, DOC_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED
PX = 105.0 / 1245.0          # facteur px -> mm
CX = BLEED + TRIM_W / 2.0    # centre horizontal du document

def mx(px_val):
    """px horizontal -> mm document"""
    return BLEED + px_val * PX

def my(px_val):
    """px vertical -> mm document"""
    return BLEED + px_val * PX


def crop_marks():
    m = []
    o = 'stroke="#FFFFFF" stroke-width="0.15" opacity="0.55" fill="none"'
    L, R = BLEED, DOC_W - BLEED
    T, B = BLEED, DOC_H - BLEED
    m.append(f'<line x1="{L}" y1="0" x2="{L}" y2="1.6" {o}/>')
    m.append(f'<line x1="{R}" y1="0" x2="{R}" y2="1.6" {o}/>')
    m.append(f'<line x1="{L}" y1="{DOC_H-1.6}" x2="{L}" y2="{DOC_H}" {o}/>')
    m.append(f'<line x1="{R}" y1="{DOC_H-1.6}" x2="{R}" y2="{DOC_H}" {o}/>')
    m.append(f'<line x1="0" y1="{T}" x2="1.6" y2="{T}" {o}/>')
    m.append(f'<line x1="0" y1="{B}" x2="1.6" y2="{B}" {o}/>')
    m.append(f'<line x1="{DOC_W-1.6}" y1="{T}" x2="{DOC_W}" y2="{T}" {o}/>')
    m.append(f'<line x1="{DOC_W-1.6}" y1="{B}" x2="{DOC_W}" y2="{B}" {o}/>')
    return "\n  ".join(m)


def svg_doc(title, body, note):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{DOC_W}mm" height="{DOC_H}mm"
     viewBox="0 0 {DOC_W} {DOC_H}" version="1.1">
  <title>{title}</title>
  <!--
    {note}
    Format final   : {TRIM_W:.0f} x {TRIM_H:.0f} mm (A6 paysage)
    Fond perdu     : {BLEED:.0f} mm par cote
    Fichier total  : {DOC_W:.0f} x {DOC_H:.0f} mm
    Texte converti en courbes vectorielles - aucune police requise.
  -->
  <rect x="0" y="0" width="{DOC_W}" height="{DOC_H}" fill="#000000"/>
  {crop_marks()}
  {body}
</svg>
'''


# ============================================================
#  CARTE 2 - RECTO : Danke
#  Releve des positions sur le visuel d'origine (px)
# ============================================================
def carte2_recto():
    el = []

    # logo EverHaar : largeur 840 px, ligne de base 330 px
    s = fit_size("EverHaar", 300, 840 * PX)
    el.append(text_to_paths("EverHaar", 300, s, CX, my(330), anchor="middle"))

    # HAIR CARE : largeur 370 px, ligne de base 385 px, tres espace
    tr = 0.30
    s = fit_size("HAIR CARE", 500, 370 * PX, tracking=tr)
    el.append(text_to_paths("HAIR CARE", 500, s, CX, my(385), tracking=tr, anchor="middle"))

    # titre 2 lignes, gras
    s1 = fit_size("Danke, dass Sie sich für", 700, 1170 * PX)
    s2 = fit_size("Everhaar entschieden haben.", 700, 1460 * PX)
    s = min(s1, s2)   # meme corps sur les 2 lignes
    el.append(text_to_paths("Danke, dass Sie sich für", 700, s, CX, my(612), anchor="middle"))
    el.append(text_to_paths("Everhaar entschieden haben.", 700, s, CX, my(695), anchor="middle"))

    # sous-texte 2 lignes, light
    b1 = "Ihre Unterstützung bedeutet uns viel, schön,"
    b2 = "dass Sie Teil unserer Community sind."
    s = min(fit_size(b1, 300, 1350 * PX), fit_size(b2, 300, 1140 * PX))
    el.append(text_to_paths(b1, 300, s, CX, my(858), anchor="middle"))
    el.append(text_to_paths(b2, 300, s, CX, my(908), anchor="middle"))

    return svg_doc("EverHaar - Carte 2 recto - Danke",
                   "\n  ".join(el),
                   "CARTE 2 - RECTO : Message de remerciement")


# ============================================================
#  CARTE 2 - VERSO : -20 %
# ============================================================
def carte2_verso():
    el = []

    # bandeau titre
    t = "–20 % AUF IHRE NÄCHSTE BESTELLUNG"
    tr = 0.015
    s = fit_size(t, 400, 1595 * PX, tracking=tr)
    el.append(text_to_paths(t, 400, s, CX, my(228), tracking=tr, anchor="middle"))

    # accroche 2 lignes, gras
    h1 = "Teilen Sie diesen Code gerne"
    h2 = "mit Familie & Freunden"
    s = min(fit_size(h1, 700, 1055 * PX), fit_size(h2, 700, 840 * PX))
    el.append(text_to_paths(h1, 700, s, CX, my(395), anchor="middle"))
    el.append(text_to_paths(h2, 700, s, CX, my(465), anchor="middle"))

    # corps 3 lignes, light
    b1 = "Genießen Sie –20 % auf den Gesamtbetrag Ihrer Bestellung."
    b2 = "Machen Sie auch Ihren Liebsten eine Freude, indem Sie diesen"
    b3 = "Code weitergeben!"
    s = min(fit_size(b1, 300, 1125 * PX), fit_size(b2, 300, 1190 * PX))
    el.append(text_to_paths(b1, 300, s, CX, my(595), anchor="middle"))
    el.append(text_to_paths(b2, 300, s, CX, my(632), anchor="middle"))
    el.append(text_to_paths(b3, 300, s, CX, my(669), anchor="middle"))

    # pastille du code promo
    bx, by = mx(518), my(775)
    bw, bh = (1232 - 518) * PX, (885 - 775) * PX
    el.append(f'<rect x="{bx:.3f}" y="{by:.3f}" width="{bw:.3f}" height="{bh:.3f}" '
              f'rx="{2.0}" ry="{2.0}" fill="#5B6478"/>')

    code = "CODE = DANKE20"
    s = fit_size(code, 700, 640 * PX)
    el.append(text_to_paths(code, 700, s, CX, my(852), anchor="middle"))

    return svg_doc("EverHaar - Carte 2 verso - Code promo",
                   "\n  ".join(el),
                   "CARTE 2 - VERSO : -20 % code DANKE20")


if __name__ == "__main__":
    out = "/home/user/macbook/print-cards"
    os.makedirs(out, exist_ok=True)
    jobs = [("carte2-recto-danke.svg", carte2_recto()),
            ("carte2-verso-discount.svg", carte2_verso())]
    for name, content in jobs:
        p = os.path.join(out, name)
        open(p, "w", encoding="utf-8").write(content)
        print(f"{name}  ->  {len(content)/1024:.1f} Ko")
