import json


class UsersDB(object):
    DBFILE = "./users.json"

    def __init__(self):
        with open(self.DBFILE, 'r') as f:
            self.db = json.load(f)
    def expectGenitive(self, name):
        gens = dict([(name, id) for (id, u) in self.db.items() for name in u.names.genitives])
        noms = dict([(name, id) for (id, u) in self.db.items() for name in u.names.nominatives])
        if name in gens.keys():
            return int(gens[name])
        elif name in noms.keys():
            return int(noms[name])

    def addOrEditUser(self, id, data):
        if name not in self.db.keys():
            self.db[id] = data
        else:
            self.db[id].update(data)
        with open(DBFILE, 'w') as f:
            json.dump(f, self.db)
