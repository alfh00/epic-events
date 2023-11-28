from authentication.auth_service import AuthenticationService

from cli.menu import MenuController

import os

# import sentry_sdk

# sentry_sdk.init(
#     dsn="https://59d64b6565d242c8ac5dbe5632b5ab24@o4506236017377280.ingest.sentry.io/4506236067446784",
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     traces_sample_rate=1.0,
#     # Set profiles_sample_rate to 1.0 to profile 100%
#     # of sampled transactions.
#     # We recommend adjusting this value in production.
#     profiles_sample_rate=1.0,
# )

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
