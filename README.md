# 🤖 Revital RP Bot v3 - Documentation Complète

## ✨ Nouvelles Fonctionnalités v3

✅ **Slash Commands** - Utilise `/` pour toutes les commandes
✅ **Captcha automatique** - S'affiche dans le channel #verification au join
✅ **Formulaires Whitelist** - Interface interactive avec sélecteurs
✅ **Formulaires Warns** - Modal pour ajouter des warns
✅ **Tickets avancés** - 6 catégories avec renommage automatique
✅ **Logs détaillés** - Tous les actions enregistrées

---

## 🚀 Installation Rapide

```bash
# 1. Installe les dépendances
pip install -r requirements.txt

# 2. Configure config.py avec tes IDs

# 3. Lance le bot
python main.py
```

---

## 📋 Toutes les Commandes

### 🔐 Vérification

```
/verify CODE          → Vérifier avec le captcha
```

**Flux:**
1. Joueur rejoins → Captcha s'affiche dans #verification
2. Joueur tape `/verify CODE`
3. Reçoit le rôle "Verified" → Accès au serveur

### ⚠️ Warns

```
/warn @user           → Ajouter un warn (ouvre un formulaire)
/warns [@user]        → Voir les warns
```

**Interface:**
- Modale pour rentrer la raison
- Logs automatiquement dans #logs-moderation
- Total des warns affiché

### 🔇 Mute

```
/mute @user 1h Raison     → Mute temporaire
/unmute @user             → Unmute
```

### 👢 Kick & Ban

```
/kick @user Raison        → Kick
/ban @user Raison         → Ban
```

### ✅ Whitelist

```
/whitelist @user          → Ouvre le formulaire whitelist
/check-wl [@user]         → Vérifier le statut
```

**Formulaire Whitelist:**
- Joueur: Affiché automatiquement
- ID Discord: Auto-rempli
- Background: Sélecteur (OK / PAS OK)
- Règlement: Sélecteur (OK / PAS OK)
- Décision: Sélecteur (Accepté / Refusé)

**Logs:**
- Sauvegardé dans #logs-wl
- Inclut tous les détails + modérateur

### 🎫 Tickets

```
/setup-tickets            → Active le système (1 fois)
```

**Flux:**
1. Admin tape `/setup-tickets`
2. Apparaît un sélecteur de catégories
3. Joueur choisit une catégorie:
   - 🎮 Problème In-Game
   - 👨‍⚖️ Plainte Staff
   - 🛍️ Problème Boutique
   - 💻 Développement
   - 📋 Dossier Légal
   - ⚖️ Dossier Illégal
4. Channel créé: `[NomJoueur]-[categorie]`
5. Clique "Fermer le Ticket" pour supprimer

---

## ⚙️ Configuration

### 1. Créer les Rôles

```
- citoyen-wl
- Muted
- Verified
```

### 2. Créer les Channels

```
- #logs-moderation
- #logs-wl
- #tickets
- #verification
```

### 3. Récupérer les IDs

- **Mode Développeur**: Paramètres Discord → Avancé → Mode Développeur ✅
- **Copier les IDs**: Clic droit sur channels/rôles → "Copier l'ID"
- **Remplir config.py** avec les IDs

### 4. Ordre des Rôles

⚠️ **Important:** Le rôle du bot doit être PLUS HAUT que les autres!

```
1. @everyone
2. Revital RP Bot    ← ICI ou PLUS HAUT
3. citoyen-wl
4. Verified
5. Muted
```

### 5. Permissions sur Discord Developer Portal

1. OAuth2 → URL Generator
2. Scopes: `bot`
3. Permissions: `Administrator`
4. Copie l'URL et invite le bot

---

## 🎯 Workflows Détaillés

### Workflow Vérification

```
Joueur rejoint
    ↓
Bot envoie captcha dans #verification
    ↓
Joueur tape /verify CODE
    ↓
Code correct?
    ├─ OUI: Reçoit rôle "Verified" → Accès serveur
    └─ NON: Message d'erreur
```

### Workflow Whitelist

```
Admin tape /whitelist @joueur
    ↓
Formulaire s'ouvre:
  - Background: OK/PAS OK
  - Règlement: OK/PAS OK
  - Décision: Accepté/Refusé
    ↓
Admin clique "Soumettre"
    ↓
Si Accepté:
  ├─ Logs dans #logs-wl
  └─ Rôle "citoyen-wl" ajouté
```

### Workflow Tickets

```
Admin tape /setup-tickets
    ↓
Message apparaît avec sélecteur
    ↓
Joueur sélectionne une catégorie
    ↓
Channel créé: joueur-categorie
    ↓
Joueur peut utiliser le ticket
    ↓
Clique "Fermer le Ticket"
    ↓
Channel supprimé
```

---

## 📊 Structure des Données

```
data/
├── warns.json          # {user_id: [{reason, moderator, date, type}]}
├── mutes.json          # {user_id: {unmute_time, reason}}
├── whitelist.json      # {user_id: {discord_id, background, reglement, decision, date, moderator}}
├── tickets.json        # {channel_id: {creator, created, status, category}}
└── captchas.json       # {user_id: {code, created, attempts}}
```

---

## 🔧 Troubleshooting

### ❌ Le captcha ne s'affiche pas dans #verification

**Cause:** Channel ID incorrect ou bot n'a pas accès

**Solution:**
1. Vérifies VERIFICATION_CHANNEL dans config.py
2. Vérifies que le bot peut écrire dans le channel
3. Redémarre le bot

### ❌ Les formulaires ne s'ouvrent pas

**Cause:** discord.py version incompatible

**Solution:**
```bash
pip install --upgrade discord.py
```

### ❌ Les tickets ne se créent pas

**Cause:** Permissions insuffisantes

**Solution:**
1. Bot doit être Admin
2. Doit avoir permission "Manage Channels"
3. Le serveur doit permettre la création de channels

### ❌ "Slash commands not found"

**Solution:**
1. Redémarre Discord complètement
2. Attends 1 minute après lancement du bot
3. Teste avec `/help` ou `/ping`

---

## 💡 Tips & Astuces

✅ **Sauvegarde régulièrement le dossier `data/`**
✅ **Teste les commandes sur un channel privé d'abord**
✅ **Vérifie les logs (#logs-moderation, #logs-wl)**
✅ **Mets à jour le bot régulièrement**
✅ **Fais des backups de la configuration**

---

## 📝 Personnalisation

### Ajouter une catégorie de ticket

Dans `main.py`, trouve la section `TicketCategoryView` et ajoute une option:

```python
discord.SelectOption(label="📚 Catégorie", value="categorie"),
```

### Modifier le message de vérification

Dans `main.py`, cherche `on_member_join` et modifie l'embed.

### Changer les emojis

Dans les commandes, remplace les emojis (🔐, ⚠️, etc.)

---

## 🚀 Déploiement en Ligne (24/7)

### Option 1: Replit (Gratuit)

1. Va sur replit.com
2. "Create" → "Import from GitHub"
3. Colle l'URL GitHub du repo
4. Lance le bot avec `python main.py`
5. Utilise "Always On" pour 24/7

### Option 2: Railway (Gratuit avec crédit)

1. railway.app → Créer un project
2. Deploy from GitHub
3. Ajoute les variables d'environnement
4. Déploie!

### Option 3: VPS Personnel

1. Loue un VPS (OVH, Scaleway, etc.)
2. SSH dedans
3. Git clone ton repo
4. Lance avec `nohup python main.py &`

---

## 📞 Support

Si tu as des problèmes:

1. Vérifies les logs dans le terminal
2. Active le Mode Développeur Discord
3. Vérifie les permissions du bot
4. Redémarre le bot et Discord
5. Vérifie que les IDs sont corrects

---

**Bot créé pour Revital RP** 🎮
Version: 3.0
Dernière mise à jour: 2026
