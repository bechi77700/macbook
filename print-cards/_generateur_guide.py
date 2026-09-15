#!/usr/bin/env python3
"""
Guide d'utilisation EverHaar - depliant accordeon 4 volets.
Texte converti en courbes vectorielles.
Source : visuel 1600 x 830 px  ->  280 x 145 mm
"""
import os, base64
from build_cards import text_to_paths, measure
import icons as I

BLEED = 3.0
TRIM_W, TRIM_H = 280.0, 145.0
DOC_W, DOC_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED
PX = TRIM_W / 1600.0            # 0.175 mm par px source

def X(v): return BLEED + v * PX
def Y(v): return BLEED + v * PX
def S(v): return v * PX

# ---- palette ------------------------------------------------------
WHITE   = "#FFFFFF"
BODY    = "#C9CEDA"      # corps de texte
BODY_2  = "#DDE2EA"      # corps sur la photo (plus contraste)
CHIP_BG = "#79808E"      # pastilles SCHRITT
RING    = "#FFFFFF"

# degrade de fond : mauve ardoise a gauche -> bleu nuit profond a droite
GRADIENT = [
    (0.00, "#5A5468"),
    (0.14, "#565064"),
    (0.25, "#4A4658"),
    (0.34, "#343243"),
    (0.46, "#1E2130"),
    (0.62, "#161A26"),
    (0.80, "#11141E"),
    (1.00, "#0C0F17"),
]

T_TITLE = S(17.0)
T_BODY  = S(15.7)
T_C2    = S(15.0)
T_STEP  = S(14.5)
T_C34   = S(14.5)

PHOTO_X0, PHOTO_X1 = 412, 795   # colonne photo, en px source


def block(lines, size, x, ybase, lead, weight=300, anchor="start",
          fill=BODY, tracking=0.0):
    return [o for o in
            (text_to_paths(ln, weight, size, x, Y(ybase + i * lead),
                           tracking=tracking, anchor=anchor, fill=fill)
             for i, ln in enumerate(lines)) if o]


def ring(cx, cy, r, sw=1.15):
    return (f'<circle cx="{X(cx):.3f}" cy="{Y(cy):.3f}" r="{S(r):.3f}" '
            f'fill="none" stroke="{RING}" stroke-width="{S(sw):.3f}" opacity="0.80"/>')


def icon(art, cx, cy, r):
    return I.wrap(X(cx), Y(cy), r, art, PX)


def chip(text, size, x, ybase, anchor="middle"):
    tr = 0.06
    w = measure(text, 600, tr) * size
    pad = size * 0.30
    rx = X(x) - (w / 2 + pad if anchor == "middle" else pad)
    ry = Y(ybase) - size * 1.00
    return [f'<rect x="{rx:.3f}" y="{ry:.3f}" width="{w + pad*2:.3f}" '
            f'height="{size*1.38:.3f}" rx="{size*0.10:.3f}" '
            f'fill="{CHIP_BG}" opacity="0.62"/>',
            text_to_paths(text, 600, size, X(x), Y(ybase),
                          tracking=tr, anchor=anchor, fill=WHITE)]


# ------------------------------------------------------------------
#  CONTENU
# ------------------------------------------------------------------
COL1 = [
    (I.HAND_RASH, 152, ["Der Hauttest Rötungen,", "Schwellungen oder Blasen", "zeigt."], 140),
    (I.SKIN_CUT,  291, ["Sie kürzlich rasiert haben", "oder die Haut Schnitte",
                        "oder Verletzungen", "aufweist."], 273),
    (I.ALLERGY,   428, ["Sie an Allergien,", "empfindlicher Haut,",
                        "Entzündungen oder", "Hauterkrankungen leiden."], 410),
    (I.PREGNANT,  566, ["Sie schwanger sind."], 578),
    (I.UNDER16,   692, ["Sie unter 16 Jahre alt sind."], 710),
]

COL2_TEXT = [
    (142, ["Haartropfen und Schaum können", "Oberflächen wie Kleidung, Böden oder",
           "Badewannen verfärben."]),
    (221, ["Reinigen Sie betroffene Bereiche sofort", "nach dem Kontakt."]),
    (278, ["Die Verwendung von warmem Wasser", "verbessert den Färbeprozess."]),
    (335, ["Diese milde Formel enthält weder", "Bleichmittel noch Tönungsmittel, daher",
           "hängen das Farbergebnis und die", "Haltbarkeit vom Haartyp ab."]),
]

COL3 = [
    (I.PUMP_BOTTLE, 155, "SCHRITT 1", 228, ["2–3 Pumpstöße auf die Hände geben."], 247),
    (I.FOAM_HEAD,   322, "SCHRITT 2", 396, ["Gleichmäßig auf das trockene Haar auftragen",
                                            "und 10 Minuten einwirken lassen."], 415),
    (I.SHOWER,      508, "SCHRITT 3", 582, ["Haare gründlich ausspülen."], 601),
    (I.GLOW_FACE,   676, "SCHRITT 4", 750, ["Genieße deine neue, intensive Farbe."], 769),
]

COL4 = [
    (I.WASH_HANDS,   168, "SCHRITT 1", 145, ["Reinige und trockne den", "Bereich hinter dem Ohr",
                                             "oder das innere", "Handgelenk mit Seife."], 167),
    (I.DROPPER_HAND, 310, "SCHRITT 2", 292, ["Trage eine kleine Menge", "Shampoo auf."], 315),
    (I.DAB_SKIN,     440, "SCHRITT 3", 432, ["Tupfe es sanft auf die Haut."], 455),
    (I.TIMER_48H,    565, "SCHRITT 4", 552, ["48 Stunden lang unberührt", "lassen."], 575),
    (I.SAFE_SKIN,    692, "SCHRITT 5", 662, ["Wenn keine Rötung, Reizung",
                                             "oder allergische Reaktion",
                                             "auftritt, ist es sicher in der",
                                             "Anwendung."], 690),
]


def photo_panel(photo_path=None):
    """Volet 2 : photo encapsulee en base64, ou zone reservee."""
    x = X(PHOTO_X0)
    w = S(PHOTO_X1 - PHOTO_X0)
    out = []
    if photo_path and os.path.exists(photo_path):
        ext = os.path.splitext(photo_path)[1].lower()
        mime = "image/png" if ext == ".png" else "image/jpeg"
        b64 = base64.b64encode(open(photo_path, "rb").read()).decode()
        out.append(f'<clipPath id="pclip"><rect x="{x:.3f}" y="0" '
                   f'width="{w:.3f}" height="{DOC_H:.3f}"/></clipPath>')
        out.append(f'<image clip-path="url(#pclip)" x="{x:.3f}" y="0" '
                   f'width="{w:.3f}" height="{DOC_H:.3f}" '
                   f'preserveAspectRatio="xMidYMid slice" '
                   f'xlink:href="data:{mime};base64,{b64}" '
                   f'xmlns:xlink="http://www.w3.org/1999/xlink"/>')
        # voile sombre pour que le texte blanc tienne
        out.append(f'<rect x="{x:.3f}" y="0" width="{w:.3f}" height="{DOC_H:.3f}" '
                   f'fill="#0E1119" opacity="0.46"/>')
        out.append(f'<rect x="{x:.3f}" y="0" width="{w:.3f}" height="{S(470):.3f}" '
                   f'fill="url(#topveil)"/>')
    else:
        out.append(f'<rect x="{x:.3f}" y="0" width="{w:.3f}" height="{DOC_H:.3f}" '
                   f'fill="#39404E"/>')
        out.append(text_to_paths("[ ZONE PHOTO - A PLACER ]", 400, S(13),
                                 X(604), Y(640), tracking=0.08,
                                 anchor="middle", fill="#818C9C"))
    return out


def build(photo_path=None):
    el = []

    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in GRADIENT)
    el.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">{stops}</linearGradient>
    <linearGradient id="topveil" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#0E1119" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#0E1119" stop-opacity="0"/>
    </linearGradient>
  </defs>''')
    el.append(f'<rect x="0" y="0" width="{DOC_W}" height="{DOC_H}" fill="url(#bg)"/>')

    el += photo_panel(photo_path)

    # ---- reperes de coupe ----
    o = f'stroke="{WHITE}" stroke-width="0.15" opacity="0.55" fill="none"'
    for xx in (BLEED, DOC_W - BLEED):
        el.append(f'<line x1="{xx}" y1="0" x2="{xx}" y2="1.6" {o}/>')
        el.append(f'<line x1="{xx}" y1="{DOC_H-1.6}" x2="{xx}" y2="{DOC_H}" {o}/>')
    for yy in (BLEED, DOC_H - BLEED):
        el.append(f'<line x1="0" y1="{yy}" x2="1.6" y2="{yy}" {o}/>')
        el.append(f'<line x1="{DOC_W-1.6}" y1="{yy}" x2="{DOC_W}" y2="{yy}" {o}/>')
    for i in (1, 2, 3):
        px = BLEED + i * (TRIM_W / 4.0)
        el.append(f'<line x1="{px:.3f}" y1="{BLEED}" x2="{px:.3f}" y2="{DOC_H-BLEED}" '
                  f'stroke="{WHITE}" stroke-width="0.12" stroke-dasharray="1.2,1.2" '
                  f'opacity="0.20"/>')

    # ================= COLONNE 1 =================
    el.append(text_to_paths("NICHT VERWENDEN, WENN", 700, T_TITLE, X(206), Y(78),
                            tracking=0.09, anchor="middle", fill=WHITE))
    for art, cy, lines, y0 in COL1:
        el.append(ring(78, cy, 33))
        el.append(icon(art, 78, cy, 33))
        el += block(lines, T_BODY, X(148), y0, 22)

    # ================= COLONNE 2 =================
    el.append(text_to_paths("TIPPS ZUM FÄRBEN", 700, T_TITLE, X(604), Y(78),
                            tracking=0.09, anchor="middle", fill=WHITE))
    el.append(text_to_paths("DER HAARE", 700, T_TITLE, X(604), Y(103),
                            tracking=0.09, anchor="middle", fill=WHITE))
    for y0, lines in COL2_TEXT:
        el += block(lines, T_C2, X(604), y0, 22, anchor="middle", fill=BODY_2)

    # ================= COLONNE 3 =================
    el.append(text_to_paths("ANWENDUNG", 700, T_TITLE, X(1000), Y(78),
                            tracking=0.09, anchor="middle", fill=WHITE))
    for art, cy, lbl, ylbl, lines, y0 in COL3:
        el.append(ring(1000, cy, 38))
        el.append(icon(art, 1000, cy, 38))
        el += chip(lbl, T_STEP, 1000, ylbl, anchor="middle")
        el += block(lines, T_C34, X(1000), y0, 21, anchor="middle")

    # ================= COLONNE 4 =================
    el.append(text_to_paths("EMPFINDLICHKEITSTEST", 700, T_TITLE, X(1400), Y(78),
                            tracking=0.07, anchor="middle", fill=WHITE))
    el.append(text_to_paths("DER HAUT", 700, T_TITLE, X(1400), Y(103),
                            tracking=0.07, anchor="middle", fill=WHITE))
    for art, cy, lbl, ylbl, lines, y0 in COL4:
        el.append(ring(1295, cy, 42))
        el.append(icon(art, 1295, cy, 42))
        el += chip(lbl, T_STEP, 1352, ylbl, anchor="start")
        el += block(lines, T_C34, X(1352), y0, 19)

    body = "\n  ".join(x for x in el if x)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{DOC_W}mm" height="{DOC_H}mm"
     viewBox="0 0 {DOC_W} {DOC_H}" version="1.1">
  <title>EverHaar - Guide d'utilisation</title>
  <!--
    GUIDE UTILISATION - depliant accordeon 4 volets
    Format deplie  : {TRIM_W:.0f} x {TRIM_H:.0f} mm
    Format plie    : {TRIM_W/4:.0f} x {TRIM_H:.0f} mm (4 volets)
    Fond perdu     : {BLEED:.0f} mm par cote
    Fichier total  : {DOC_W:.0f} x {DOC_H:.0f} mm
    Pliage         : accordeon, 3 plis (pointilles)
    Texte converti en courbes - aucune police requise.
  -->
  {body}
</svg>
'''


if __name__ == "__main__":
    import sys
    photo = sys.argv[1] if len(sys.argv) > 1 else None
    p = "/home/user/macbook/print-cards/guide-depliant-shampooing.svg"
    open(p, "w", encoding="utf-8").write(build(photo))
    tag = "avec photo" if photo and os.path.exists(photo) else "zone reservee"
    print(f"guide-depliant-shampooing.svg -> {os.path.getsize(p)/1024:.1f} Ko ({tag})")
