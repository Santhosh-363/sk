# (c) @RoyalKrrishna — Cleaned for Render Deployment

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "movie_bot")
    
    # User Session Removed for BOT-only mode
    USER_SESSION_STRING = None

    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "0"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    RESULTS_COUNT = int(os.environ.get("RESULTS_COUNT", 5))
    BROADCAST_AS_COPY = os.environ.get("BROADCAST_AS_COPY", "True")
    MOVIE_WEBSITE = os.environ.get("MOVIE_WEBSITE")
    UPDATES_CHANNEL_USERNAME = os.environ.get("UPDATES_CHANNEL_USERNAME", "")
    FORCE_SUB = os.environ.get("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", 300))
    MDISK_API = os.environ.get("MDISK_API", "12334")

    # Replit is unused in Render but kept for compatibility
    REPLIT_USERNAME = os.environ.get("REPLIT_USERNAME", None)
    REPLIT_APP_NAME = os.environ.get("REPLIT_APP_NAME", None)
    REPLIT = False
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "300"))
