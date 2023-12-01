from .menu_models import commercial_menu, gestion_menu, support_menu

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
        
class MenuController:
    def __init__(self, user):
        self.user = user
        self.menu = self.generate_menu()
        self.display_menu()

    def generate_menu(self):
        if self.user['department']['name'] == 'Gestion':
            return self.generate_gestion_menu()
        elif self.user['department']['name'] == 'Commercial':
            return self.generate_commercial_menu()
        elif self.user['department']['name'] == 'Support':
            return self.generate_support_menu()

    def generate_gestion_menu(self):
        return gestion_menu

    def generate_commercial_menu(self):
        return commercial_menu

    def generate_support_menu(self):
        return support_menu

    def display_menu(self, current_menu=None):
        parent_menu = None
        if not current_menu:
          current_menu = self.menu
        while True:
            clear_console()
            print(current_menu.name)
            for index, submenu in enumerate(current_menu.submenus, start=1):
                print(f"{index}. {submenu.name}")

            choice = input("Enter your choice: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(current_menu.submenus):
                    selected_submenu = current_menu.submenus[choice - 1]
                    if selected_submenu.name == "Back":
                        if parent_menu is None:
                            print("Cannot go back from the main menu.")
                        else:
                            current_menu = parent_menu  # Go back to the parent menu
                    elif selected_submenu.name == "Exit":
                        self.say_goodbye()
                        return
                    else:
                        if selected_submenu.submenus:
                            parent_menu = current_menu  # Update the parent menu
                            current_menu = selected_submenu
                        else:
                            selected_submenu.action()
                else:
                    print("Invalid choice. Please try again.")
            else:
                print("Invalid input. Please enter a number.")

    def say_goodbye(self):
        print(f"Goodbye!")
        



