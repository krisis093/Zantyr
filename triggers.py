import json
import random
from userdb import userdb

TRIGGERFILE = "./triggers.json"

with open(TRIGGERFILE, "r") as f:
    TRIGGERS = json.load(f)


def triggerMe(client, message):
    for trigger in TRIGGERS:
        if any([s in message.content for s in trigger["triggers"]]):
            if "minantipathy" in trigger.keys() and "maxantipathy" in trigger.keys():
                if trigger["minantipathy"] < self.db[message.author.id]['antipathy'] < trigger["maxantipathy"]:
                    if random.random() < trigger["chance"]:
                        return random.choice(trigger["reactions"])
            else:
                if random.random() < trigger["chance"]:
                    return random.choice(trigger["reactions"])

EXPORT = [triggerMe]
