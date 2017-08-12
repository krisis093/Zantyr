import discord
import logging
import time
import random
import json
import importlib
import os

# serwer IP: 195.181.219.13

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('discord')

client = discord.Client()

EXTENSIONS = []
for path in os.listdir('.'):
    if path[-3:] == ".py" and path != "main.py":
        log.info("Importing {}...".format(path[:-3]))
        module = importlib.import_module(path[:-3])
        try:
            EXTENSIONS.extend(module.EXPORT)
        except:
            log.error("Cannot import {}!".format(path[:-3]))

TOKEN = "MzQ1NjY5Nzc1NDk1NjU5NTIx.DG-pog.UvSoILSNd3LhrG49Y3X-ZziB_VM"
WKURWRATE = 9
WKURWFILE = "./wkurw.txt"
WKURWDICT = []

with open(WKURWFILE, "r") as f:
    for line in f:
        WKURWDICT.append(line)

from userdb import UsersDB
client.userdb = UsersDB()

@client.event
async def on_ready():
    log.info("Logged as {} - {}".format(client.user.name, client.user.id))

@client.event
async def on_message(message):
    log.info("    {}({})@{}: {}".format(message.author.nick if message.author.nick else message.author.name, message.author.id, message.channel, message.content))
    if message.author==client.user:
        log.debug("Oh, it's me")
    else:
        for extension in EXTENSIONS:
            msg = extension(client, message)
            if msg:
                client.send_typing(message.channel)
                time.sleep(0.02 * len(msg) + 0.5)
                await client.send_message(message.channel, msg.format(
                    name=(message.author.nick if message.author.nick else message.author.name)))
                break
        else:
            if random.randint(0, WKURWRATE)==0:
                client.send_typing(message.channel)
                time.sleep(1)
                await client.send_message(message.channel, random.choice(WKURWDICT).format(
                    name=(message.author.nick if message.author.nick else message.author.name)))
            else:
                log.debug("Damn, got no response ;(")

client.run(TOKEN)  # BOTEMAIL, BOTPW)