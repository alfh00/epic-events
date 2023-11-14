from .auth_controller import AuthenticationController
from .auth_presenter import AuthenticationPresenter

class AuthenticationService:
    def __init__(self):
        self.controller = AuthenticationController()
        self.presenter = AuthenticationPresenter()
        
    @staticmethod
    def register_user():
        
        registration_data = AuthenticationPresenter.collect_registration_data()
        departments = AuthenticationController.get_departments()
        department = AuthenticationPresenter.select_department(departments)
        AuthenticationController.register(registration_data, department)
    
    def login_user(self):
        username, password = self.presenter.prompt_for_credentials()
        user = self.controller.login(username, password)
        return user or False
