# -*- coding: utf-8 -*-
"""
Source unique de verite. Toutes les valeurs ci-dessous sont TIREES DES
DOCUMENTS OFFICIELS fournis (licence DIEZ, lettre d'annulation DIEZ,
Liquidator's Report & Financial Statements audites par Axis Auditing).
Ne rien inventer ici : tout doit pouvoir etre recoupe avec une piece jointe.

Relancer apres modification :  python3 build_docs.py
"""

COMPANY = {
    "name": "ELIES ECOMMERCE & DIGITAL - FZCO",
    "legal_form": "Free Zone Company (FZCO)",
    "registration_no": "DSO-FZCO-39398",
    "address_lines": [
        "Premises No. DSO-IFZA, IFZA Properties",
        "Dubai Silicon Oasis, Dubai, United Arab Emirates",
    ],
    "licence_no": "41532",
    "licence_authority": "Dubai Integrated Economic Zones Authority (DIEZ) - Dubai Silicon Oasis",
    "licence_issue_date": "13 February 2024",
    "licence_expiry_date": "12 February 2025",
    "activity": "Ecommerce",
    # ATTENTION : deux identifiants distincts.
    # TRN = numero d'enregistrement CT (15 chiffres), affiche dans le formulaire.
    # application_ref = reference du dossier de radiation, utilisee dans le
    # libelle de la tache "Additional Information pending for ...".
    "trn": "104552889800001",
    "application_ref": "101001430723",
    "vat_status": "Not registered for Value Added Tax",
    "currency": "AED",
    "incorporation_date": "13 February 2024",
    # Liquidation : resolution de l'actionnaire 30/01/2025, effet 31/01/2025
    "liquidation_resolution_date": "30 January 2025",
    "liquidation_effective_date": "31 January 2025",
    # Lettre d'annulation DIEZ
    "cancellation_letter_date": "28 February 2025",
    "cancellation_verify_url": "https://verify.diez.ae/yFkkaN",
    "licence_status": "cancelled",
    # Date de cessation telle que saisie dans le formulaire de radiation.
    "cessation_date": "28 February 2025",
}

SIGNATORY = {
    "name": "Elies Bechahed",
    "title": "Shareholder and Manager",
    "nationality": "French",
    "address": "Azizi Riviera 27, Apt 318, Nad Al Sheba 1, Dubai, United Arab Emirates",
    "email": "elies.bechahed@gmail.com",
    "phone": "+971 58 528 1013",
}

LIQUIDATOR = {
    "firm": "Axis Auditing & Accounting L.L.C",
    "partner": "Walid Aqil Mohammed Abdulla AlRafi",
    "registration_no": "1104, Dubai, U.A.E",
    "file_no": "AAA/15037/25",
    "report_date": "6 February 2025",
    "fs_signature_date": "4 February 2025",
}

LETTER_DATE = "18 September 2026"

# ---------------------------------------------------------------------------
# PERIODE FISCALE
# Exercice unique, du jour de l'immatriculation a la date d'effet de la
# liquidation. C'est la periode couverte par les etats financiers audites.
# La periode residuelle (01/02/2025 -> 28/02/2025, annulation de la licence)
# est couverte par une declaration de neant dans la lettre : la societe
# etait deja liquidee, sans actif ni compte bancaire.
# ---------------------------------------------------------------------------
# Le portail enregistre l'exercice fiscal en ANNEE CIVILE ("January - December").
# Les periodes fiscales CT sont donc celles-ci, et non la periode des etats
# financiers. Il faut declarer sur les deux bases pour eviter tout ecart.
CT_TAX_PERIODS = [
    {"label": "First tax period", "start": "13 February 2024", "end": "31 December 2024"},
    {"label": "Final tax period", "start": "1 January 2025",   "end": "28 February 2025"},
]

# Periode couverte par les etats financiers audites (base liquidation).
FS_PERIOD = {
    "start": "13 February 2024",
    "end": "31 January 2025",
}

# Entre la cloture des comptes et la cessation : aucune operation.
DORMANT_TAIL = {
    "start": "1 February 2025",
    "end": "28 February 2025",
}

# ---------------------------------------------------------------------------
# CHIFFRES AUDITES - periode du 13/02/2024 au 31/01/2025 (AED)
# Source : Statement of Financial Position (p.2) et Statement of
# Comprehensive Income (p.3) du rapport Axis Auditing.
# ---------------------------------------------------------------------------
FIGURES = {
    "revenue": 0,
    "admin_expenses": 6260,          # Legal and professional fees (note 4)
    "operating_loss": -6260,
    "total_assets": 0,
    "total_liabilities": 0,
    "share_capital": 10000,
    "retained_earnings": -6260,
    "shareholder_current_account": -3740,
    "total_equity": 0,
}

# Balance generale a etablir a la date de cloture (seul document reclame par
# la FTA qui ne figure pas dans le rapport d'audit).
TRIAL_BALANCE_DATE = "31 January 2025"
TRIAL_BALANCE = [
    # (compte, debit, credit)
    ("Share capital",                                        0,    10000),
    ("Shareholder's current account",                     3740,        0),
    ("Administration expenses - legal and professional fees", 6260,    0),
]

# Comptes bancaires (Liquidator's Report, point 5) - tous clotures.
BANK_ACCOUNTS = [
    {"bank": "Wio Bank P.J.S.C", "number": "9485724553", "currency": "AED",
     "closed": "29 January 2025"},
    {"bank": "Wio Bank P.J.S.C", "number": "9451723126", "currency": "EUR",
     "closed": "29 January 2025"},
]
