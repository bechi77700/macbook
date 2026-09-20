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
