from authentication.auth_service import AuthenticationService

from cli.menu import MenuController

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize the AuthenticationService
auth_service = AuthenticationService()

def main():
    print("Welcome to Your Terminal Authentication App")

    while True:
        
        print("\nMenu:")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            clear_console()
            user = auth_service.login_user()
            if user:
                print(user)
                return MenuController(user)
            else:
                print('no user try again')
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
