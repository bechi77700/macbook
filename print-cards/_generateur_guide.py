#!/usr/bin/env python3
"""
Guide d'utilisation EverHaar - depliant accordeon 4 volets.
Texte converti en courbes vectorielles.
Source : visuel 1600 x 830 px  ->  280 x 145 mm
"""
import os
from build_cards import text_to_paths, fit_size, fit_tracking, measure

BLEED = 3.0
TRIM_W, TRIM_H = 280.0, 145.0
DOC_W, DOC_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED
PX = TRIM_W / 1600.0            # 0.175 mm par px source

def X(v): return BLEED + v * PX
def Y(v): return BLEED + v * PX
def S(v): return v * PX          # taille/longueur

WHITE = "#FFFFFF"
DIM   = "#D6DAE2"                # corps de texte legerement adouci
CHIP  = "#6E7480"                # fond des pastilles SCHRITT

# tailles de corps relevees sur le visuel
T_TITLE = S(17.0)                # titres de colonne
T_BODY  = S(15.7)                # corps colonne 1
T_C2    = S(15.0)                # corps colonne 2
T_STEP  = S(14.5)                # libelle SCHRITT
T_C34   = S(14.5)                # corps colonnes 3 et 4


def block(lines, size, x, ybase, lead, weight=300, anchor="start",
          fill=DIM, tracking=0.0):
    """Bloc de lignes, interligne constant."""
    out = []
    for i, ln in enumerate(lines):
        out.append(text_to_paths(ln, weight, size, x, Y(ybase + i * lead),
                                 tracking=tracking, anchor=anchor, fill=fill))
    return [o for o in out if o]


def ring(cx, cy, r, sw=1.1):
    return (f'<circle cx="{X(cx):.3f}" cy="{Y(cy):.3f}" r="{S(r):.3f}" '
            f'fill="none" stroke="{WHITE}" stroke-width="{S(sw):.3f}" opacity="0.85"/>')


def chip(text, size, cx_or_x, ybase, anchor="middle"):
    """Pastille grise + libelle SCHRITT n."""
    tr = 0.06
    w = measure(text, 600, tr) * size
    h = size * 1.35
    if anchor == "middle":
        rx = X(cx_or_x) - w / 2 - size * 0.28
    else:
        rx = X(cx_or_x) - size * 0.28
    ry = Y(ybase) - size * 0.98
    out = [f'<rect x="{rx:.3f}" y="{ry:.3f}" width="{w + size*0.56:.3f}" '
           f'height="{h:.3f}" fill="{CHIP}" opacity="0.55"/>']
    ax = cx_or_x if anchor == "middle" else cx_or_x
    out.append(text_to_paths(text, 600, size, X(ax), Y(ybase),
                             tracking=tr, anchor=anchor, fill=WHITE))
    return out


# ------------------------------------------------------------------
#  ICONES  (trait fin, dans un cercle) - dessinees en vectoriel
#  Chaque fonction recoit le centre (cx, cy) et le rayon en px source.
# ------------------------------------------------------------------
def _g(cx, cy, r, inner, sw=1.05):
    """Place un dessin normalise (-1..1) dans le cercle."""
    k = S(r) * 0.62
    return (f'<g transform="translate({X(cx):.3f},{Y(cy):.3f}) scale({k:.4f})" '
            f'fill="none" stroke="{WHITE}" stroke-width="{S(sw)/k:.4f}" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="0.9">{inner}</g>')


def ic_hand_rash(cx, cy, r):
    d = ('<path d="M-0.30,0.75 L-0.30,0.05 C-0.30,-0.10 -0.52,-0.20 -0.52,-0.34 '
         'C-0.52,-0.46 -0.38,-0.48 -0.30,-0.36 L-0.10,-0.02 L-0.10,-0.62 '
         'C-0.10,-0.76 0.10,-0.76 0.10,-0.62 L0.10,-0.16 L0.10,-0.70 '
         'C0.10,-0.84 0.30,-0.84 0.30,-0.70 L0.30,-0.16 L0.30,-0.58 '
         'C0.30,-0.72 0.50,-0.72 0.50,-0.58 L0.50,0.16 '
         'C0.50,0.52 0.30,0.75 0.05,0.75 Z"/>'
         '<circle cx="-0.02" cy="0.18" r="0.05"/>'
         '<circle cx="0.22" cy="0.34" r="0.05"/>'
         '<circle cx="0.16" cy="0.02" r="0.04"/>')
    return _g(cx, cy, r, d)


def ic_skin_dots(cx, cy, r):
    d = ('<path d="M-0.72,-0.30 C-0.40,-0.52 -0.10,-0.10 0.20,-0.34 '
         'C0.44,-0.52 0.62,-0.34 0.74,-0.24"/>'
         '<path d="M-0.72,0.12 C-0.40,-0.10 -0.10,0.32 0.20,0.08 '
         'C0.44,-0.10 0.62,0.08 0.74,0.18"/>'
         '<circle cx="-0.42" cy="0.44" r="0.06"/>'
         '<circle cx="0.02" cy="0.52" r="0.06"/>'
         '<circle cx="0.44" cy="0.44" r="0.06"/>'
         '<circle cx="-0.20" cy="-0.60" r="0.05"/>'
         '<circle cx="0.34" cy="-0.62" r="0.05"/>')
    return _g(cx, cy, r, d)


def ic_cracked(cx, cy, r):
    d = ('<path d="M-0.78,-0.16 L-0.30,-0.34 L0.04,-0.06 L0.46,-0.30 L0.80,-0.12"/>'
         '<path d="M-0.30,-0.34 L-0.40,-0.74"/>'
         '<path d="M0.04,-0.06 L0.00,0.40"/>'
         '<path d="M0.46,-0.30 L0.60,-0.70"/>'
         '<path d="M-0.72,0.42 L-0.34,0.24 L0.00,0.40 L0.40,0.22 L0.78,0.44"/>'
         '<path d="M-0.34,0.24 L-0.44,0.72"/>'
         '<path d="M0.40,0.22 L0.50,0.70"/>')
    return _g(cx, cy, r, d)


def ic_pregnant(cx, cy, r):
    d = ('<circle cx="-0.06" cy="-0.60" r="0.20"/>'
         '<path d="M-0.06,-0.38 C-0.26,-0.30 -0.34,-0.10 -0.32,0.12 '
         'C-0.30,0.40 -0.24,0.60 -0.30,0.82"/>'
         '<path d="M-0.06,-0.34 C0.16,-0.28 0.34,-0.06 0.34,0.16 '
         'C0.34,0.38 0.18,0.50 0.00,0.50"/>'
         '<path d="M0.00,0.50 C0.06,0.64 0.08,0.74 0.06,0.84"/>')
    return _g(cx, cy, r, d)


def ic_under16(cx, cy, r):
    d = ('<circle cx="0" cy="-0.05" r="0.56"/>'
         '<circle cx="-0.22" cy="-0.14" r="0.05"/>'
         '<circle cx="0.22" cy="-0.14" r="0.05"/>'
         '<path d="M-0.22,0.20 C-0.08,0.34 0.08,0.34 0.22,0.20"/>'
         '<path d="M-0.62,0.62 L0.62,-0.72"/>')
    return _g(cx, cy, r, d)


def ic_pump(cx, cy, r):
    d = ('<path d="M0.02,-0.72 L0.34,-0.72 L0.34,-0.54"/>'
         '<path d="M0.34,-0.54 L0.12,-0.54 L0.12,-0.40"/>'
         '<rect x="-0.14" y="-0.40" width="0.56" height="0.86" rx="0.12"/>'
         '<path d="M-0.34,-0.42 C-0.52,-0.24 -0.58,-0.08 -0.46,0.04 '
         'C-0.36,0.14 -0.20,0.10 -0.20,-0.06 C-0.20,-0.20 -0.26,-0.32 -0.34,-0.42 Z"/>'
         '<path d="M-0.62,0.46 C-0.44,0.62 -0.18,0.66 0.00,0.60"/>')
    return _g(cx, cy, r, d)


def ic_wash_head(cx, cy, r):
    d = ('<path d="M-0.34,0.10 C-0.40,-0.32 -0.20,-0.56 0.02,-0.56 '
         'C0.26,-0.56 0.44,-0.34 0.40,0.06 C0.38,0.34 0.24,0.52 0.02,0.52 '
         'C-0.18,0.52 -0.32,0.36 -0.34,0.10 Z"/>'
         '<circle cx="-0.30" cy="-0.52" r="0.14"/>'
         '<circle cx="0.02" cy="-0.68" r="0.14"/>'
         '<circle cx="0.34" cy="-0.52" r="0.13"/>'
         '<circle cx="-0.48" cy="-0.26" r="0.11"/>'
         '<circle cx="0.52" cy="-0.26" r="0.11"/>'
         '<circle cx="-0.12" cy="0.02" r="0.045"/>'
         '<circle cx="0.18" cy="0.02" r="0.045"/>'
         '<path d="M-0.06,0.26 C0.02,0.32 0.10,0.32 0.16,0.26"/>')
    return _g(cx, cy, r, d)


def ic_shower(cx, cy, r):
    d = ('<path d="M-0.50,-0.44 L0.50,-0.44 C0.42,-0.64 0.20,-0.74 0.00,-0.74 '
         'C-0.20,-0.74 -0.42,-0.64 -0.50,-0.44 Z"/>'
         '<path d="M-0.34,-0.18 L-0.44,0.30"/>'
         '<path d="M-0.10,-0.18 L-0.16,0.46"/>'
         '<path d="M0.14,-0.18 L0.20,0.46"/>'
         '<path d="M0.38,-0.18 L0.48,0.30"/>'
         '<path d="M-0.26,0.48 L-0.30,0.72"/>'
         '<path d="M0.04,0.56 L0.02,0.78"/>'
         '<path d="M0.32,0.48 L0.38,0.72"/>')
    return _g(cx, cy, r, d)


def ic_face_shine(cx, cy, r):
    d = ('<path d="M0.10,-0.66 C0.36,-0.56 0.50,-0.30 0.48,0.02 '
         'C0.46,0.36 0.26,0.62 -0.04,0.66 C-0.10,0.67 -0.16,0.66 -0.20,0.64"/>'
         '<path d="M0.10,-0.66 C-0.10,-0.72 -0.28,-0.64 -0.36,-0.48"/>'
         '<circle cx="0.18" cy="-0.10" r="0.045"/>'
         '<path d="M0.06,0.24 C0.16,0.30 0.28,0.28 0.34,0.20"/>'
         '<path d="M-0.56,-0.46 L-0.56,-0.20 M-0.69,-0.33 L-0.43,-0.33"/>'
         '<path d="M-0.62,0.22 L-0.62,0.42 M-0.72,0.32 L-0.52,0.32"/>'
         '<path d="M-0.30,-0.78 L-0.30,-0.62 M-0.38,-0.70 L-0.22,-0.70"/>')
    return _g(cx, cy, r, d)


def ic_tap_hands(cx, cy, r):
    d = ('<path d="M-0.72,-0.66 L-0.30,-0.66 L-0.30,-0.40"/>'
         '<path d="M-0.30,-0.40 L-0.06,-0.40"/>'
         '<path d="M-0.18,-0.22 L-0.22,0.00 M0.00,-0.22 L0.00,0.04 '
         'M0.18,-0.22 L0.22,0.00"/>'
         '<path d="M-0.56,0.30 C-0.46,0.10 -0.22,0.12 -0.06,0.26 '
         'C0.10,0.40 0.34,0.36 0.48,0.22"/>'
         '<path d="M-0.56,0.30 C-0.60,0.52 -0.44,0.70 -0.18,0.70 '
         'L0.24,0.70 C0.46,0.70 0.58,0.52 0.48,0.22"/>'
         '<circle cx="-0.34" cy="0.50" r="0.05"/>'
         '<circle cx="0.02" cy="0.54" r="0.05"/>'
         '<circle cx="0.30" cy="0.48" r="0.05"/>')
    return _g(cx, cy, r, d)


def ic_dropper(cx, cy, r):
    d = ('<path d="M-0.62,0.74 L-0.62,0.10 C-0.62,-0.04 -0.78,-0.14 -0.78,-0.28 '
         'C-0.78,-0.40 -0.66,-0.42 -0.58,-0.30 L-0.42,-0.02 L-0.42,-0.56 '
         'C-0.42,-0.70 -0.24,-0.70 -0.24,-0.56 L-0.24,-0.14 L-0.24,-0.64 '
         'C-0.24,-0.78 -0.06,-0.78 -0.06,-0.64 L-0.06,-0.14 L-0.06,-0.52 '
         'C-0.06,-0.66 0.12,-0.66 0.12,-0.52 L0.12,0.16 '
         'C0.12,0.50 -0.06,0.74 -0.28,0.74 Z"/>'
         '<path d="M0.46,-0.72 L0.72,-0.46 L0.46,-0.20 L0.34,-0.32 Z"/>'
         '<path d="M0.36,-0.12 C0.28,0.02 0.24,0.12 0.30,0.20 '
         'C0.36,0.27 0.47,0.24 0.47,0.14 C0.47,0.05 0.42,-0.04 0.36,-0.12 Z"/>')
    return _g(cx, cy, r, d)


def ic_dab(cx, cy, r):
    d = ('<rect x="-0.76" y="-0.62" width="1.52" height="1.24" rx="0.10"/>'
         '<path d="M-0.50,0.30 C-0.30,0.10 -0.06,0.02 0.16,0.04 '
         'C0.34,0.06 0.48,0.00 0.56,-0.12"/>'
         '<path d="M-0.34,0.36 C-0.20,0.22 -0.02,0.16 0.16,0.18"/>'
         '<path d="M0.10,-0.30 L0.10,-0.10 M0.00,-0.20 L0.20,-0.20"/>'
         '<path d="M-0.30,-0.40 L-0.30,-0.26 M-0.37,-0.33 L-0.23,-0.33"/>')
    return _g(cx, cy, r, d)


def ic_timer(cx, cy, r):
    d = ('<circle cx="0" cy="0.10" r="0.58"/>'
         '<path d="M-0.20,-0.66 L0.20,-0.66"/>'
         '<path d="M0,-0.66 L0,-0.48"/>'
         '<path d="M0.44,-0.52 L0.58,-0.38"/>'
         '<path d="M0,0.10 L0,-0.22 M0,0.10 L0.24,0.26"/>')
    return _g(cx, cy, r, d)


def ic_sparkle_skin(cx, cy, r):
    d = ('<path d="M-0.30,-0.50 L-0.30,-0.14 M-0.48,-0.32 L-0.12,-0.32"/>'
         '<path d="M0.26,-0.66 L0.26,-0.38 M0.12,-0.52 L0.40,-0.52"/>'
         '<path d="M0.44,-0.14 L0.44,0.06 M0.34,-0.04 L0.54,-0.04"/>'
         '<path d="M-0.76,0.34 C-0.50,0.18 -0.22,0.44 0.06,0.30 '
         'C0.32,0.16 0.54,0.30 0.76,0.40"/>'
         '<path d="M-0.76,0.64 C-0.50,0.48 -0.22,0.74 0.06,0.60 '
         'C0.32,0.46 0.54,0.60 0.76,0.70"/>')
    return _g(cx, cy, r, d)


# ------------------------------------------------------------------
#  CONTENU
# ------------------------------------------------------------------
COL1 = [
    (ic_hand_rash, 152, ["Der Hauttest Rötungen,", "Schwellungen oder Blasen", "zeigt."], 140),
    (ic_skin_dots, 291, ["Sie kürzlich rasiert haben", "oder die Haut Schnitte",
                         "oder Verletzungen", "aufweist."], 273),
    (ic_cracked,   428, ["Sie an Allergien,", "empfindlicher Haut,",
                         "Entzündungen oder", "Hauterkrankungen leiden."], 410),
    (ic_pregnant,  566, ["Sie schwanger sind."], 578),
    (ic_under16,   692, ["Sie unter 16 Jahre alt sind."], 710),
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
    (ic_pump,       155, "SCHRITT 1", 228, ["2–3 Pumpstöße auf die Hände geben."], 247),
    (ic_wash_head,  322, "SCHRITT 2", 396, ["Gleichmäßig auf das trockene Haar auftragen",
                                            "und 10 Minuten einwirken lassen."], 415),
    (ic_shower,     508, "SCHRITT 3", 582, ["Haare gründlich ausspülen."], 601),
    (ic_face_shine, 676, "SCHRITT 4", 750, ["Genieße deine neue, intensive Farbe."], 769),
]

COL4 = [
    (ic_tap_hands,    168, "SCHRITT 1", 145, ["Reinige und trockne den", "Bereich hinter dem Ohr",
                                              "oder das innere", "Handgelenk mit Seife."], 167),
    (ic_dropper,      310, "SCHRITT 2", 292, ["Trage eine kleine Menge", "Shampoo auf."], 315),
    (ic_dab,          440, "SCHRITT 3", 432, ["Tupfe es sanft auf die Haut."], 455),
    (ic_timer,        565, "SCHRITT 4", 552, ["48 Stunden lang unberührt", "lassen."], 575),
    (ic_sparkle_skin, 692, "SCHRITT 5", 662, ["Wenn keine Rötung, Reizung",
                                              "oder allergische Reaktion",
                                              "auftritt, ist es sicher in der",
                                              "Anwendung."], 690),
]


def build():
    el = []

    # ---- fond degrade ----
    el.append(f'''<defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0.00" stop-color="#4E4E60"/>
      <stop offset="0.22" stop-color="#4A4A5C"/>
      <stop offset="0.30" stop-color="#2E3440"/>
      <stop offset="0.48" stop-color="#181D26"/>
      <stop offset="0.72" stop-color="#12171F"/>
      <stop offset="1.00" stop-color="#0D1219"/>
    </linearGradient>
  </defs>''')
    el.append(f'<rect x="0" y="0" width="{DOC_W}" height="{DOC_H}" fill="url(#bg)"/>')

    # ---- reperes de coupe + plis ----
    o = f'stroke="{WHITE}" stroke-width="0.15" opacity="0.55" fill="none"'
    L, R, T, B = BLEED, DOC_W - BLEED, BLEED, DOC_H - BLEED
    for xx in (L, R):
        el.append(f'<line x1="{xx}" y1="0" x2="{xx}" y2="1.6" {o}/>')
        el.append(f'<line x1="{xx}" y1="{DOC_H-1.6}" x2="{xx}" y2="{DOC_H}" {o}/>')
    for yy in (T, B):
        el.append(f'<line x1="0" y1="{yy}" x2="1.6" y2="{yy}" {o}/>')
        el.append(f'<line x1="{DOC_W-1.6}" y1="{yy}" x2="{DOC_W}" y2="{yy}" {o}/>')
    # lignes de pliure
    for i in (1, 2, 3):
        px = BLEED + i * (TRIM_W / 4.0)
        el.append(f'<line x1="{px:.3f}" y1="{BLEED}" x2="{px:.3f}" y2="{DOC_H-BLEED}" '
                  f'stroke="{WHITE}" stroke-width="0.12" stroke-dasharray="1.2,1.2" '
                  f'opacity="0.22"/>')

    # ================= COLONNE 1 =================
    t = "NICHT VERWENDEN, WENN"
    tr = 0.09
    el.append(text_to_paths(t, 700, T_TITLE, X(206), Y(78),
                            tracking=tr, anchor="middle", fill=WHITE))
    for icon, cy, lines, y0 in COL1:
        el.append(ring(78, cy, 33))
        el.append(icon(78, cy, 33))
        el += block(lines, T_BODY, X(148), y0, 22)

    # ================= COLONNE 2 =================
    # zone photo reservee - plein fond perdu en haut et en bas
    el.append(f'<rect x="{X(412):.3f}" y="0" '
              f'width="{S(383):.3f}" height="{DOC_H:.3f}" fill="#3A4450"/>')
    el.append(f'<rect x="{X(412):.3f}" y="0" '
              f'width="{S(383):.3f}" height="{DOC_H:.3f}" fill="#000000" opacity="0.30"/>')
    el.append(text_to_paths("[ ZONE PHOTO - A PLACER ]", 400, S(13),
                            X(604), Y(640), tracking=0.08, anchor="middle", fill="#7C8896"))

    el.append(text_to_paths("TIPPS ZUM FÄRBEN", 700, T_TITLE, X(604), Y(78),
                            tracking=0.09, anchor="middle", fill=WHITE))
    el.append(text_to_paths("DER HAARE", 700, T_TITLE, X(604), Y(103),
                            tracking=0.09, anchor="middle", fill=WHITE))
    for y0, lines in COL2_TEXT:
        el += block(lines, T_C2, X(604), y0, 22, anchor="middle", fill="#E2E6EC")

    # ================= COLONNE 3 =================
    el.append(text_to_paths("ANWENDUNG", 700, T_TITLE, X(1000), Y(78),
                            tracking=0.09, anchor="middle", fill=WHITE))
    for icon, cy, lbl, ylbl, lines, y0 in COL3:
        el.append(ring(1000, cy, 38))
        el.append(icon(1000, cy, 38))
        el += chip(lbl, T_STEP, 1000, ylbl, anchor="middle")
        el += block(lines, T_C34, X(1000), y0, 21, anchor="middle")

    # ================= COLONNE 4 =================
    el.append(text_to_paths("EMPFINDLICHKEITSTEST", 700, T_TITLE, X(1400), Y(78),
                            tracking=0.07, anchor="middle", fill=WHITE))
    el.append(text_to_paths("DER HAUT", 700, T_TITLE, X(1400), Y(103),
                            tracking=0.07, anchor="middle", fill=WHITE))
    for icon, cy, lbl, ylbl, lines, y0 in COL4:
        el.append(ring(1295, cy, 42))
        el.append(icon(1295, cy, 42))
        el += chip(lbl, T_STEP, 1352, ylbl, anchor="start")
        el += block(lines, T_C34, X(1352), y0, 19)

    body = "\n  ".join(x for x in el if x)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{DOC_W}mm" height="{DOC_H}mm"
     viewBox="0 0 {DOC_W} {DOC_H}" version="1.1">
  <title>EverHaar - Guide d'utilisation</title>
  <!--
    GUIDE UTILISATION - depliant accordeon 4 volets
    Format deplie  : {TRIM_W:.0f} x {TRIM_H:.0f} mm
    Format plie    : {TRIM_W/4:.0f} x {TRIM_H:.0f} mm (4 volets)
    Fond perdu     : {BLEED:.0f} mm par cote
    Fichier total  : {DOC_W:.0f} x {DOC_H:.0f} mm
    Pliage         : accordeon, 3 plis (pointilles sur le fichier)
    Texte converti en courbes - aucune police requise.
    ZONE PHOTO volet 2 : a remplacer par la photo produit.
  -->
  {body}
</svg>
'''


if __name__ == "__main__":
    p = "/home/user/macbook/print-cards/guide-depliant-shampooing.svg"
    open(p, "w", encoding="utf-8").write(build())
    print(f"guide-depliant-shampooing.svg -> {os.path.getsize(p)/1024:.1f} Ko")
