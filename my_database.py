import json


class Database:

    def add_data(self, name, email, password):

        with open('database.json', 'r') as rf:
            db = json.load(rf)

        if email in db:
            return 0
        else:
            db[email] = [name, password]
            with open('database.json', 'w') as wf:
                json.dump(db, wf)
            return 1

    def search(self, email, password):

        with open('database.json', 'r') as rf:
            db = json.load(rf)

        if email in db:
            if db[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0
