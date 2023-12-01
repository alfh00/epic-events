

class EmployeePresenter:
    @staticmethod
    def display_employees(employees):
        if not employees:
            print("No employees to display.")
                    
        column_widths = {
            
            "Username": 12,
            "Full Name": 18,
            "Email": 22,
            "Phone": 15,
            "Department": 12,
        }

        # Print headers
        headers = ["Username", "Full Name", "Email", "Phone", "Department"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for emp in employees:
            data = [
                emp['username'],
                emp['contact']['full_name'],
                emp['contact']['email'],
                emp['contact']['phone'],
                emp['department']['name'],
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)

        key = input('\n\nPress any key to continue...')

    @staticmethod
    def select_employee(employees):
        if not employees:
            print("No employees to update.")
            return None

        column_widths = {
            "N°": 3,
            "Username": 12,
            "Full Name": 18,
            "Email": 22,
            "Phone": 15,
            "Department": 12,
        }

        # Print headers row
        headers = ["N°", "Username", "Full Name", "Email", "Phone", "Department"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data rows
        for idx, emp in enumerate(employees, start=1):
            data = [
                str(idx),
                emp['username'],
                emp['contact']['full_name'],
                emp['contact']['email'],
                emp['contact']['phone'],
                emp['department']['name'],
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)

        while True:
            try:
                selected_index = int(input('\n\nEnter the number of the employee to select (0 to cancel): '))
                if 0 <= selected_index <= len(employees):
                    return selected_index - 1 if selected_index > 0 else None
                else:
                    print("Invalid selection. Please enter a number within the valid range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    @staticmethod
    def select_department(departments):
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

    @staticmethod
    def ask_for_employee_info_updates(emp):
        return {
        'new_username' : input(f'New Username ({emp["username"]}): '),
        'new_full_name' : input(f'New Full Name ({emp["contact"]["full_name"]}): '),
        'new_email' : input(f'New Email ({emp["contact"]["email"]}): '),
        'new_phone' : input(f'New Phone ({emp["contact"]["phone"]}): '),
        }
    
    def confirm(message):
       input(message + '\nPress Enter to continue...')