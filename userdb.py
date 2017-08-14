import json
from copy import deepcopy


class UsersDB(object):
    DBFILE = "./users.json"
    SCHEMA = {"name": "", "antipathy": 0, "note": ""}
    LIKES_GEN = []
    LIKES_NOM = []
    DISLIKES_GEN = ['vitava']
    DISLIKES_NOM = ['vitav']
    DISLIKE_VERB_GEN = ['jebać', 'jebanego', 'popierdolonego', 'pierdolonego', 'chujowego', 'pieprzonego']
    DISLIKE_VERB_NOM = ['jebany', 'pierdolony']

    def __init__(self):
        with open(self.DBFILE, 'r') as f:
            self.db = json.load(f)

    def commit(self):
        # if too much load, create journal and dump to json each N commits
        with open(self.DBFILE, 'w') as f:
            json.dump(self.db, f)

    def addUser(self, id, name):
        self.db[id] = deepcopy(self.SCHEMA)
        self.db[id]["name"] = name
        self.commit()

    def passiveScan(self, client, message):
        if message.author.id not in self.db.keys():
            self.addUser(message.author.id, message.author.name)
            return "{name}, witaj na forum. Gdybyś kiedykolwiek czegoś potrzebował, zawołaj mnie lub wpisz '!jestemjebanymnoobempomuszmi'. To ostatni raz, kiedy jestem tak pomocny."
        if message.content == "!lubiszmje?":
            return str(self.db[message.author.id]['antipathy'])
        words = [i.strip(".,?! \"()[{}]-+=/|\\*_@") for i in message.content.lower().split()]
        try:
            test = [i in self.DISLIKE_VERB_GEN for i in words]
            if any(test):
                if words[test.index(True) + 1] in self.DISLIKES_GEN:
                    self.db[message.author.id]['antipathy'] -= 1
                    self.commit()
                elif words[test.index(True) + 1] in self.LIKES_GEN:
                    self.db[message.author.id]['antipathy'] += 1
                    self.commit()
            test = [i in self.DISLIKE_VERB_NOM for i in words]
            if any(test):
                if words[test.index(True) + 1] in self.DISLIKES_NOM:
                    self.db[message.author.id]['antipathy'] -= 1
                    self.commit()
                elif words[test.index(True) + 1] in self.LIKES_NOM:
                    self.db[message.author.id]['antipathy'] += 1
                    self.commit()
        except:
            pass

    def editNote(self, id, note):
        self.db[id]['note'] = note
        self.commit()

userdb = UsersDB()


EXPORT = [userdb.passiveScan]
