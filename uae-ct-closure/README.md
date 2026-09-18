# Clôture Corporate Tax — ELIES ECOMMERCE & DIGITAL - FZCO

Dossier de radiation CT auprès de la FTA. Réf. CT **101001430723**, licence
DIEZ **41532**.

## État du dossier au 18/09/2026

La FTA réclame deux choses depuis le 30/04/2025, relancées le 13/02/2026 puis
le 09/09/2026. Les documents officiels de la société montrent que **presque
tout existait déjà** :

| Demande FTA | Statut |
|---|---|
| (a) Annulation officielle de la licence | ✅ Notice DIEZ du 28/02/2025, déjà en main |
| (b) Balance sheet + Profit and loss | ✅ Rapport d'audit Axis, déjà en main |
| (b) Trial Balance | ✅ Généré ici |
| (b) Declaration letter | ✅ Générée ici |

Le dossier n'était pas bloqué par une pièce manquante. Il était bloqué parce
que rien n'avait été uploadé.

## Chiffres de référence

Période fiscale unique : **13/02/2024 → 31/01/2025** (immatriculation →
date d'effet de la liquidation). **Ce n'est pas l'année civile.**

| Poste (AED) | |
|---|---|
| Revenus | 0 |
| Charges administratives | 6 260 |
| Total actifs | 0 |
| Total passifs | 0 |
| Capital social | 10 000 |
| Total capitaux propres | 0 |

Source : Liquidator's Report & Financial Statements, Axis Auditing &
Accounting LLC, signés le 04/02/2025.

## Contenu

```
out/
  01_Declaration_Letter_FTA_101001430723.pdf   à signer + tamponner
  02_Trial_Balance_101001430723.pdf            à signer + tamponner
emaratax/
  01_Reponse_Additional_Information.md         pièces + texte à coller
  02_Point_Bloquant_CT_Return.md               la déclaration CT et ses pénalités
guides/
  PLAN_ACTION.md                               séquence d'exécution
  EMARATAX_PROCEDURES.md                       navigation dans le portail
config.py / build_docs.py                      génération des documents
```

**Commencer par `guides/PLAN_ACTION.md`.**

## Documents sources (non versionnés)

Fournis séparément, à joindre tels quels à la soumission :
licence 41532, Notice of Cancellation DIEZ du 28/02/2025, Liquidator's Report
& Financial Statements (9 p.), MOA/AOA signé.

## Régénérer les documents

```bash
pip install python-docx openpyxl
python3 build_docs.py     # écrit .docx/.xlsx + .pdf dans out/
```

Toutes les valeurs sont dans `config.py`. Elles proviennent des documents
officiels — ne rien y saisir qui ne soit recoupable avec une pièce jointe :
la lettre de déclaration doit rester cohérente avec les états financiers
audités qu'elle accompagne.

La conversion PDF utilise LibreOffice headless (`libreoffice-writer`,
`libreoffice-calc`).
