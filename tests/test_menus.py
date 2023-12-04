import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from cli.menu import MenuController
from cli.menu_models import gestion_menu, commercial_menu, support_menu
from authentication.user_context import UserContext

from common.database import Employee



def test_manager_menu(setup_test_database, capsys):
  manager = Employee.filter_by_department('Gestion')[0]
  serialized_manager = manager.serialize()

  context_user = UserContext()
  auth_user = context_user.set_current_user(serialized_manager)

  user_menu = MenuController(serialized_manager)

  assert user_menu.menu == gestion_menu




