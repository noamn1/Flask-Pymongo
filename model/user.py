import json


class User:

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __init__(self, user_id, first_name, last_name, username, email, age, date):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.email = email
        self.date = str(date)
