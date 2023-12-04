import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from dotenv import load_dotenv
load_dotenv()

from common.database import Event
from core.event_usecase.event_controller import EventController




def test_list_contract(setup_test_database, capsys):
    
    EventController.list_events()
    
    captured = capsys.readouterr()
    actual_output = captured.out


    assert str(Event.list_all()[0].note) in actual_output