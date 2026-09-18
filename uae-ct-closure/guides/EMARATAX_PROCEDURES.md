# EmaraTax — deux procédures

> **Avertissement de fiabilité.** Les libellés exacts des boutons, onglets et champs
> d'EmaraTax changent régulièrement et je ne peux pas me connecter au portail pour
> vérifier. Ce qui est **certain** : la logique de la loi (ce qui doit être déclaré,
> ce qu'il ne faut surtout pas cocher, les seuils). Ce qui est **à confirmer à
> l'écran** : la navigation précise. Les points incertains sont marqués `[VÉRIFIER]`.

---

## PROCÉDURE A — Répondre à la tâche « Additional Information pending »

### A.0 — À faire AVANT de toucher à quoi que ce soit (5 min, prioritaire)

La demande FTA du 09/09/2026 affiche une échéance au 09/09/2026, soit une date déjà
passée. Deux cas :

- **La tâche est encore ouverte et actionnable** → tu réponds, tout va bien.
- **La fenêtre de réponse est fermée / la demande est expirée** → l'application de
  dé-registration a probablement été rejetée ou va l'être. Dans ce cas il faut
  **déposer une nouvelle demande de dé-registration** (mêmes pièces), pas essayer de
  ranimer l'ancienne. Ça change le plan, préviens-moi.

Vérifie aussi, dans le même passage :
- **Onglet des pénalités / « Payments » ou « My Payments »** : est-ce qu'une pénalité
  administrative a déjà été *assessed* (dé-registration tardive : 1 000 AED/mois,
  plafond 10 000) ? **Une pénalité impayée bloque l'approbation de la
  dé-registration.** Si elle existe, elle devra être payée — ou contestée par
  reconsideration, ce qui est un autre chantier.
- **La liste complète des périodes fiscales enregistrées** (2024 ? 2025 ? les deux ?).
  Screenshot. C'est ce qui détermine le contenu final de la declaration letter.

### A.1 — Navigation

1. `eservices.tax.gov.ae` (EmaraTax) → login UAE Pass ou email + mot de passe → OTP.
2. Écran « Taxable Person list » → sélectionne **ELIES ECOMMERCE & DIGITAL FZCO**
   (réf. 101001430723) → *View*.
3. Sur le dashboard du Taxable Person, la tâche apparaît soit dans un encart
   **« Action Required » / « Pending Actions »** en haut, soit dans la tuile
   **Corporate Tax → De-Registration → statut « Additional Information pending »**
   avec un bouton **Edit / Take Action / Provide Additional Information**. `[VÉRIFIER]`
4. Clic → tu es renvoyé dans le formulaire de dé-registration, à l'étape qui contient
   la zone de commentaire et la zone de pièces jointes.

### A.2 — Ce que tu joins

| # | Fichier | Obligatoire ? |
|---|---------|---------------|
| 1 | `01_Declaration_Letter_FTA_101001430723.pdf` — **signée + tamponnée + scannée** | Oui |
| 2 | Lettre d'annulation de licence DIEZ/IFZA (ou, à défaut, preuve d'expiration + preuve de la demande en cours : email envoyé, accusé de réception) | Oui — c'est le point dur |
| 3 | `02_Nil_Financial_Statements_101001430723.pdf` | Non, mais joins-le : ça ferme la porte à une 4ᵉ demande |
| 4 | Copie de la dernière licence commerciale | Recommandé |
| 5 | Copie passeport / Emirates ID du signataire | Recommandé |
| 6 | Accusé de dépôt du CT Return 2025 (screenshot ou PDF) | Oui, **si la procédure B est déjà faite** |

Nomme les fichiers en anglais, sans accents, sans espaces. PDF < 5 Mo chacun.
`[VÉRIFIER]` la limite de taille et les formats acceptés à l'écran.

### A.3 — Le commentaire à coller dans la zone de texte

```
Please find attached the documents requested in your notifications of 30 April 2025,
13 February 2026 and 9 September 2026:

1. A signed and stamped declaration of revenues and assets, covering every tax period
   of the Taxable Person and stating nil revenue, nil assets and no business activity
   throughout, together with the reason for de-registration (cessation of business and
   non-renewal / cancellation of trade licence no. 41532).
2. [Official licence cancellation letter issued by DIEZ - Dubai Silicon Oasis]
   OR
   [Evidence that trade licence no. 41532 expired on <<DATE>> and has not been renewed,
   together with the pending cancellation request submitted to the issuing authority on
   <<DATE>>. The official cancellation letter will be submitted as soon as it is issued.]
3. A full set of nil financial statements (statement of financial position, statement of
   profit or loss and trial balance) for each tax period, provided in support.
4. Confirmation that the Corporate Tax Return for the tax period 1 January 2025 to
   31 December 2025 has been filed on <<DATE>> with a nil tax position.

The company never commenced trading, generated no revenue and held no assets at any
time. Kindly proceed with the Corporate Tax de-registration.
```

### A.4 — Avant de cliquer Submit

- [ ] Toutes les périodes fiscales listées dans la lettre correspondent **exactement** à
      ce qu'affiche EmaraTax (c'est la cause n°1 d'une nouvelle demande d'info).
- [ ] La lettre porte une signature manuscrite **et** le tampon de la société.
- [ ] La date sur la lettre ≤ la date de soumission.
- [ ] Chaque pièce jointe s'ouvre correctement après upload (re-clique dessus).
- [ ] Le motif de dé-registration sélectionné dans le formulaire est bien
      *cessation of business / licence cancelled*, pas autre chose.

### A.5 — Preuves à screenshoter après Submit

1. L'écran de confirmation avec le **numéro de référence de la soumission**.
2. La liste des pièces jointes telle qu'affichée après validation.
3. Le nouveau statut de l'application (doit passer de *Additional Information pending*
   à *Submitted* / *Under review*).
4. L'email de confirmation FTA (garde-le, ne le supprime pas).

Archive tout dans un dossier daté. Si la FTA revient une 4ᵉ fois, ces preuves sont ton
seul levier pour une demande de *reconsideration* sur les pénalités.

---

## PROCÉDURE B — Déposer le Corporate Tax Return 2025 à zéro

**Deadline dure : 30/09/2026.** C'est la partie que tu contrôles à 100 %, elle ne
dépend d'aucun tiers. Fais-la en premier.

### B.1 — Navigation

1. Dashboard du Taxable Person → tuile **Corporate Tax** → *View*.
2. Onglet **Corporate Tax Returns** (ou « Returns ») → ligne
   **01/01/2025 – 31/12/2025**, statut *Open* → bouton **File** / **Submit Return**.
   `[VÉRIFIER]`

### B.2 — Les réponses, section par section

Le retour CT d'EmaraTax est découpé en sections successives. Les libellés peuvent
différer ; ce qui compte c'est la substance.

**1. Taxable Person details** — préremplis. Vérifie le nom, la licence 41532, la
référence 101001430723, la période fiscale. Ne corrige rien d'autre.

**2. Free Zone Person**
- « Are you a Free Zone Person? » → **Yes** (c'est une FZCO).
- **« Do you elect to be treated as a Qualifying Free Zone Person (QFZP)? » → NON.**
  ⚠️ **Piège principal.** Répondre *Yes* déclenche l'obligation de produire des
  **états financiers audités** et les tests de *de minimis* / *qualifying income*.
  Tu n'as aucun intérêt à ça : à revenu nul, le 0 % QFZP et le taux normal donnent
  exactement le même résultat, zéro. Réponds **No**.

**3. Elections**
- **Small Business Relief → Yes.** Conditions à confirmer dans le formulaire : revenu
  ≤ 3 M AED sur cette période **et sur toutes les périodes précédentes**, pas QFZP,
  pas membre d'un groupe multinational. Tu coches les trois.
  Effet : tu es traité comme n'ayant aucun revenu imposable, et le reste du formulaire
  se réduit fortement.
  *Note :* le SBR fait perdre le report des pertes fiscales. Sans objet ici : pas de
  pertes, la société n'a jamais rien dépensé en son nom.
  *Alternative :* ne pas élire le SBR et déclarer simplement 0 partout donne aussi un
  impôt de 0. Le SBR sert à raccourcir le formulaire, pas à réduire l'impôt.
- Realisation basis / autres élections → **No**.

**4. Accounting schedule / Financial information**
- Basis of accounting → **Cash basis** (autorisé sous 3 M AED de revenu).
- Revenue → **0**
- Accounting income / net profit → **0**
- Total assets → **0**
- « Are the financial statements audited? » → **No**.
- Si le portail exige de téléverser des états financiers ici : utilise
  `02_Nil_Financial_Statements_101001430723.pdf`. `[VÉRIFIER]` — normalement, avec le
  SBR élu, aucune pièce n'est exigée à ce stade.

**5. Adjustments, exempt income, reliefs, tax credits** — tout à **0** / **No**.
Pas de participation exemption, pas de foreign tax credit, pas de transferts de pertes,
pas de business restructuring relief.

**6. Related parties / Connected persons**
Rien à déclarer. Les seuils de disclosure ne sont pas atteints (aucune transaction).
De mémoire — à revérifier à l'écran si le portail insiste : les annexes ne se
déclenchent qu'au-delà d'agrégats de l'ordre de plusieurs dizaines de millions AED
pour les parties liées, et de quelques centaines de milliers pour les connected
persons. À zéro transaction, tu réponds **No** partout.

**7. Tax liability**
- Taxable income → **0**
- Corporate Tax payable → **0**
- Vérifie que la ligne finale affiche bien **AED 0.00**.

**8. Review & declaration**
- Coche la déclaration d'exactitude.
- Nom + qualité du déclarant.

### B.3 — Avant de cliquer Submit

- [ ] La période affichée est bien **01/01/2025 – 31/12/2025**.
- [ ] QFZP = **No**. Relis cette ligne deux fois.
- [ ] Net Corporate Tax Position = **0.00**.
- [ ] Aucune case « audited financial statements » cochée par erreur.
- [ ] Tu as téléchargé le **brouillon PDF** du retour avant soumission si le portail le
      propose.

### B.4 — Preuves à screenshoter après Submit

1. L'écran de confirmation + **numéro de référence du retour**.
2. Le statut de la ligne 2025 passé de *Open* à **Submitted / Filed**.
3. Le **Tax Return acknowledgement PDF** — télécharge-le, c'est la pièce que tu joindras
   dans la procédure A.
4. L'écran « Payments » montrant **0 AED dû** pour cette période.

### B.5 — Et la période 2024 ?

Si EmaraTax affiche **aussi** une période fiscale 2024 (01/01/2024 – 31/12/2024), son
retour était dû le **30/09/2025**. S'il n'a jamais été déposé, la pénalité de retard
court depuis octobre 2025 : 500 AED/mois les 12 premiers mois, soit de l'ordre de
**6 000 AED déjà accumulés**, et elle continue. Dans ce cas :

1. Dépose le retour 2024 **d'abord** (même contenu, tout à zéro, SBR élu), pour arrêter
   le compteur.
2. Puis le retour 2025.
3. Puis seulement la réponse à la demande d'information.

La dé-registration ne sera **pas** approuvée tant qu'un retour reste non déposé ou
qu'une pénalité reste impayée. C'est le point le plus coûteux du dossier s'il est réel
— c'est pour ça que la question des périodes enregistrées est la première à trancher.
