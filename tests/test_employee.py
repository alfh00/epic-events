import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from common.database import Employee, Department
from authentication.auth_service import AuthenticationService
from core.employee_usecase.employee_controller import EmployeeController, EmployeePresenter



def test_list_employees(setup_test_database, capsys):

    EmployeeController.list_employees()
    # Capture the output using capsys
    captured = capsys.readouterr()
    actual_output = captured.out.strip()
    # Assert that the serialized data matches the expected output
    assert Employee.list_all()[0].username in actual_output 




def test_add_employee_successfully_registered(setup_test_database, mocker, capsys):
    # Authentication will be tested seperatly
    # Mock the register_user method to return True (success)
    mocker.patch.object(AuthenticationService, 'register_user', return_value=True)

    # Call the add_employee function
    EmployeeController.add_employee()

    # Assertions
    AuthenticationService.register_user.assert_called_once()

    # Capture printed output
    captured = capsys.readouterr()
    actual_output = captured.out
    
    assert "successfully" in actual_output

def test_add_employee_registration_failed(setup_test_database, mocker, capsys):
    # Mock the register_user method to return True (success)
    mocker.patch.object(AuthenticationService, 'register_user', return_value=False)

    # Call the add_employee function
    EmployeeController.add_employee()

    # Assertions
    AuthenticationService.register_user.assert_called_once()

    # Capture printed output
    captured = capsys.readouterr()
    actual_output = captured.out
    
    assert "went wrong" in actual_output


def test_update_employee_successfully_updated(setup_test_database, mocker, capsys):

    # Mock the select_employee method of EmployeePresenter to return an index
    mocker.patch.object(EmployeePresenter, 'select_employee', return_value=1)

    # Mock the ask_for_employee_info_updates method of EmployeePresenter to return updated info
    mocker.patch.object(EmployeePresenter, 'ask_for_employee_info_updates', return_value={
        'new_username': 'updated_user',
        'new_full_name': 'Updated User',
        'new_email': 'updated@example.com',
        'new_phone': '555-555-5555',
    })

    # Mock the select_department method of EmployeePresenter to return a department
    mocker.patch.object(EmployeePresenter, 'select_department', return_value=Department.read(department_id=1))

    # Call the update_employee function
    EmployeeController.update_employee()

    # Assertions

    captured = capsys.readouterr()
    #check if the wight messgae was printed
    assert "Successfully updated..." in captured.out
    #check if the department was updated
    assert Employee.list_all()[0].department == Department.read(department_id=1)


# def test_delete_employee_successfully_deleted(mocker, capsys):
#     # Mock the select_employee method of EmployeePresenter to return an index
    
#     mocker.patch.object(EmployeePresenter, 'select_employee', return_value=2)
#     selected_emp = Employee.list_all()[2]
    
#     # Call the delete_employee function
#     EmployeeController.delete_employee()

#     # Capture printed output
#     captured = capsys.readouterr()
#     #check if the right message is printed
#     assert "has been deleted" in captured.out
#     #check if the deleted employee doesnt exist anymore
#     assert selected_emp not in Employee.list_all()



def test_delete_employee_not_deleted(setup_test_database, mocker, capsys):
    # Mock the select_employee method of EmployeePresenter to return an index
    mocker.patch.object(EmployeePresenter, 'select_employee')
    # Mock the select_employee method of EmployeePresenter to return None
    mocker.patch.object(EmployeePresenter, 'select_employee', return_value=None)
    selected_emp = Employee.list_all()[0]

    # Call the delete_employee function
    EmployeeController.delete_employee()

    
    #check if the right message is printed
    assert selected_emp in Employee.list_all()






