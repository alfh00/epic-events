from core.employee_usecase.employee_controller import EmployeeController
from core.contract_usecase.contract_controller import ContractController
from core.client_usecase.client_controller import ClientController
from core.event_usecase.event_controller import EventController

class Menu:
  def __init__(self, name, action=None, submenus=None):
        self.name = name
        self.action = action
        self.submenus = submenus if submenus else []

gestion_menu = Menu(
            "Main Menu",
            submenus=[
                Menu("Employee", submenus=[
                    Menu("Display Employees", action=EmployeeController.list_employees),
                    Menu("Add an Employee", action=EmployeeController.add_employee),
                    Menu("Update an Employee", action=EmployeeController.update_employee),
                    Menu("Delete an Employee", action=EmployeeController.delete_employee),
                    Menu("Back"),
                ]),
                Menu("Contracts", 
                    submenus=[
                    Menu("Display Contracts", action=ContractController.list_contracts),
                    Menu("Add a Contract", action=ContractController.create_contract),
                    Menu("Update a contract", action=ContractController.update_contract),
                    Menu("Delete a contract", action=ContractController.delete_contract),
                    Menu("Back"),
                ]),
                Menu("Events", 
                     submenus=[
                    Menu("Display Events", action=EventController.list_events),
                    Menu("Filter Events without support", action=EventController.list_events_no_support),
                    Menu("Add an Event", action=EventController.create_event),
                    Menu("Update an Event", action=EventController.update_event),
                    Menu("Assign Support", action=EventController.assign_support),
                    Menu("Back"),
                ]),
                Menu("Exit"),
            ],
        )
commercial_menu = Menu(
            "Main Menu",
            submenus=[
                Menu("Clients", 
                    submenus=[
                    Menu("Display Clients", action=ClientController.list_clients),
                    Menu("Add a Client", action=ClientController.create_client),
                    Menu("Update a Client", action=ClientController.update_client),
                    Menu("Delete a Client", action=ClientController.delete_client),
                    Menu("Back"),
                ]),
                Menu("Contracts", 
                    submenus=[
                    Menu("Display Contracts", action=ContractController.list_contracts),
                    Menu("Add a Contract", action=ContractController.create_contract),
                    Menu("Update a contract", action=ContractController.update_contract),
                    Menu("Delete a contract", action=ContractController.delete_contract),
                    Menu("Back"),
                ]),
                Menu("Events", 
                     submenus=[
                    Menu("Display Events", action=EventController.list_events),
                    Menu("Add an Event", action=EventController.create_event),
                    Menu("Update an Event", action=EventController.update_event),
                    
                    Menu("Back"),
                ]),
                Menu("Exit"),
            ],
        )
support_menu = Menu(
            "Main Menu",
            submenus=[
                Menu("Clients", 
                    submenus=[
                    Menu("Display Clients", action=ClientController.list_clients),
                    Menu("Back"),
                ]),
                Menu("Contracts", 
                    submenus=[
                    Menu("Display Contracts", action=ContractController.list_contracts),
                    Menu("Back"),
                ]),
                Menu("Events", 
                     submenus=[
                    Menu("Display All Events", action=EventController.list_events),
                    Menu("Display My Events", action=EventController.list_my_events),
                    Menu("Update My Events", action=EventController.update_my_event),
                    Menu("Back"),
                ]),
                Menu("Exit"),
            ],
        )