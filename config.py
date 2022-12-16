import os

API_ID = int(os.environ.get("API_ID", "18078505"))
API_HASH = os.environ.get("API_HASH", "fd98890afedd24d650f9698007e14754")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5826445829:AAEso-66DszfjpTfGRTu71RuJ5CMjl46NgA")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001876960404")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", "1801434814"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
