from common.database import Employee
from ..employee_usecase.employee_presenter import EmployeePresenter


class ClientPresenter:
  def Display_all_client(clients):
    if not clients:
            print("No clients to display.")
                    
    column_widths = {
        
        "Full Name": 12,
        "Email": 22,
        "Phone": 15,
        "Company Name": 18,
        "Commercial Employee": 20,
    }

    # Print headers
    headers = ["Full Name", "Email", "Phone", "Company Name", "Commercial Employee"]
    header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
    print(header_line)
    print("-" * len(header_line))

    # Print data
    for client in clients:
        data = [
            client['client_contact']['full_name'],
            client['client_contact']['email'],
            client['client_contact']['phone'],
            client['company_name'],
            client['commercial_employee']['username'],
        ]
        data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
        print(data_line)

    key = input('\n\nPress any key to continue...')

  def ask_for_client_infos():
    client_contact = {
      'full_name' : input('Client Full Name: ' ),
      'email' : input('Client Email: ' ),
      'phone_number' : input('Client Phone Number: ' )
    }

    selected_emp = ClientPresenter.select_com_employee()

    client_company_name = input('Company Name: ')

    return {
      'client_contact' : client_contact,
      'client_company_name' : client_company_name,
      'commercial_empl': selected_emp,
    }
  
  def ask_for_client_infos_com():
    client_contact = {
      'full_name' : input('Client Full Name: ' ),
      'email' : input('Client Email: ' ),
      'phone_number' : input('Client Phone Number: ' )
    }

    client_company_name = input('Company Name: ')

    return {
      'client_contact' : client_contact,
      'client_company_name' : client_company_name,
    }
  
  def select_com_employee():
    comm_empl = Employee.filter_by_department('Commercial')
    serialised_employees = []
    for emp in comm_empl:
      emp = emp.serialize()
      serialised_employees.append(emp)
    
    emp_idx = EmployeePresenter.select_employee(serialised_employees)
    return comm_empl[emp_idx]

  def select_client(clients):
    if not clients:
      print("No clients to display.")
                    
    column_widths = {
        
        "N°": 3,
        "Full Name": 12,
        "Email": 22,
        "Phone": 15,
        "Company Name": 18,
        "Commercial Employee": 20,
    }

    # Print headers
    headers = ["N°","Full Name", "Email", "Phone", "Company Name", "Commercial Employee"]
    header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
    print(header_line)
    print("-" * len(header_line))

    for idx, client in enumerate(clients, start=1):
        data = [
            str(idx),
            client['client_contact']['full_name'],
            client['client_contact']['email'],
            client['client_contact']['phone'],
            client['company_name'],
            client['commercial_employee']['username'],
        ]
        data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
        print(data_line)

    while True:
            try:
                selected_index = int(input('\n\nEnter the number of the client to select (0 to cancel): '))
                if 0 <= selected_index <= len(clients):
                    return selected_index - 1 if selected_index > 0 else None
                else:
                    print("Invalid selection. Please enter a number within the valid range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

  def ask_what_to_update():
    print("\nWhat would you like to update?")
    print("1. Company Name")
    print("2. Associated Employee")
    print("3. Client Contact")
    print("4. Cancel")
   
    choice = None
    
    while choice not in ['1','2','3','4']:
        choice = input("Enter your choice (1-4): ")
    return choice
  
  def field_prompt(prompt):
      res = input(prompt)
      return res
      