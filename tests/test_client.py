import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from dotenv import load_dotenv
load_dotenv()

from common.database import Employee, Client
from core.client_usecase.client_controller import ClientController
from core.client_usecase.client_presenter import ClientPresenter

from authentication.user_context import UserContext 




def test_list_clients(setup_test_database, capsys):
    ClientController.list_clients()
    # Capture the output using capsys
    captured = capsys.readouterr()
    actual_output = captured.out.strip()
    assert Client.list_all()[0].company_name in actual_output

def test_create_client(mocker, capsys):
  

    mocker.patch.object(ClientPresenter, 'ask_for_client_infos', return_value={
      'client_contact' : {
            'full_name': 'full name',
            'email': 'email@test.com',
            'phone_number': '123-456-7890',
        },
      'client_company_name' : 'Company_name',
      'commercial_empl': Employee.filter_by_department('Commercial')[0],
    })

    client = ClientController.create_client()

    assert client.company_name == 'Company_name'

def test_update_client(setup_test_database, mocker):
    user_context = UserContext()
    user_context.set_current_user(Employee.filter_by_department('Gestion')[0].serialize())

    mocker.patch.object(ClientPresenter, 'select_client', return_value=0)
    mocker.patch.object(ClientPresenter, 'ask_what_to_update', return_value='1')
    mocker.patch.object(ClientPresenter, 'field_prompt', return_value='Company_name')

    ClientController.update_client()

    assert 'Company_name' == Client.list_all()[0].company_name


def test_delete_client(setup_test_database, mocker):
    selected_client= Client.list_all()[0]
    mocker.patch.object(ClientPresenter, 'select_client', return_value=0)
    ClientController.delete_client()
    assert selected_client not in Client.list_all()

