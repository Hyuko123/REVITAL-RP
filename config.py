# ============================================================
#  CONFIGURATION — REVITAL RP BOT v4
#  Remplis toutes les valeurs avec les IDs de ton serveur
# ============================================================

# ── BOT ──────────────────────────────────────────────────────
TOKEN    = "MTUxNzAwMjg3NzYzMjEyMjk4Mg.GXQ_QA.fH5T3h4P-sxh91npkNTWWnEyqUrj3I2B-iqnjA"
GUILD_ID = 1516284708219256962

# ── CHANNELS LOGS ────────────────────────────────────────────
LOGS_CHANNEL            = 1517020116737593455   # #logs-moderation (warns, kicks, bans, mutes)
LOGS_WL_CHANNEL         = 1516285063996899359   # #logs-wl (whitelists)
LOGS_TICKETS_CHANNEL    = 1517020177508733092   # #logs-tickets (ouverture/fermeture tickets)
LOGS_REMBOURSEMENT_CHANNEL = 1517050226387714048   # #logs-remboursement (remboursements)

# ── CHANNELS FONCTIONNELS ────────────────────────────────────
VERIFICATION_CHANNEL = 1517020243975864442   # #verification (captcha au join)
WELCOME_CHANNEL      = 1516285038151471255   # #bienvenue-départ (messages join/leave)

# ── CATÉGORIE DISCORD POUR LES TICKETS ──────────────────────
# ID de la catégorie Discord dans laquelle les tickets seront créés.
# Mets 0 si tu ne veux pas de catégorie.
TICKET_CATEGORY_ID = 0  # ← Remplace par l'ID de ta catégorie "Tickets"

# Canaux Discord spécifiques par type de ticket (optionnel)
# Si tu veux que chaque catégorie aille dans une sous-catégorie différente,
# renseigne les IDs ici. Sinon, laisse 0.
TICKET_CHANNELS = {
    "boutique":    1516285006492995694,   # catégorie Discord pour 💎 Boutique/Remboursement
    "superviseur": 1516285007818391652,   # catégorie Discord pour ⚜️ Superviseur
    "recrutement": 1516285008837611540,   # catégorie Discord pour 🔵 Recrutement Staff
    "legal":       1516285009713954906,   # catégorie Discord pour 🟢 Dossier Légal
    "illegal":     1516285011177898054,   # catégorie Discord pour 🔴 Dossier Illégal
    "wiperp":      1516285012062900346,   # catégorie Discord pour 💀 Wipe/Mort RP
}

# ── RÔLES ────────────────────────────────────────────────────
CITOYEN_WL_ROLE  = 1517007376287404103   # Rôle assigné après whitelist acceptée
MUTED_ROLE       = 1517007357320626336   # Rôle "Muted"
UNVERIFIED_ROLE  = 1517043612892926002   # Rôle donné à l'arrivée (non vérifié)
VERIFIED_ROLE    = 1516284942064025661   # Rôle après vérification captcha
STAFF_ROLE       = 1516284938645798953   # Rôle Staff/Modérateur

# ── SANCTIONS AUTOMATIQUES ───────────────────────────────────
# Durée du mute automatique à 3 warns (en secondes)
# 3600 = 1h | 7200 = 2h | 86400 = 1 jour
AUTO_SANCTION_MUTE_DURATION = 3600   # Mute 1h à 3 warns
# À 5 warns → Kick automatique
# À 7 warns → Ban automatique

# ============================================================
#  COMMENT RÉCUPÉRER LES IDs
#
#  1. Active le Mode Développeur Discord :
#     Paramètres → Avancé → Mode Développeur ✅
#
#  2. Clic droit sur :
#     - Un salon  → "Copier l'identifiant du salon"
#     - Un rôle   → "Copier l'identifiant du rôle"
#     - Le serveur → "Copier l'identifiant du serveur"
# ============================================================
