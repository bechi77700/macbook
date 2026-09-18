# Point bloquant : la déclaration CT de la période 13/02/2024 – 31/01/2025

## Le problème

La FTA n'approuve pas une radiation tant que **toutes les déclarations CT ont
été déposées** et que toutes les sommes dues (impôt + pénalités) sont réglées.
Répondre à la demande d'informations ne suffit donc pas : si la déclaration
finale n'a jamais été déposée, la radiation restera bloquée même avec un
dossier parfait.

**À vérifier immédiatement dans EmaraTax :**
Dashboard → Corporate Tax → onglet **Returns / Tax Returns**

Trois cas possibles :

| Ce que tu vois | Ce que ça veut dire |
|---|---|
| Période 13/02/2024–31/01/2025 avec statut *Submitted* / *Filed* | Rien à faire, tu es propre |
| Période 13/02/2024–31/01/2025 avec statut *Pending* / *Overdue* | **À déposer, pénalités en cours** |
| Période affichée différente (ex. année civile) | Signale-le-moi avant de soumettre quoi que ce soit |

## L'exposition chiffrée si elle n'est pas déposée

Échéance CT = 9 mois après la fin de la période fiscale.
Fin de période **31/01/2025** → échéance **31/10/2025**.

Barème des pénalités de dépôt tardif :
- 500 AED par mois (ou fraction de mois) pendant les 12 premiers mois
- 1 000 AED par mois à partir du 13e mois

| Date | Mois de retard | Pénalité cumulée estimée |
|---|---|---|
| Aujourd'hui (18/09/2026) | 11 | ~5 500 AED |
| 31/10/2026 | 12 | ~6 000 AED |
| 31/12/2026 | 14 | ~8 000 AED |

Chiffres indicatifs calculés sur le barème public — le montant réel exigible
est celui affiché dans EmaraTax, onglet **Payments / Penalties**. Vérifie-le :
c'est aussi là que tu verras si une pénalité de radiation tardive
(1 000 AED/mois, plafond 10 000) a été émise.

**Chaque mois d'attente coûte 500 à 1 000 AED. C'est la seule horloge qui
tourne encore contre toi.**

## Comment remplir la déclaration

Périmètre : période **13/02/2024 → 31/01/2025**, revenus nil, perte de 6 260 AED.

| Champ | Réponse | Pourquoi |
|---|---|---|
| Tax Period | 13/02/2024 – 31/01/2025 | Doit correspondre aux états financiers audités |
| Qualifying Free Zone Person ? | **No** | Aucun bénéfice à 0 de revenu, et répondre Yes déclenche des obligations supplémentaires |
| Small Business Relief ? | **Yes** | Revenus < 3M AED. Simplifie radicalement la déclaration |
| Accounting basis | Accrual (conforme aux états financiers IFRS) | Cohérence avec le rapport d'audit |
| Revenue | 0 | Statement of Comprehensive Income |
| Expenses | 6 260 | Administration expenses, note 4 |
| Taxable income | 0 | Perte, pas de base imposable |
| Tax payable | 0 | |

> **Le piège QFZP.** Répondre « Yes » à Qualifying Free Zone Person déclenche
> les tests de revenus qualifiants et de substance, et expose à des questions
> supplémentaires. Avec 0 de revenu, le résultat fiscal est nul dans tous les
> cas de figure. Réponds **No**.

> **Sur le Small Business Relief.** Élire le SBR fait perdre le report du
> déficit fiscal. Sans importance ici : la société est liquidée, le déficit de
> 6 260 AED ne sera jamais utilisé. Le gain de simplicité l'emporte.

## Ordre d'exécution

1. **D'abord** : vérifier l'onglet Returns et l'onglet Payments/Penalties
   → me renvoyer les deux captures
2. **Ensuite** : déposer la déclaration si elle est en attente
3. **Puis** : répondre à la tâche Additional Information (dossier prêt)
4. **Enfin** : régler les pénalités si des montants sont dus

Les étapes 2 et 3 sont indépendantes — si la déclaration demande du temps, ne
retarde pas la réponse à la demande d'informations, elle a déjà 9 jours de
retard.
