# ⚡ Guide Rapide - Revital RP Bot v3

## 1️⃣ Installation (5 min)

```bash
# Installe les dépendances
pip install -r requirements.txt

# Lance le bot
python main.py
```

## 2️⃣ Configuration

**Dans `config.py`, remplace:**

```python
TOKEN = "TON_TOKEN_ICI"
GUILD_ID = 123456789
LOGS_CHANNEL = 123456789
LOGS_WL_CHANNEL = 123456789
TICKETS_CHANNEL = 123456789
VERIFICATION_CHANNEL = 123456789
CITOYEN_WL_ROLE = 123456789
MUTED_ROLE = 123456789
VERIFIED_ROLE = 123456789
```

## 3️⃣ Activé les Intents (Discord Developer Portal)

1. Applications → Ton Bot → Bot
2. Scroll vers "PRIVILEGED GATEWAY INTENTS"
3. Active: 
   - ☑️ Presence Intent
   - ☑️ Server Members Intent
   - ☑️ Message Content Intent

## 4️⃣ Crée les Structures

**Rôles:**
- citoyen-wl
- Muted
- Verified

**Channels:**
- #logs-moderation
- #logs-wl
- #tickets
- #verification

## 5️⃣ Teste le Bot

```bash
python main.py

# Tu devrais voir:
# ✅ Bot connecté en tant que Revital RP Bot
# ✅ Slash commands synchronisées!
```

## 🎯 Premières Commandes

```
/setup-tickets          → Activer les tickets
/verify CODE            → Tester la vérification
/whitelist @user        → Tester la whitelist
```

---

**C'est prêt!** 🚀

Pour plus de détails → voir README.md
