# -*- coding: utf-8 -*-
"""
Source unique de verite pour tous les documents generes.
MODIFIE CE FICHIER puis relance:  python3 build_docs.py
Tout ce qui est entre << >> est une valeur a confirmer.
"""

COMPANY = {
    "name": "ELIES ECOMMERCE & DIGITAL FZCO",
    "legal_form": "Free Zone Company (FZCO)",
    "address_lines": [
        "IFZA Properties, Dubai Silicon Oasis",
        "Dubai, United Arab Emirates",
    ],
    "free_zone": "DSO-IFZA, IFZA Properties, Dubai Silicon Oasis",
    "licence_no": "41532",
    "licence_authority": "DIEZ - Dubai Silicon Oasis",
    "ct_reference": "101001430723",
    "vat_status": "Not registered for Value Added Tax",
    "currency": "AED",
    # <<A CONFIRMER>>
    "incorporation_date": "<<DD Month YYYY>>",
    "cessation_date": "<<DD Month YYYY>>",
    # "cancelled" -> licence formellement annulee ; "expired" -> laissee expirer
    "licence_status": "expired",          # "expired" | "cancelled" | "cancellation_in_progress"
    "licence_status_date": "<<DD Month YYYY>>",
}

SIGNATORY = {
    "name": "<<NOM COMPLET>>",
    "title": "Manager / Authorised Signatory",
    "id_label": "Emirates ID / Passport No.",
    "id_value": "<<NUMERO>>",
    "email": "elies.bechahed@gmail.com",
    "phone": "<<+971 ...>>",
}

LETTER_DATE = "<<DD>> September 2026"

# Periodes fiscales CT. A ajuster APRES verification dans EmaraTax
# (onglet Corporate Tax > Tax Periods / Filings).
TAX_PERIODS = [
    {"label": "FY2024", "start": "1 January 2024",  "end": "31 December 2024"},
    {"label": "FY2025", "start": "1 January 2025",  "end": "31 December 2025"},
]

# Affirmations factuelles incluses dans la lettre.
# Passe a False celles que tu ne peux pas soutenir.
ASSERTIONS = {
    "no_bank_account_operated": True,   # aucun compte bancaire ouvert/utilise au nom de la societe
    "no_employees": True,               # aucun salarie, aucun visa emis
    "no_fixed_assets": True,            # aucune immobilisation
    "setup_costs_borne_by_shareholder": True,  # frais de licence/setup payes par l'actionnaire
}
