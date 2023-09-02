import json
from models.models import User, Model


class Controller():

    @staticmethod
    def print_menu():
        print("1. Add New User\n"
              + "2. Get All Users\n"
              + "3. Search\n"
              + "4. Update User By Id"
              )

    @staticmethod
    def add_new_user():
        user = User(input("First Name: "), input("Last Name: "), input("Email: "))
        user.add_to_file()

    @staticmethod
    def get_all():
        users = User.get_all()
        for user in users:
            print("User #" + str(user['id']))
            print("First Name: " + user['first_name'])
            print("Last Name: " + user['last_name'])
            print("Email: " + user['email'])

    @staticmethod
    def search_by(search_str, what_to_search):
        founded = User.search_by(search_str, what_to_search)
        if not founded:
            print('No one founded')
        else:
            for user in founded:
                print("Founded user:")
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['email'])

    @staticmethod
    def update_user():
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        User.update(id, first_name, last_name, email)
