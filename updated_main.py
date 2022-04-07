import discord
import os 
import requests
import json
import random
from replit import db


client = discord.Client()


based_takes_words = ["based", "Matthew", "matthew", "takes", "political", "why", "matt", "EUGH"]

starter_basedtakes = ["transhumanism based. -Matthew", "human rights don't exist. -Matthew", "rethinking security politics, biopolitics-Matthew, n psychopolitics-Matthew", "squid game is proof of capitalist realism.-Matthew", "the CIA is giving me tons of english homework on purpose so i don’t read more theory-Matthew", "WAKE UP BABE PANDORA PAPERS JUS DROPPED!!!-Matthew", "accelerationist arc?-Matthew", "market stalinism go brrrr in every crevice around the world-Matthew"]


def update_based(based_msg):
  if "base" in db.keys():
    based = db["base"]
    based.append(based_msg)
    db["base"] = based
  else:
    db["base"] = [based_msg]

def delete_based(index):
  based = db["base"]
  if len(based) > index:
    del based[index]
    db["base"] = based


@client.event
async def on_ready():
  print('We haven logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  options = starter_basedtakes
  if "base" in db.keys():
    options.extend(db["base"])
  
  if any(word in msg for word in based_takes_words):
    await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    based_msg = msg.split("$new ", 1)[1]
    update_based(based_msg)
    await message.channel.send("New based take added.")
    
  if msg.startswith("$del"):
    based = []
    if "base" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_based(index)
      based = db["base"]
    await message.channel.send(based)

      
client.run(os.getenv('KEY'))






