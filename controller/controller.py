import json
from models.models import User, USER_FILE


class Controller():

    @staticmethod
    def print_menu():
        print("1. Add New User\n"
              + "2. Get All Users\n"
              + "3. Search\n"
              + "4. Update User By Id"
              )

    @staticmethod
    def user_add():
        user = User(1, input("First Name: "), input("Last Name: "), input("Email: "))
        file = open('database/' + USER_FILE, 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()

        if len(all_users_data) > 0:
            user.id = all_users_data[-1]['id'] + 1
        else:
            user.id = 1

        dict = user.__dict__
        all_users_data.append(dict)
        with open('database/' + USER_FILE, 'w') as file:
            file.write(json.dumps(all_users_data))

    @staticmethod
    def get_all():
        with open('database/' + USER_FILE, 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['email'])

    @staticmethod
    def search_by(search_str, what_to_search):
        with open('database/' + USER_FILE, 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + user['email'])

    @staticmethod
    def update_user():
        file = open('database/' + USER_FILE, 'r')
        users = json.loads(file.read())
        file.close()
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['email'] = email

        with open('database/' + USER_FILE, 'w') as file:
            file.write(json.dumps(users))
