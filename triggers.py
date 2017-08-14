import json
import random
from usersdb import usersDB

TRIGGERFILE = "./triggers.json"

with open(TRIGGERFILE, "r") as f:
    TRIGGERS = json.load(f)


def triggerMe(client, message):
    for trigger in TRIGGERS:
        if any([s in message.content for s in trigger["triggers"]]):
            if trigger["minantypathy"] and trigger["maxantypathy"]:
                if trigger["minantypathy"] < self.db[message.author.id]['antipathy'] < trigger["maxantypathy"]:
                    if random.random() < trigger["chance"]:
                        return random.choice(trigger["reactions"])
            else:
                if random.random() < trigger["chance"]:
                    return random.choice(trigger["reactions"])
EXPORT = [triggerMe]
