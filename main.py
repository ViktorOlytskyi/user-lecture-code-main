from controller.controller import Controller

while True:
    Controller.print_menu()
    menu_flag = int(input("Type your choose: "))
    if menu_flag == 1:
        Controller.user_add()
    elif menu_flag == 2:
        Controller.get_all()
    elif menu_flag == 3:
        what_to_search = input('By Which Parametr you want to search: ')
        search_str = input('Search: ')
        Controller.search_by(search_str, what_to_search)
    elif menu_flag == 4:
        Controller.update_user()
