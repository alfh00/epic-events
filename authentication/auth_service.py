from .auth_controller import AuthenticationController
from .auth_presenter import AuthenticationPresenter

class AuthenticationService:
    def __init__(self):
        self.controller = AuthenticationController()
        self.presenter = AuthenticationPresenter()

    def register_user(self):
        
        registration_data = self.presenter.collect_registration_data()
        departments = self.controller.get_departments()
        department = self.presenter.select_department(departments)
        self.controller.register(registration_data, department)

    def login_user(self):
        username, password = self.presenter.prompt_for_credentials()
        user = self.controller.login(username, password)
        return user or False
