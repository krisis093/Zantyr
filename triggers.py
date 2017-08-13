import json
import random

TRIGGERFILE = "./triggers.json"

with open(TRIGGERFILE, "r") as f:
    TRIGGERS = json.load(f)


def triggerMe(client, message):
    for trigger in TRIGGERS:
        if any([s in message.content for s in trigger["triggers"]]):
            if random.random() < trigger["chance"]:
                return random.choice(trigger["reactions"])

EXPORT = [triggerMe]
