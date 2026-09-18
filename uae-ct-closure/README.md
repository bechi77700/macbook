# Clôture fiscale — ELIES ECOMMERCE & DIGITAL FZCO

Dossier de dé-registration Corporate Tax (FTA ref. 101001430723, licence 41532).

## Contenu

| Fichier | Quoi |
|---|---|
| `config.py` | Toutes les données de la société, les périodes fiscales et les affirmations factuelles. **Le seul fichier à éditer.** |
| `build_docs.py` | Génère la lettre et les états financiers. `python3 build_docs.py` |
| `out/01_Declaration_Letter_FTA_101001430723.docx` / `.pdf` | Declaration letter pour la FTA, 1 page, à signer + tamponner |
| `out/02_Nil_Financial_Statements_101001430723.xlsx` / `.pdf` | États financiers nil, 1 page par période fiscale |
| `emails/01_DIEZ_demande_lettre_annulation.md` | Email à IFZA/DIEZ |
| `emails/02_DIEZ_relance_J3.md` | Relance à J+3 |
| `guides/EMARATAX_PROCEDURES.md` | Les deux procédures portail, pas à pas |
| `guides/PLAN_12_JOURS.md` | Plan daté 18 → 30 septembre |

## Régénérer les documents

```bash
pip install python-docx openpyxl
python3 build_docs.py    # produit .docx/.xlsx puis .pdf via LibreOffice
```

Les valeurs entre `<< >>` dans `config.py` sont des placeholders à remplir.
