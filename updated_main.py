import discord
import os 
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()


based_takes_words = ["based"]

starter_basedtakes = ["transhumanism based. - Matthew", "human rights don't exist. - Matthew", "libs and their security politics, biopolitics, n psychopolitics teehee - Matthew", "squid game is proof of capitalist realism. - Matthew", "the CIA is giving me tons of english homework on purpose so i don’t read more theory - Matthew", "the deterritorialization and destigmatization of certain language is good.  moral dumbfounding plagues us. we are frozen in time. i will neither elaborate nor specify what i'm talking about so i don't get cancelled. - Matthew"
                      , "accelerationism go brrr - Matthew", "you're a fucking ugly bitch. i wanna stab you to death, and play around with your blood. :Stare~1: -Matthew Bateman", "i love when abstract categorizations are warped into political bodies! i loveeeee mainstream progressive culture! 💞 - Matthew", "we remain in a perpetual culture war - Matthew", "libidinal expenditure through masturbatory politics. we go full circle ⚫ - Matthew"
                      , "scarcity is still a thing", "if there is no god, what else but capital can rule the world? - Matthew", "political discourse is dying; the cathedral is maintained. man is a sanctimonious animal! - Matthew", "progressive joystick go brr - Matthew", "we not escaping 😹😹 - Matthew", "soyjack soyjack L pseud. - Matthew", "left wing: ❌ right wing: ❌ chicken wing: ✅ - Matthew", "eating dogs is not inherently more unethical than eating farm animals - Matthew"
                      , "call me shang chi the way i be RINGin up ur girl at 10 so she can EAT my SOUL - Matthew", "jus found out about the male gaze, don't hmu not too happy rn ☹️ single women hmu - Matthew (single women please hit him up)", "thinking.. - Matthew (thinking)", "lemonade is definitely top 3 drinks. 🍋 - Matthew", "regulation doesn’t work in every fucking industry holyyy - Matthew", "god i hate the left - Matthew"
                      , "theory of exploitation is not a moral argument; it’s a scientific one. - Matthew", "stock buybacks are BASED. reformists are BASED. twitter populism is CRINGE. - Matthew", "the only commodity allowed within a communist society shall be the McRib - McMatthew", "TOP 10 THINGS REAGAN HAS DONE AS PRESIDENT: 1. die - Matthew"]


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


keep_alive()

client.run(os.getenv('KEY'))






