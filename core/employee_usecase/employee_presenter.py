

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

        # Print headers
        headers = ["N°", "Username", "Full Name", "Email", "Phone", "Department"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
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


   