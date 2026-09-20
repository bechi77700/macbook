# AMAYA VISION — Notes DA & structure site (audit du 20/09/2026)

Source : https://amayavisionofficial.com — Shopify, thème **"Final Amaya by @agencemade"** basé sur **Horizon 3.0.0** (thème custom, `theme_store_id: null`). Langue FR, devise EUR, marché Europe.

---

## 1. Identité de marque

- **Nom** : AMAYA VISION. Positionnement : accessoires "street-luxe" accessibles — lunettes de soleil + bijoux (chaînes, bracelets, bagues, boucles).
- **Naming produit** : lunettes = **noms de villes/destinations en MAJUSCULES** (DUBAI, MONACO, IBIZA, SANTORINI, MYKONOS, MIAMI, LOS ANGELES, BROOKLYN, MELBOURNE, CASABLANCA, VENISE) + quelques noms "concept" (INVICTUS, VIPER, LEVONZE, CAVAYA). Bijoux = **descriptif technique en MAJUSCULES** : `TYPE + STYLE + – XXMM` (ex. `BRACELET ICED CUBAN – 8MM`, `CHAÎNE MIAMI CUBAN – 8MM`, `BAGUE CUBAN CLAW – 10MM`).
- **Naming des variantes lunettes** : couleurs poétiques 2 mots en anglais — *Ash Rose, Verdant Gilt, Sunlit Mocha, Azure Crest, Slate Gleam, Noir Alloy, Halo Alloy, Crystal Luxe, Golden Obsidian, Midnight Slate, Aegean Drift, Solar Ember, Eclipse Gold…* Toujours `Adjectif/Matière + Nuance`. **À respecter impérativement** pour tout nouveau produit lunettes.
- **Ton copy** : court, sensoriel, sans superlatifs criards. Ex. PDP : *« Une silhouette affirmée, des finitions soignées. Une paire qui s'impose sans effort, du plein soleil aux soirées qui s'étirent. »* / *« Pensés pour durer. Créés pour être portés. »* / *« Chez Amaya, nous ne créons pas des bijoux pour les vitrines mais pour la vraie vie. »*

## 2. Système visuel (DA)

| Élément | Valeur |
|---|---|
| Fond | `#FFFFFF` pur |
| Texte | `#050505` (quasi-noir) |
| Bouton primaire | fond `#000000`, texte `#FFFFFF` |
| **Border-radius** | **0px partout** (boutons, inputs, cartes) — angles vifs, aucun arrondi |
| Police titres | **Inter**, `700`, **UPPERCASE**, h1 = 24px / line-height 24px |
| Police corps | **Figtree**, `400`, 14px, line-height 22.4px |
| Police accent | *Covered By Your Grace* (cursive, usage très ponctuel) |
| Police section avis | Josefin Sans (section app) |
| Gris secondaires | `#9a9a9a` (labels), `#666`/`#6b6b6b` (texte secondaire), `#ececec` (filets) |
| Accents | `#DAF3FE` (badge bleu pâle "OFFRE D'ÉTÉ"), `#00b67a` (étoiles style Trustpilot), `#c0392b` (urgence "Stock limité"), `#DBF9E6`/`#289668` (vert succès) |
| CTA | pleine largeur, `padding: 16px 32px`, uppercase, Figtree 14px |

**Résumé DA** : monochrome noir/blanc, typo Inter uppercase + Figtree, zéro arrondi, zéro ombre lourde, photo plein cadre. Minimaliste "premium accessible". Les seules couleurs sont fonctionnelles (badge promo, urgence, avis).

## 3. Structure du site

**Annonce (barre haute, 2 messages en rotation)**
- `LIVRAISON GRATUITE DANS TOUTE L'EUROPE`
- `1 ACHETÉ, 1 OFFERT SUR TOUT LE SITE`

**Nav header** : ACCUEIL · BIJOUX · LUNETTES DE SOLEIL · COLLECTIONS (méga-menu : BIJOUX / COLLIERS / BRACELETS / BOUCLES D'OREILLES / BAGUES / MEILLEURES VENTES / LUNETTES DE SOLEIL) · AIDE & CONTACT (Contact, Questions fréquentes, VISION, SUIVRE MA COMMANDE) · sélecteur région/devise · recherche · compte · panier.

**Homepage (ordre des sections)**
1. `ss_hero_33` — hero plein écran, copy minimal : **« ÉTÉ 2026 »** + CTA `DÉCOUVRIR`
2. `hero` — 2e hero
3. `collection_list` — titre **« NOS COLLECTIONS »** (h3) : BRACELETS / COLLIERS / LUNETTES DE SOLEIL / BAGUES / BOUCLES D'OREILLES
4. `ss_media_grid_2` — grille média avec CTA `VOIR NOS BIJOUX` / `VOIR NOS LUNETTES`
5. `section` (bandeau)
6. `ss_scrolling_images` — bande d'images défilantes
7. `ss_footer_6`

**Footer** : colonnes COLLECTIONS / AIDE & LEGAL (Questions fréquentes, Politique de confidentialité, Politique de remboursement, CGV) / COMPTE (Accueil, Mes commandes, Contact, Profile) / **REJOIGNEZ-NOUS** + newsletter (« Inscrivez-vous pour recevoir des offres exclusives, des informations sur les événements et bien plus encore. »).

## 4. Anatomie d'une page produit (référence : `/products/dubai`)

Ordre des sections :
1. `main` (galerie + colonne achat)
2. `custom_liquid` — bloc **description + caractéristiques** (lunettes ; sur bijoux ce bloc est placé après la section marque)
3. `ss_testimonial_28` — **NOS AVIS CLIENTS** (carrousel Swiper, avis en dur dans la section)
4. `section` — bandeau marque
5. `product_recommendations`
6. `product_list`
7. footer group

**Colonne achat, de haut en bas :**
1. Bloc `.amaya-pdp-timer` (custom liquid) : badge `OFFRE D'ÉTÉ` (fond `#DAF3FE`, 11px/800, radius 6px) + `1 acheté = 1 offert — jusqu'à épuisement des stocks` + à droite `⚠ Stock limité` en rouge `#c0392b`. Filets 1px `#eee` haut/bas.
2. `<h1>` titre produit, Inter 700 uppercase 24px
3. Bloc `.av-trustpilot` : 5 étoiles vertes `#00b67a` + **4.8/5** + `+12.567 clients` (lunettes) / `+1.247 clients` (bijoux) → ancre vers `#avis-clients`
4. Prix : `Prix promotionnel` + `Prix régulier` barré
5. Guide des tailles (bijoux uniquement : tableau pouces/cm, 6"→15 cm … 9"→23 cm)
6. Sélecteur `Couleur` (lunettes) / `Taille` (bijoux)
7. Quantité + CTA noir `AJOUTER AU PANIER` (état `Ajouté`)
8. Moyens de paiement
9. Badge `Viral sur TikTok` (bijoux)
10. Bloc offre : `1 ACHETÉ, 1 OFFERT` / `AJOUTEZ AU MOINS 2 ARTICLES. RÉDUCTION AUTOMATIQUE AU PANIER.` / *L'article le moins cher est offert pour deux articles ajoutés au panier.*
11. Accordéons : **Notre Garantie** (12 mois, remplacement unique gratuit, exclusions) · **EMBALLAGE** (étui rigide + chiffon microfibre) · **Retours** (LIVRAISON gratuite 7-12 j ouvrés / RETOURS 14 jours non porté / **OFFRE 1 ACHETÉ = 1 OFFERT** avec les règles de remboursement)

**Bloc description/caractéristiques (`.amaya-info`, custom liquid)** — à répliquer tel quel :
- `p.lead` 15px `#1a1a1a` (accroche sensorielle) + `p` 14px `#666` (bénéfice technique)
- Label `CARACTÉRISTIQUES` : Inter 11px, 600, letter-spacing .16em, uppercase, `#9a9a9a`
- Liste `label / valeur` en flex space-between, bordure haute 1px `#1a1a1a`, séparateurs 1px `#ececec`, labels 11px gris uppercase, valeurs 13px `#111` weight 500.
- Specs lunettes : Protection `UV400 — 100% UVA / UVB` · Verres `Traités anti-reflets` · Monture `Acétate & métal, légère` · Charnières `Renforcées` · Genre `Mixte` · Inclus `Étui + chiffon microfibre`
- Specs bijoux (en prose) : Métal laiton · Placage rhodium · Pierres zircone cubique · mention mannequin/taille.

⚠️ **Le `body_html` Shopify est vide (`<p></p>`)** : toute la description vit dans le bloc *custom liquid* du **template produit**, pas dans la fiche produit.

## 5. Templates produit (point critique pour l'ajout d'un produit)

| Catégorie | Template (section group id) |
|---|---|
| **Toutes les lunettes** | `template--28281349767543` — **un seul template partagé** |
| Bracelets | `template--27815989248375` |
| Colliers | `template--27815905853815` |
| Bagues | `template--27815989313911` |

→ **Ajouter une nouvelle lunette = elle hérite automatiquement du template** (description/specs génériques déjà en place). Ajouter un produit d'une nouvelle catégorie = il faut dupliquer un template et adapter le custom liquid.

## 6. Catalogue & pricing

- **Lunettes (40 réf.)** : 39,99 € ou 49,99 € — barré 59,99 € (parfois 69,99 €). 5 à 9 variantes couleur.
- **Bijoux (23 réf.)** : bracelets 29,99–79,99 € · bagues 39,99–49,99 € · boucles 39,99–59,99 € · chaînes 39,99–119,99 €. Barré 49,99–149,99 €.
- **Collections** : BIJOUX (23), LUNETTES DE SOLEIL (40), COLLIERS (8), BRACELETS (8), BOUCLES D'OREILLES (4), BAGUES (3), MEILLEURES VENTES / `frontpage` (10).
- **Grille de prix implicite** : prix psychologique en `X9,99`, remise affichée ~30-40 %, offre BOGO site-wide par-dessus.

## 7. Stack technique

- Thème custom Horizon 3.0.0 · sections app préfixées `ss_` (Section Store) : hero 33, media grid 2, testimonial 28, scrolling images, footer 6.
- **MoonBundle** (app extension) = moteur de l'offre *1 acheté = 1 offert*.
- **Microsoft Clarity** (heatmaps/replays).
- Avis clients **en dur** dans la section testimonial (pas de Judge.me/Loox/Yotpo). Ton des avis : très parlé, fautes assumées, mix lunettes/bijoux, signés `Prénom + Initiale.` + tag `Vérifié`.
- Pages live : `/pages/contact`, policies. Pas de `/pages/faq` ni `/pages/suivi-de-commande` (liens du menu potentiellement cassés → à vérifier).
- Images : mix **exports Canva** (`Untitleddesign-2025-…jpg`), **visuels générés Higgsfield** (`hf_2026…jpg/png`), **packshots fournisseur** (`ys-8mm-iocb-wg7-1.jpg`) et `mockup.jpg`.

## 8. Checklist pour ajouter un produit (à valider avec les visuels)

1. Titre en MAJUSCULES selon la convention de sa catégorie.
2. Variantes nommées selon la nomenclature couleur 2 mots (lunettes) ou tailles pouces (bijoux).
3. Prix en `X9,99` + `compare_at_price` cohérent (~ -30/-40 %).
4. `body_html` vide — la description passe par le custom liquid du template.
5. Assigner le bon template (lunettes = template existant, sinon dupliquer).
6. Ajouter aux bonnes collections (catégorie + éventuellement MEILLEURES VENTES).
7. 8-10 visuels : 1 packshot fond neutre, lifestyle, détail, mockup packaging.
8. Vérifier que le bloc `.amaya-pdp-timer`, `.av-trustpilot` et les accordéons s'affichent (ils viennent du template).

### Points d'attention repérés (à arbitrer)
- Certains handles ne correspondent plus au titre : `LOS ANGELES` → `/products/veloura`, `VIPER` → `/products/urban-halo`, `MIAMI` → `/products/nova-gaze`, `CASABLANCA` → `/products/crimson`, `VENISE` → `/products/imperial-eclipse`, `MELBOURNE` → `/products/lunettes-de-soleil-vintage`, et **`CHAÎNE TENNIS – 5MM – OR BLANC` a le handle `test`**.
- Des variantes sans SKU (ex. DUBAI : Azure Crest, Noir Alloy).
- Les avis affichés sur une PDP lunettes parlent de bracelets/chaînes (carrousel global non filtré par catégorie).
- Incohérence de délais : PDP lunettes annonce **7-12 j ouvrés**, PDP bijoux **5-8 j ouvrés**.

---

# ADDENDUM — DA visuelle (captures desktop du 20/09/2026)

> Site conçu **mobile-first** (confirmé par le client) : le desktop rend moins bien, les décisions de DA se lisent sur mobile.

## Direction photo (le vrai ADN)

**3 registres visuels qui cohabitent :**

1. **Lifestyle street / "cité" — le registre dominant et le plus fort.**
   Modèles hommes 18-30 ans, majoritairement noirs et métis, quelques blancs. Tenues : t-shirt blanc, hoodie noir, polo noir, doudoune. Décors : barre d'immeuble ensoleillée, escaliers béton, voiture (volant Chevrolet), rue de nuit avec néons, bord de mer. **Lumière naturelle dure, soleil franc, ombres marquées.** Aucun studio blanc, aucune pose catalogue. Cadrage souvent serré (cou, torse, mains) pour que le produit domine.
2. **Packshot produit** — deux sous-styles qui ne se parlent pas :
   - bijoux → macro sur fond noir ou sur peau/vêtement noir ;
   - lunettes → packshot sur **fond blanc pur** (visible dans les grilles produits, ça casse la continuité visuelle des rangées de cartes).
3. **Créa promo 3D "chrome"** — le 2e hero : produits en lévitation sur fond dégradé bleu-violet, reflets miroir, typo chromée biseautée `WELCOME SUMMER / 1 ACHETÉ = 1 OFFERT / SUR TOUT LE SITE`. Registre publicitaire assumé, en rupture totale avec le minimalisme du reste.

**Packaging** : boîtes noires mates rigides floquées `AMAYA` en blanc, shootées en pile sur fond blanc. C'est le visuel n°4/5 de la galerie lunettes.

## Éléments d'UI vus sur les captures (à ajouter au modèle PDP)

- **Barre de stock** sous le prix : `Plus que 5 en stock` (rouge) ← barre de progression rouge → `Forte demande` (gris, à droite). Présente sur lunettes ET bijoux.
- **Sélecteur couleur lunettes** : vignettes packshot carrées (pas des pastilles) + nom de la couleur sous chaque vignette.
- **Sélecteur taille bijoux** : boutons carrés `18 / 20 / 22`, actif = fond noir texte blanc.
- **Bijoux** : bouton `Acheter avec shop` (Shop Pay violet) sous le CTA noir — **absent des PDP lunettes**.
- **Bloc `VIRAL SUR TIKTOK`** (bijoux) : logo TikTok + carrousel 4 vignettes UGC verticales avec flèches.
- **Bandeau offre** : bloc noir pleine largeur, `1 ACHETÉ, 1 OFFERT*` (lunettes) / `1 BIJOU ACHETÉ, LE 2ÈME OFFERT*` (bijoux) en blanc bold centré + 2 lignes de conditions.
- **Section marque bas de page** : image lifestyle plein cadre à gauche + titre + texte à droite.
  - lunettes : `CONÇUES POUR LE SOLEIL. PENSÉES POUR LE STYLE.`
  - bijoux : `PENSÉS POUR DURER. CRÉÉS POUR ÊTRE PORTÉS.`
- **Avis clients** : cartes avec **vraie photo/vidéo UGC** (selfie piscine, voiture, ascenseur, main baguée ; certaines avec bouton play), texte, 5 étoiles vertes + `Vérifié`, prénom + initiale. Carrousel avec flèches `‹ ›`.
- **Cartes produit (grilles)** : image, badge pill `1 ACHETÉ = 1 OFFERT` en haut à droite (bleu pâle `#DAF3FE` ou blanc), titre uppercase, prix + prix barré.
- **Bandeau Instagram** : titre `RETROUVEZ NOUS ICI.` + `@amayavision.off`, puis bande d'images UGC défilante pleine largeur, fondu blanc sur les bords.
- **Footer** : fond noir, 4 colonnes, puis **wordmark `AMAYA` géant** en blanc, pleine largeur, bas de page.
- **Logo header** : wordmark `AMAYA` noir, bold, letter-spacing large, centré.

## Devise / marché

Les captures affichent des **prix en USD** ($58.00 barré $69.00 pour MYKONOS, $92.00 barré $114.00 pour la CHAÎNE CUBAN 14MM) avec sélecteur `USD`, **alors que la barre d'annonce dit `LIVRAISON GRATUITE DANS TOUTE L'EUROPE` et que tout le copy est en français.** Shopify Markets convertit, mais le message et la langue ne suivent pas.

## Règles pour les visuels d'un nouveau produit

1. Visuel 1 (vignette collection) : **lifestyle porté**, cadrage serré, lumière naturelle dure — pas de packshot blanc si le produit va côtoyer des cartes lifestyle.
2. 2-3 lifestyle portés, décor urbain/extérieur ensoleillé, modèle homme 18-30.
3. 1-2 macro produit sur fond sombre ou sur peau.
4. 1 visuel packaging boîte noire `AMAYA`.
5. 1 packshot détouré pour les vignettes de variantes.
6. Pas de fond studio gris, pas de mannequin souriant type stock photo, pas de flat-lay pastel.
