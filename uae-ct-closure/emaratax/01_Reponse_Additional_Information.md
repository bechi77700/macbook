# Répondre à « Additional Information pending » — procédure exacte

Écran : **Corporate Tax De-Registration**, étape 1/2 (*De-Registration Details*).
Le formulaire est en mode édition, avec trois zones à traiter :
les **uploads**, la **note à l'officier**, et le champ **motif de cessation**.

---

## Trois écarts détectés dans le portail — à corriger avant d'envoyer

### 1. Deux identifiants distincts, à ne pas confondre

| | |
|---|---|
| **TRN** (enregistrement CT) | `104552889800001` |
| **Référence du dossier de radiation** | `101001430723` |

`101001430723` n'est **pas** le TRN — c'est la référence du dossier, celle qui
apparaît dans le libellé de la tâche. Les documents citent désormais les deux.

### 2. La période fiscale du portail contredit les états financiers

Le formulaire affiche **Tax Period : January – December**. Tes états financiers
audités couvrent **13/02/2024 → 31/01/2025**. Ce n'est pas la même base.

Périodes fiscales CT réelles, selon l'enregistrement du portail :

| Période | Du | Au |
|---|---|---|
| Première | 13/02/2024 (immatriculation) | 31/12/2024 |
| Finale | 01/01/2025 | 28/02/2025 (cessation) |

Le champ Tax Period est grisé, tu ne peux pas le modifier — et **il ne faut
pas essayer**. La lettre déclare donc sur **les deux bases** : tout est à zéro
dans tous les cas, donc aucune contradiction. C'est ce qui empêche l'officier
de relancer sur « vos périodes ne correspondent pas ».

### 3. Le motif de cessation ne répond pas à la question posée

Le champ contient aujourd'hui :
> *Opened a new business activity in Sharjah (Shams Freezone)*

La toute première question de l'officier, le **30/04/2025**, était précisément
*« Kindly clarify more the reason of CT De-Registration »*. Elle n'a jamais reçu
de vraie réponse : ouvrir une société à Sharjah explique ce que tu as fait
ensuite, pas pourquoi celle-ci a cessé. Ce champ est éditable — remplace-le par :

```
The Company never commenced commercial operations and generated no revenue
at any time. The shareholder resolved to wind it up on 30 January 2025;
liquidation took effect on 31 January 2025 and was completed by a licensed
liquidator, Axis Auditing & Accounting L.L.C (Registration No. 1104). The
trade licence was officially cancelled by Dubai Silicon Oasis on 28 February
2025. The shareholder subsequently established a separate entity in Shams
Free Zone, Sharjah, for his business activity.
```

On garde la mention de Sharjah : elle est déjà au dossier, la supprimer
créerait une incohérence.

---

## Uploads — attention, 3 fichiers maximum par zone

| Zone | Formats | Limite |
|---|---|---|
| **Upload Supporting Documents** | PDF, DOC, DOCX | 15 Mo/fichier — **3 fichiers max** |
| **Upload Financial Documents** (Optional) | DOC, DOCX, PDF, XLS, XLSX | 15 Mo/fichier — **3 fichiers max** |

La zone Supporting affiche déjà **Add/View(1)** : un fichier est présent.
**Ouvre-le avant d'ajouter quoi que ce soit** — s'il s'agit déjà de la lettre
d'annulation DIEZ, tu as une place de libre ; sinon il te reste deux places.

Répartition à viser :

**Supporting Documents**
1. *(fichier déjà présent — à identifier)*
2. `Licence_Cancellation_DIEZ_28Feb2025.pdf`
3. `Trade_Licence_41532.pdf`

**Financial Documents**
1. `Audited_Financial_Statements_13Feb2024_31Jan2025.pdf` *(9 p., 2,6 Mo — passe sans compression)*
2. `Trial_Balance_31Jan2025.pdf` *(signé + tamponné)*
3. `Declaration_Letter_Revenue_Assets.pdf` *(signé + tamponné)*

Si la zone Supporting est déjà pleine avec un fichier sans rapport, mets la
lettre d'annulation DIEZ en priorité absolue : c'est le point (a) de la
demande.

---

## La note à l'officier

`Officer Notes` → **View/Add notes** → zone *« Please share your notes with the
officer »* → bouton **Share Note**.

C'est un simple champ texte, séparé du formulaire. À coller :

```
Reference: TRN 104552889800001 - De-Registration Ref. 101001430723

Dear Officer,

Further to your notes of 30 April 2025, 13 February 2026 and 09 September
2026, all outstanding items have now been uploaded.

(a) OFFICIAL CANCELLATION OF THE TRADE LICENCE
Notice of Termination/Cancellation of Company issued by Dubai Silicon Oasis
on 28 February 2025 for licence 41532, confirming that all formalities are
complete and the company/licence has been de-registered and cancelled. It
can be verified with the issuing authority at https://verify.diez.ae/yFkkaN

(b) FINANCIAL STATEMENTS FOR ALL TAX PERIODS
- Liquidator's Report and audited Financial Statements for 13 February 2024
  to 31 January 2025, signed and stamped by Axis Auditing & Accounting
  L.L.C (Reg. No. 1104): Statement of Financial Position, Statement of
  Comprehensive Income, Statement of Changes in Equity, Statement of Cash
  Flows and Notes.
- Trial Balance as at 31 January 2025, signed and stamped.
- Declaration Letter of revenue and assets, signed and stamped, stating the
  tax periods.

DECLARED FIGURES (AED)
Tax period 13 Feb 2024 - 31 Dec 2024:  revenue NIL, assets NIL
Tax period 01 Jan 2025 - 28 Feb 2025:  revenue NIL, assets NIL
Audited period 13 Feb 2024 - 31 Jan 2025: revenue NIL, total assets NIL,
total liabilities NIL, total equity NIL, administration expenses AED 6,260
(legal and professional fees borne by the shareholder personally).

The Company's tax periods are registered on a January to December basis,
while the liquidation financial statements were drawn to 31 January 2025.
Revenue and assets were NIL under either basis. No transaction occurred
between 31 January 2025 and the cessation date of 28 February 2025.

REASON FOR DE-REGISTRATION
The Company never commenced operations and earned no revenue. It was
liquidated with effect from 31 January 2025 and its licence was cancelled
on 28 February 2025. Its two bank accounts with Wio Bank P.J.S.C were
closed on 29 January 2025. All employees' dues and all creditors were
settled, with no claims outstanding.

We request approval of the de-registration under Article 52 of Federal
Decree-Law No. 47 of 2022.

Elies Bechahed
Shareholder and Manager
```

Si le champ refuse le texte (limite de caractères), garde les blocs (a), (b)
et DECLARED FIGURES, et supprime REASON FOR DE-REGISTRATION — il est déjà
couvert par le champ *Detailed Reason for Cessation* et par la lettre jointe.

---

## Ordre d'exécution

1. Ouvrir le fichier déjà présent dans **Supporting Documents** pour savoir ce que c'est
2. Corriger le champ **Detailed Reason for Cessation**
3. Uploader les fichiers dans les deux zones
4. **View/Add notes** → coller la note → **Share Note**
5. **Next Step** → *Review and Declaration* → vérifier → soumettre
6. Capturer l'accusé de réception et son numéro de référence

> Ne clique pas **Save as Draft** en pensant avoir terminé : un brouillon
> n'est pas une soumission et l'échéance du 09/09/2026 est déjà dépassée
> de 9 jours.

## Checklist avant soumission

- [ ] Lettre de déclaration et balance générale **signées à la main et tamponnées**
- [ ] Motif de cessation remplacé
- [ ] Lettre d'annulation DIEZ bien présente dans les pièces
- [ ] Aucune mention de « FY2024 » ou « FY2025 » nulle part
- [ ] Le TRN cité est `104552889800001`, pas la référence du dossier
