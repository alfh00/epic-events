import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from authentication.auth_controller import AuthenticationController
from common.database import Employee, Department


def test_register(setup_test_database, capsys):
  registration_data = {
    'username': 'new_user',
    'full_name': 'new_user',
    'email': 'email@example.com',
    'password': 'password123',
    'confirmed_password': 'password123',
    'phone_number': '123-456-9999',
    }
  department = Department.list_all()[0]
  AuthenticationController.register(registration_data, department)
  assert Employee.filter_by_keyword(username='new_user') is not None


def test_login(setup_test_database, capsys):
  registration_data = {
    'username': 'new_user',
    'full_name': 'new_user',
    'email': 'email@example.com',
    'password': 'password123',
    'confirmed_password': 'password123',
    'phone_number': '123-456-9999',
    }
  department = Department.list_all()[0]
  AuthenticationController.register(registration_data, department)
  new_user = Employee.read(username='new_user')
  loggedin_emp = AuthenticationController.login(username='new_user', password='password123')

  assert new_user == loggedin_emp