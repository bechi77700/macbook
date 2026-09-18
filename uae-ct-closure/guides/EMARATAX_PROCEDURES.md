# EmaraTax — navigation et mécanique d'upload

> Le **contenu** à soumettre (pièces jointes + texte des commentaires) est dans
> `emaratax/`. Ce guide ne couvre que le parcours dans le portail.
>
> Les points marqués `[VÉRIFIER]` sont ceux où l'interface peut différer de ce
> qui est décrit : le libellé exact des onglets EmaraTax change régulièrement.
> Si l'écran ne correspond pas, envoie-moi une capture.

---

## A — Répondre à « Additional Information pending »

### A.1 Navigation

1. Login sur `eservices.tax.gov.ae`
2. Sur le dashboard, section **Required Actions**, cliquer
   `Additional Information pending for 101001430723`
3. L'écran affiche l'historique des messages de l'officier FTA (30/04/2025,
   13/02/2026, 09/09/2026) et, en bas, une zone de réponse.
4. `[VÉRIFIER]` Le bouton d'entrée peut s'appeler *Respond*, *Provide
   Information* ou *Edit*. Il ouvre un formulaire avec une zone de texte
   libre et une zone d'upload.

### A.2 Avant d'uploader — la vérification qui compte

Ouvrir dans un autre onglet **Corporate Tax → Tax Periods** et noter les dates
exactes de la période enregistrée.

Elle doit être **13/02/2024 → 31/01/2025**.

Si le portail affiche autre chose (année civile, ou une seconde période après
le 31/01/2025), **arrêter ici** et me le signaler : la lettre de déclaration et
la balance générale doivent être réalignées avant soumission. Soumettre des
documents dont les périodes ne correspondent pas à celles du portail garantit
une quatrième relance.

### A.3 Upload

Les 5 pièces, dans l'ordre listé dans
`emaratax/01_Reponse_Additional_Information.md`.

Contraintes habituelles : PDF, < 5 Mo par fichier, noms sans accents ni
caractères spéciaux. Le rapport d'audit fait 9 pages et 2,6 Mo — il passe tel
quel. `[VÉRIFIER]` Si un plafond plus bas est imposé, compresser via un outil
de compression PDF plutôt que de scinder le rapport : il doit rester un seul
document cohérent.

Noms de fichiers suggérés :

```
1_Licence_Cancellation_DIEZ_28Feb2025.pdf
2_Audited_Financial_Statements_13Feb2024_31Jan2025.pdf
3_Trial_Balance_31Jan2025.pdf
4_Declaration_Letter_Revenue_Assets.pdf
5_Trade_Licence_41532.pdf
```

### A.4 Commentaire

Coller le bloc de texte de `emaratax/01_Reponse_Additional_Information.md`.

`[VÉRIFIER]` Si la zone de texte est limitée en caractères, garder les sections
ITEM (A), ITEM (B) et REQUEST, et supprimer le paragraphe SUMMARY OF THE
FIGURES — les chiffres figurent déjà dans la lettre de déclaration jointe.

### A.5 Avant Submit

- [ ] 5 fichiers visibles dans la liste des pièces jointes, chacun ouvrable
- [ ] Lettre et balance portent une signature manuscrite **et** un tampon
- [ ] Les dates de période du texte collé correspondent à celles du portail
- [ ] Aucune mention de « FY2024 » ou « FY2025 »

### A.6 Après Submit

Capturer :
- L'accusé de réception et son numéro de référence
- Le dashboard montrant que la Required Action a disparu ou est passée en
  *Submitted* / *Under Review*

Conserver ces captures : en cas de contestation de pénalité, elles datent la
soumission.

---

## B — Déclaration Corporate Tax

Couverte par `emaratax/02_Point_Bloquant_CT_Return.md`, qui détaille comment
savoir si elle est due, les pénalités en cours et les réponses champ par champ.

Navigation : **Corporate Tax → Returns** `[VÉRIFIER]` (parfois *Tax Returns*
ou *Filings*), puis *File Return* sur la ligne de la période
13/02/2024 – 31/01/2025.

Les deux réponses à ne pas rater :
- Qualifying Free Zone Person → **No**
- Small Business Relief → **Yes**

---

## C — Pénalités

**Payments** `[VÉRIFIER]` (ou *My Payments* / *Liabilities*) liste les montants
exigibles et leur motif. Deux lignes possibles :

- Dépôt tardif de la déclaration CT — 500 AED/mois les 12 premiers mois,
  1 000 AED/mois ensuite
- Demande de radiation tardive — 1 000 AED/mois, plafond 10 000 AED

La radiation ne sera pas approuvée tant que le solde n'est pas à zéro.
Capture cet écran et envoie-la-moi : le montant exact détermine s'il vaut la
peine de déposer une demande de remise (*penalty waiver / reconsideration*),
qui se justifie plus facilement quand la société n'a jamais eu d'activité.
