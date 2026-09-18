# -*- coding: utf-8 -*-
"""
Genere les deux pieces manquantes pour la FTA :
  01_Declaration_Letter  -> declaration de revenus et d'actifs, signee/tamponnee
  02_Trial_Balance       -> balance generale au 31/01/2025 (absente du rapport d'audit)

Les etats financiers audites (Axis Auditing) sont deja disponibles et sont
joints tels quels : on ne les reproduit pas, on s'y conforme.
"""
import os, subprocess, sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.worksheet.page import PageMargins

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import (COMPANY, SIGNATORY, LIQUIDATOR, LETTER_DATE, TAX_PERIOD,
                    RESIDUAL_PERIOD, FIGURES, TRIAL_BALANCE, BANK_ACCOUNTS)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

AED = lambda n: "{:,.2f}".format(n) if n else "-"


def _p(doc, text="", size=9.5, bold=False, align=None, space_after=4, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    if align is not None:
        p.alignment = align
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = "Calibri"
    return p


# ------------------------------------------------------------------ letter
def build_letter():
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(9.5)
    for s in doc.sections:
        s.top_margin = Cm(1.2); s.bottom_margin = Cm(1.0)
        s.left_margin = Cm(2.0); s.right_margin = Cm(2.0)

    C = WD_ALIGN_PARAGRAPH.CENTER
    J = WD_ALIGN_PARAGRAPH.JUSTIFY

    # --- letterhead (supprimer ce bloc si impression sur papier a en-tete)
    _p(doc, COMPANY["name"], size=13, bold=True, align=C, space_after=1)
    _p(doc, ", ".join(COMPANY["address_lines"]), size=8.5, align=C, space_after=1)
    _p(doc, "Registration No. %s  |  Trade Licence No. %s  |  Corporate Tax Registration No. %s"
       % (COMPANY["registration_no"], COMPANY["licence_no"], COMPANY["ct_reference"]),
       size=8.5, align=C, space_after=8)

    _p(doc, LETTER_DATE, size=9.5, space_after=6)
    _p(doc, "Federal Tax Authority", bold=True, space_after=0)
    _p(doc, "United Arab Emirates", space_after=8)

    _p(doc, "Subject: Declaration of Revenue and Assets for all Tax Periods - "
            "Corporate Tax De-Registration (TRN %s)" % COMPANY["ct_reference"],
       bold=True, space_after=8)

    _p(doc, "Dear Sir / Madam,", space_after=6)

    _p(doc,
       "We refer to your requests for additional information dated 30 April 2025, "
       "13 February 2026 and 9 September 2026 in connection with the above "
       "de-registration application. We hereby declare the following, which is "
       "supported by the audited financial statements and the official documents "
       "enclosed with this letter.",
       align=J, space_after=8)

    # --- 1. identification
    _p(doc, "1.  The Company", bold=True, space_after=3)
    _p(doc,
       "%s was registered in Dubai Silicon Oasis on %s under Registration No. %s, "
       "Trade Licence No. %s, as a Free Zone Company with limited liability. Its "
       "licensed activity was %s. The Company is wholly owned and was managed by "
       "%s, a %s national. The Company is %s."
       % (COMPANY["name"], COMPANY["incorporation_date"], COMPANY["registration_no"],
          COMPANY["licence_no"], COMPANY["activity"], SIGNATORY["name"],
          SIGNATORY["nationality"], COMPANY["vat_status"].lower()),
       align=J, space_after=8)

    # --- 2. tax periods
    _p(doc, "2.  Tax Periods Concerned", bold=True, space_after=3)
    _p(doc,
       "The Company had a single Tax Period, running from %s (date of registration) "
       "to %s (effective date of liquidation). The Company was placed into "
       "liquidation by a resolution of the shareholder passed on %s. Its trade "
       "licence was subsequently cancelled by %s on %s. No Tax Period exists "
       "after that date."
       % (TAX_PERIOD["start"], TAX_PERIOD["end"], COMPANY["liquidation_resolution_date"],
          COMPANY["licence_authority"], COMPANY["cancellation_letter_date"]),
       align=J, space_after=6)

    # --- 3. declaration table
    _p(doc, "3.  Declaration of Revenue and Assets", bold=True, space_after=3)

    rows = [
        ("Tax Period", "Revenue (AED)", "Total Assets (AED)", "Total Liabilities (AED)"),
        ("%s to %s" % (TAX_PERIOD["start"], TAX_PERIOD["end"]),
         "NIL (0.00)", "NIL (0.00)", "NIL (0.00)"),
        ("%s to %s" % (RESIDUAL_PERIOD["start"], RESIDUAL_PERIOD["end"]),
         "NIL (0.00)", "NIL (0.00)", "NIL (0.00)"),
    ]
    t = doc.add_table(rows=len(rows), cols=4)
    t.style = "Table Grid"
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = t.cell(i, j)
            cell.text = ""
            par = cell.paragraphs[0]
            par.paragraph_format.space_after = Pt(1)
            par.paragraph_format.space_before = Pt(1)
            if j > 0:
                par.alignment = C
            run = par.add_run(val)
            run.font.size = Pt(8.5)
            run.font.bold = (i == 0)
            run.font.name = "Calibri"
    _p(doc, "", size=4, space_after=2)

    _p(doc,
       "The Company earned NIL revenue and held NIL assets throughout its entire "
       "existence. It never commenced commercial operations. The only charges "
       "recorded were administration expenses of AED %s, consisting solely of legal "
       "and professional fees, which were borne by the shareholder in his personal "
       "capacity and are reflected in the shareholder's current account. As at the "
       "date of liquidation the Company had no assets and no liabilities."
       % AED(FIGURES["admin_expenses"]),
       align=J, space_after=8)

    # --- 4. statement of facts
    _p(doc, "4.  Supporting Facts", bold=True, space_after=3)
    facts = [
        "The Company never traded and generated no revenue in any Tax Period.",
        "The Company held no fixed assets, no inventory and no receivables at any time.",
        "The two bank accounts held with %s (%s, AED, and %s, EUR) were closed on %s "
        "and carried no balance at closure."
        % (BANK_ACCOUNTS[0]["bank"], BANK_ACCOUNTS[0]["number"],
           BANK_ACCOUNTS[1]["number"], BANK_ACCOUNTS[0]["closed"]),
        "All employee dues were settled and no claims remain from any employee.",
        "All creditors were settled and no claims were received from any creditor.",
        "The issued share capital of AED %s was fully accounted for; total equity at "
        "the close of liquidation was NIL." % AED(FIGURES["share_capital"]),
        "The liquidation was carried out by %s (%s, Registration No. %s), whose "
        "Liquidator's Report dated %s confirms that the liquidation proceedings are "
        "closed." % (LIQUIDATOR["firm"], LIQUIDATOR["partner"],
                     LIQUIDATOR["registration_no"], LIQUIDATOR["report_date"]),
        "The trade licence was officially cancelled by %s on %s; the cancellation "
        "notice may be verified at %s."
        % (COMPANY["licence_authority"], COMPANY["cancellation_letter_date"],
           COMPANY["cancellation_verify_url"]),
        "Between %s and %s the Company was already in liquidation, held no assets, "
        "operated no bank account and carried out no activity whatsoever."
        % (RESIDUAL_PERIOD["start"], RESIDUAL_PERIOD["end"]),
    ]
    for f in facts:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.left_indent = Cm(0.7)
        r = p.add_run(f)
        r.font.size = Pt(9)
        r.font.name = "Calibri"
    _p(doc, "", size=4, space_after=2)

    # --- 5. enclosures
    _p(doc, "5.  Documents Enclosed", bold=True, space_after=3)
    encl = [
        "Notice of Termination / Cancellation of Company issued by Dubai Silicon "
        "Oasis dated %s (official cancellation of the trade licence)."
        % COMPANY["cancellation_letter_date"],
        "Liquidator's Report and audited Financial Statements for the period from "
        "%s to %s, comprising the Statement of Financial Position, the Statement of "
        "Comprehensive Income, the Statement of Changes in Equity, the Statement of "
        "Cash Flows and the Notes, signed and stamped."
        % (TAX_PERIOD["start"], TAX_PERIOD["end"]),
        "Trial Balance as at %s, signed and stamped." % TAX_PERIOD["end"],
        "Trade Licence No. %s issued by %s." % (COMPANY["licence_no"], COMPANY["licence_authority"]),
        "This Declaration Letter, signed and stamped.",
    ]
    for i, e in enumerate(encl, 1):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.left_indent = Cm(0.7)
        r = p.add_run("(%d)  %s" % (i, e))
        r.font.size = Pt(9)
        r.font.name = "Calibri"
    _p(doc, "", size=4, space_after=4)

    # --- 6. request
    _p(doc, "6.  Request", bold=True, space_after=3)
    _p(doc,
       "The Company has ceased its business, has been liquidated and its trade "
       "licence has been officially cancelled. We therefore respectfully request "
       "the Authority to approve the de-registration of the Company from Corporate "
       "Tax pursuant to Article 52 of Federal Decree-Law No. 47 of 2022.",
       align=J, space_after=6)

    _p(doc,
       "I confirm that the information given in this letter is true, correct and "
       "complete, and that it is consistent in all respects with the audited "
       "financial statements enclosed.",
       align=J, space_after=10)

    _p(doc, "Yours faithfully,", space_after=26)
    _p(doc, "_______________________________", space_after=2)
    _p(doc, SIGNATORY["name"], bold=True, space_after=0)
    _p(doc, SIGNATORY["title"], space_after=0)
    _p(doc, COMPANY["name"], space_after=0)
    _p(doc, "Email: %s  |  Mobile: %s" % (SIGNATORY["email"], SIGNATORY["phone"]),
       size=8.5, space_after=6)
    _p(doc, "(Company stamp)", size=8.5, italic=True, space_after=0)

    path = os.path.join(OUT, "01_Declaration_Letter_FTA_%s.docx" % COMPANY["ct_reference"])
    doc.save(path)
    return path


# ------------------------------------------------------------ trial balance
def build_trial_balance():
    wb = Workbook()
    ws = wb.active
    ws.title = "Trial Balance"

    thin = Side(style="thin", color="000000")
    med = Side(style="medium", color="000000")
    box = Border(left=thin, right=thin, top=thin, bottom=thin)
    R = Alignment(horizontal="right")
    Cn = Alignment(horizontal="center", vertical="center")

    ws.column_dimensions["A"].width = 52
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 16

    def put(cell, val, size=10, bold=False, align=None, border=None, fmt=None):
        c = ws[cell]
        c.value = val
        c.font = Font(name="Calibri", size=size, bold=bold)
        if align is not None:
            c.alignment = align
        if border is not None:
            c.border = border
        if fmt:
            c.number_format = fmt
        return c

    ws.merge_cells("A1:C1"); put("A1", COMPANY["name"], size=13, bold=True, align=Cn)
    ws.merge_cells("A2:C2"); put("A2", ", ".join(COMPANY["address_lines"]), size=9, align=Cn)
    ws.merge_cells("A3:C3")
    put("A3", "Trade Licence No. %s  |  Corporate Tax Registration No. %s"
        % (COMPANY["licence_no"], COMPANY["ct_reference"]), size=9, align=Cn)
    ws.merge_cells("A5:C5"); put("A5", "TRIAL BALANCE", size=12, bold=True, align=Cn)
    ws.merge_cells("A6:C6")
    put("A6", "As at %s  (period from %s to %s)"
        % (TAX_PERIOD["end"], TAX_PERIOD["start"], TAX_PERIOD["end"]), size=9.5, align=Cn)
    ws.merge_cells("A7:C7"); put("A7", "All amounts in UAE Dirhams (AED)", size=9, align=Cn)

    r = 9
    for col, lbl in (("A", "Account"), ("B", "Debit"), ("C", "Credit")):
        c = put("%s%d" % (col, r), lbl, bold=True, border=box,
                align=Cn if col == "A" else R)
        c.border = Border(left=thin, right=thin, top=med, bottom=med)

    tot_d = tot_c = 0
    for name, d, c in TRIAL_BALANCE:
        r += 1
        put("A%d" % r, name, border=box)
        put("B%d" % r, d if d else None, align=R, border=box, fmt="#,##0.00")
        put("C%d" % r, c if c else None, align=R, border=box, fmt="#,##0.00")
        tot_d += d; tot_c += c

    r += 1
    put("A%d" % r, "TOTAL", bold=True).border = Border(left=thin, right=thin, top=med, bottom=med)
    for col, v in (("B", tot_d), ("C", tot_c)):
        cc = put("%s%d" % (col, r), v, bold=True, align=R, fmt="#,##0.00")
        cc.border = Border(left=thin, right=thin, top=med, bottom=med)

    r += 2
    ws.merge_cells("A%d:C%d" % (r, r))
    put("A%d" % r,
        "Note: the Company earned NIL revenue and held NIL assets during the period. "
        "Administration expenses represent legal and professional fees borne by the "
        "shareholder in his personal capacity.", size=8.5)
    ws.row_dimensions[r].height = 26
    ws["A%d" % r].alignment = Alignment(wrap_text=True, vertical="top")

    r += 2
    ws.merge_cells("A%d:C%d" % (r, r))
    put("A%d" % r,
        "This trial balance agrees with the audited financial statements for the "
        "period from %s to %s signed on %s."
        % (TAX_PERIOD["start"], TAX_PERIOD["end"], LIQUIDATOR["fs_signature_date"]), size=8.5)
    ws.row_dimensions[r].height = 26
    ws["A%d" % r].alignment = Alignment(wrap_text=True, vertical="top")

    r += 3
    put("A%d" % r, "_______________________________")
    r += 1; put("A%d" % r, SIGNATORY["name"], bold=True)
    r += 1; put("A%d" % r, SIGNATORY["title"])
    r += 1; put("A%d" % r, "Date: %s" % LETTER_DATE, size=9)
    r += 1; put("A%d" % r, "(Company stamp)", size=9)

    ws.page_setup.orientation = "portrait"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_margins = PageMargins(left=0.7, right=0.7, top=0.7, bottom=0.7)
    ws.sheet_view.showGridLines = False

    path = os.path.join(OUT, "02_Trial_Balance_%s.xlsx" % COMPANY["ct_reference"])
    wb.save(path)
    return path


# ------------------------------------------------------------------- pdf
def to_pdf(src):
    profile = os.path.join(HERE, ".lo_profile")
    subprocess.run(
        ["soffice", "--headless", "-env:UserInstallation=file://%s" % profile,
         "--convert-to", "pdf", "--outdir", OUT, src],
        check=True, capture_output=True, timeout=180)
    return os.path.splitext(src)[0] + ".pdf"


if __name__ == "__main__":
    for f in (build_letter(), build_trial_balance()):
        print("  built ", os.path.basename(f))
        print("  pdf   ", os.path.basename(to_pdf(f)))
