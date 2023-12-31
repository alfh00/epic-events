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
    registred = AuthenticationService.register_user()
    if registred:
      return EmployeePresenter.confirm('New employee successfully registred...')
    else:
      return EmployeePresenter.confirm('Something went wrong while registring...')
  
  
  def update_employee():
    employees = Employee.list_all()

    serialised_employees = [e.serialize() for e in employees]
   
    emp_idx = EmployeePresenter.select_employee(serialised_employees)
    selected_emp = employees[emp_idx]

    all_departments = Department.list_all()

    updated_infos = EmployeePresenter.ask_for_employee_info_updates(serialised_employees[emp_idx])

    new_department = EmployeePresenter.select_department(all_departments)

    try:

      selected_emp.update(username=updated_infos['new_username'])
      selected_emp.department = new_department
      selected_emp.contact.update(
        full_name=updated_infos['new_full_name'],
        email=updated_infos['new_email'],
        phone_number=updated_infos['new_phone'],
        )
      selected_emp._session.commit()
      EmployeePresenter.confirm('Successfully updated...')
    except Exception as e:
      EmployeePresenter.confirm(f'Something Went wrong while updating...\n{e}')

  def delete_employee():
    employees = Employee.list_all()
    
    serialised_employees = [e.serialize() for e in employees]

    emp_idx = EmployeePresenter.select_employee(serialised_employees)
    if not emp_idx: return
    selected_emp = employees[emp_idx]
    result = selected_emp.delete()
    if result:
      EmployeePresenter.confirm('the emp has been deleted')
    else:
      EmployeePresenter.confirm('something went wrong')