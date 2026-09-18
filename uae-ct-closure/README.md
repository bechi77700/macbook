# Clôture Corporate Tax — ELIES ECOMMERCE & DIGITAL - FZCO

Dossier de radiation CT auprès de la FTA. TRN **104552889800001**, réf. dossier
**101001430723**, licence DIEZ **41532**.

## État du dossier au 18/09/2026 (fin de journée)

Tout ce qui dépendait de nous est déposé. Le dossier attend la décision de
l'officier FTA.

| Obligation | Statut |
|---|---|
| Déclaration CT 13/02/2024 - 31/12/2024 | Déposée le 23/07/2025, position nette 0 |
| Déclaration CT 01/01/2025 - 31/12/2025 | Déposée le 18/09/2026, demande 230011618275, position nette 0 |
| Pénalités et montants dus | 0,00 AED - aucune pénalité émise |
| Demande de radiation + pièces | Soumise le 18/09/2026 |

Les trois conditions de l'article 52 sont réunies : déclarations à jour, solde
à zéro, licence annulée avec justificatif officiel.

Reste ouvert : la Required Action « Trade License Number 41532 » (échéance
12/02/2025), dont le libellé complet n'a pas encore été lu.

## Historique du diagnostic

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

Le « 30/09/2026 » du brief initial n'était pas une échéance de radiation : c'est
la date limite de dépôt de la déclaration CT 2025, déposée le 18/09/2026.

## Chiffres de référence

Le portail enregistre l'exercice en **année civile**, alors que les états
financiers audités sont arrêtés au 31/01/2025. Deux bases coexistent :

| Base | Périodes |
|---|---|
| Périodes fiscales CT (portail) | 13/02/2024 → 31/12/2024, puis 01/01/2025 → 31/12/2025 |
| États financiers audités | 13/02/2024 → 31/01/2025 |

Tout étant à zéro, la déclaration est identique sur les deux bases — la lettre
les couvre explicitement toutes les deux.

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
out/                                           (non versionné)
  01_Declaration_Letter_FTA_104552889800001.pdf  signé + tamponné
  02_Trial_Balance_104552889800001.pdf           signé + tamponné
emaratax/
  01_Reponse_Additional_Information.md         procédure de soumission complète
  02_Point_Bloquant_CT_Return.md               déclarations CT et pénalités
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

## Signature et tampon

`build_docs.py` incruste automatiquement `assets/signature_stamp.png`
(signature manuscrite + tampon de la société) dans la lettre et la balance.

**Ce fichier n'est volontairement pas versionné**, ni les documents générés
dans `out/` une fois signés : une signature et un tampon sont réutilisables
tels quels par quiconque y a accès, y compris extraits d'un PDF. Ils restent
en local. Si `assets/signature_stamp.png` est absent, les documents sont
générés avec un espace vide à signer à la main.
