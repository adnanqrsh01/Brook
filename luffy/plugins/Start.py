from .. import bot, openai_key
from telethon import events 
import asyncio
#import openai

#openai.my_api_id = "openai_key"

@bot.on(events.NewMessage(incoming= True,pattern="/start"))
async def start(event):
  await event.reply ("Hello This is Robinbig bot")
  
  
@bot.on(events.NewMessage(incoming= True,pattern="/get"))
async def start(event):
  a=await event.reply("hii this is get command")
  await asyncio.sleep(3)
  await a.edit("it is  edited a msg")
  
  
@bot.on(events.NewMessage(incoming= True,pattern="/eval"))
async def start(event):
  await event.reply("hii this is eval command")