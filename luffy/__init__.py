from telethon import TelegramClient
import logging
import time


openai_key = "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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6243206260:AAHLYG28m8GL5Gs4CfXbaDyoFk9VLJXyHF4"

bot=TelegramClient("Robinbig",api_id,api_hash).start(bot_token = bot_token)
