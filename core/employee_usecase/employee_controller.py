from common.database import Employee, Department
from authentication.auth_service import AuthenticationService

from .employee_presenter import EmployeePresenter

class EmployeeController:

  def list_employees():
    employees = Employee.list_all()
    serialised_employees = []
    for emp in employees:
      emp = emp.serialize()
      serialised_employees.append(emp)
    EmployeePresenter.display_employees(serialised_employees)
    

  def add_employee():
    return AuthenticationService.register_user()
  
  def update_employee():
    employees = Employee.list_all()

    serialised_employees = []
    for emp in employees:
      emp = emp.serialize()
      serialised_employees.append(emp)

    emp_idx = EmployeePresenter.select_employee(serialised_employees)
    selected_emp = employees[emp_idx]

    all_departments = Department.list_all()

    updated_infos = EmployeePresenter.ask_for_employee_info_updates(serialised_employees[emp_idx])

    new_department = EmployeePresenter.select_department(all_departments)

    selected_emp.update(username=updated_infos['new_username'])
    selected_emp.department = new_department
    selected_emp.contact.update(
      full_name=updated_infos['new_full_name'],
      email=updated_infos['new_email'],
      phone_number=updated_infos['new_phone'],
      )
    selected_emp._session.commit()

  def delete_employee():
    employees = Employee.list_all()
    
    serialised_employees = []
    for emp in employees:
      emp = emp.serialize()
      serialised_employees.append(emp)

    emp_idx = EmployeePresenter.select_employee(serialised_employees)
    selected_emp = employees[emp_idx]
    result = selected_emp.delete()
    if result:
      print('the emp has been deleted')
    else:
      print('something went wrong')