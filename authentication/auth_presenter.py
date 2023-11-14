import getpass

class AuthenticationPresenter:
  def prompt_for_credentials(self):
    username = input('Username:')
    password = getpass.getpass(prompt='Password:')
    return username, password

  def collect_registration_data(self):
      # Collect and validate user registration data
    username = input('Username: ')
    password = getpass.getpass(prompt='Password: ')
    confirmed_password = getpass.getpass(prompt='Confirm Password: ')
    full_name = input('Full Name: ')
    email = input('Email: ')
    phone = input('Phone: ')

    new_employee  = {
      'username': username,
      'password': password,
      'confirmed_password': confirmed_password, 
      'full_name': full_name,
      'email': email,
      'phone': phone,
    }
    return new_employee

    # Other methods for presenting information to the user
  def select_department(self, departments):
        print("Select a department:")
        for index, department in enumerate(departments, start=1):
            print(f"{index}. {department.department_name}")

        while True:
            try:
                choice = int(input("Enter the number of the department: "))
                if 1 <= choice <= len(departments):
                    return departments[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

