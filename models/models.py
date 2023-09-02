from abc import ABC, abstractmethod
import json


class Model(ABC):
    file = 'default.json'

    @classmethod
    def get_all(cls):
        data = cls.get_file_data(cls.file)
        return data

    @staticmethod
    def get_file_data(file_name):
        file = open("database/" + file_name, 'r')
        data = json.loads(file.read())
        file.close()
        return data

    def save_to_file(self, data):
        data = json.dumps(data)
        file = open('database/' + self.file, "w")
        file.write(data)
        file.close()

    def save(self):
        generate_dict = self.__dict__
        data = self.get_file_data(self.file)
        data.append(generate_dict)
        try:
            element = self.get_by_id(self.id)
        except Exception:
            self.save_to_file(data)

    def set_id(self, data):
        if len(data) > 0:
            self.id = data[-1]['id'] + 1
        else:
            self.id = 1

    def add_to_file(self):

        all_data = self.get_file_data(self.file)

        self.set_id(all_data)

        dict = self.__dict__
        all_data.append(dict)
        with open('database/' + self.file, 'w') as file:
            file.write(json.dumps(all_data))

    @classmethod
    def search_by(self, search_str, what_to_search):
        data = self.get_file_data(self.file)
        founded = []
        for item in data:
            if str(search_str).lower() == str(item[what_to_search]).lower():
                founded.append(item)

        return founded

    @classmethod
    def update(self, id, first_name, last_name, email):
        data = self.get_file_data(self.file)

        for item in data:
            if item['id'] == id:
                item['first_name'] = first_name
                item['last_name'] = last_name
                item['email'] = email

        with open('database/' + self.file, 'w') as file:
            file.write(json.dumps(data))


class User(Model):
    file = "users.json"
    id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
