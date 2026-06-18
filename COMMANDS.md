# 🤖 Revital RP Bot v4 — Référence des Commandes

## 🔐 VÉRIFICATION

| Commande | Description |
|----------|-------------|
| `/verify CODE` | Vérifier avec le code captcha reçu dans #verification |

Le captcha est envoyé automatiquement dans `#verification` à chaque nouveau membre.

---

## ⚠️ MODÉRATION

| Commande | Permission | Description |
|----------|-----------|-------------|
| `/warn @user raison [type]` | Staff | Ajouter un warn (Discord ou In-Game) |
| `/warns [@user]` | Tous | Voir les warns (10 derniers) |
| `/clearwarn @user N` | Admin | Supprimer le warn numéro N |
| `/clearallwarns @user` | Admin | Supprimer tous les warns |
| `/history @user` | Staff | Historique complet (warns + WL + mute actif) |
| `/mute @user durée [raison]` | Staff | Mute temporaire (`30m`, `1h`, `7d`...) |
| `/unmute @user` | Staff | Unmute immédiat |
| `/kick @user [raison]` | Admin | Expulser du serveur |
| `/ban @user [raison] [durée]` | Admin | Bannir (permanent ou temporaire) |
| `/bc #salon` | Staff | Envoyer un broadcast / annonce dans un salon |

### ⚡ Sanctions automatiques (AutoMod)

| Seuil | Sanction |
|-------|----------|
| 3 warns | Mute automatique (durée config) |
| 5 warns | Kick automatique |
| 7 warns | Ban automatique |

---

## ✅ WHITELIST

| Commande | Permission | Description |
|----------|-----------|-------------|
| `/whitelist @user` | Staff | Ouvre le formulaire en 2 étapes |
| `/check-wl [@user]` | Tous | Voir le statut whitelist actuel |
| `/wl-history @user` | Staff | Voir tout l'historique des WL d'un joueur |
| `/wl-revoke @user raison` | Admin | Révoquer la whitelist + retirer le rôle |

### Formulaire Whitelist (2 étapes)

**Étape 1 — Infos RP (Modal)**
- Nom & Prénom RP
- Âge du personnage
- Background (résumé)
- Notes staff (optionnel)

**Étape 2 — Évaluation (Sélecteurs)**
- Type : Légal / Illégal
- Background validé : ✅ OK / ❌ NON
- Règlement maîtrisé : ✅ OK / ❌ NON
- Décision : ✅ ACCEPTÉ / ❌ REFUSÉ / ⏳ EN ATTENTE

---

## 🎫 TICKETS

| Commande | Permission | Description |
|----------|-----------|-------------|
| `/setup-tickets` | Admin | Envoie le panneau de création dans le salon actuel |
| `/ticket-add @user` | Staff | Ajouter un membre au ticket actuel |
| `/ticket-close` | Tous | Fermer le ticket avec confirmation |

### Catégories disponibles

| Catégorie | Usage |
|-----------|-------|
| 💎 Boutique / Remboursement | Problème d'achat, remboursement, item manquant |
| ⚜️ Superviseur | Contacter un superviseur |
| 🔵 Recrutement Staff | Candidature ou question recrutement |
| 🟢 Dossier Légal | Affaire légale RP |
| 🔴 Dossier Illégal | Affaire criminelle / illégale RP |
| 💀 Wipe / Mort RP | Demande de wipe ou mort RP officielle |

### Panel dans chaque ticket (boutons)

| Bouton | Permission | Action |
|--------|-----------|--------|
| ✅ Claim | Staff | Se désigner comme responsable |
| 👤 Ajouter membre | Staff | Ajouter un membre via son ID |
| 🔄 Réassigner | Staff | Changer le responsable |
| 📋 Transcript | Staff | Télécharger l'historique HTML |
| 🔒 Fermer | Tous | Fermer (confirmation requise) |

### À la fermeture
- Transcript HTML généré automatiquement
- Log envoyé dans `#logs-tickets` avec le fichier joint
- Salon supprimé

---

## 📝 LOGS AUTOMATIQUES

| Salon | Contenu |
|-------|---------|
| `#logs-moderation` | Warns, mutes, kicks, bans, sanctions auto |
| `#logs-wl` | Toutes les décisions whitelist + révocations |
| `#logs-tickets` | Ouverture/fermeture + transcripts |

---

## 🔐 PERMISSIONS

| Niveau | Qui ? | Accès |
|--------|-------|-------|
| `Admin` | Administrateurs Discord | Tout |
| `Staff` | Admins + rôle `STAFF_ROLE` | Modération, tickets, WL |
| `Tous` | Tout le monde | Voir ses warns, check-wl, tickets |

---

## 💡 TIPS

✅ Configure `STAFF_ROLE` dans `config.py` pour donner l'accès staff sans donner l'admin
✅ Configure `TICKET_CATEGORY_ID` pour ranger les tickets dans une catégorie Discord
✅ Configure `TICKET_CHANNELS` pour des sous-catégories par type de ticket
✅ Les transcripts sont aussi sauvegardés dans `data/transcripts/`
✅ L'historique WL conserve **toutes** les entrées, même après révocation

---

**Bot v4 — Revital RP** 🎮
