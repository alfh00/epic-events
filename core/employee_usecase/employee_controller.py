from common.database import Employee
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
    

  def delete_employee(self):
    pass
   