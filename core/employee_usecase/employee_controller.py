from common.database import Employee
from authentication.auth_service import AuthenticationService

class EmployeeController:
  def add_employee(self):
    return AuthenticationService.login_user()
  
  def update_employee(self):
    pass
  def delete_employee(self):
    pass
   