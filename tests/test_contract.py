import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from dotenv import load_dotenv
load_dotenv()

from common.database import Contract
from core.contract_usecase.contract_controller import ContractController
from core.contract_usecase.contract_presenter import ContractPresenter

from core.client_usecase.client_presenter import ClientPresenter

from authentication.user_context import UserContext 



def test_list_contract(setup_test_database, capsys):
    ContractController.list_contracts()
    
    captured = capsys.readouterr()
    actual_output = captured.out

    assert str(Contract.list_all()[0].paid_amount) in actual_output

def test_create_contract(setup_test_database, mocker, capsys):
    mocker.patch.object(ClientPresenter, 'select_client', return_value=0)
    mocker.patch.object(ContractPresenter, 'ask_for_contract_inputs', return_value={
      'total_amount' : 1000,
      'paid_amount' : 500,
      'is_signed' : False
      })
    
    ContractController.create_contract()

    captured = capsys.readouterr()
    actual_output = captured.out

    assert 'Contract created.' in actual_output

