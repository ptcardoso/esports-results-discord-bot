import os
from dotenv import load_dotenv

load_dotenv()

# https://discordapp.com/oauth2/authorize?client_id={}&scope=bot
TOKEN = os.environ['DISCORD_BOT_TOKEN']
