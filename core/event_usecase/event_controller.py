from common.database import Event, Employee, Contract
from .event_presenter import EventPresenter

from ..contract_usecase.contract_presenter import ContractPresenter
from ..employee_usecase.employee_presenter import EmployeePresenter

from authentication.user_context import UserContext

class EventController:
  def list_events():
    events = Event.list_all()
    serialized_events = [event.serialize() for event in events]
    return EventPresenter.display_events(serialized_events)
  
  def list_events_no_support():
    events = Event.filter_by_keyword(support_employee_id=None)
    serialized_events = [event.serialize() for event in events]
    return EventPresenter.display_events(serialized_events)
    

  def create_event():
    user_context = UserContext()
    auth_user = user_context.get_current_user()
    if auth_user['department']['name'] == 'Gestion':
      contracts = Contract.list_all()
    else:
      contracts = Contract.filter_by_keyword(is_signed=True)
    # select the contract 
    serialized_contracts = [contract.serialize() for contract in contracts]
    contract_idx = ContractPresenter.select_contact(serialized_contracts)
    event_contract = serialized_contracts[contract_idx]

    #select the support employee
    support_employees = Employee.filter_by_department(department_name='Support')
    serialized_support_employee = [emp.serialize() for emp in support_employees]
    employee_idx = EmployeePresenter.select_employee(serialized_support_employee)
    event_employee = serialized_support_employee[employee_idx]

    event_infos = EventPresenter.ask_event_inputs()

    try:
      new_event = Event.create(
        contract_id=event_contract['contract_id'],
        support_employee_id=event_employee['employee_id'],
        start_date=event_infos['start_date'],
        end_date=event_infos['end_date'],
        location=event_infos['location'],
        attendees=event_infos['attendees'],
        note=event_infos['note']
      )
      if new_event:
        input('created')
      else:
        input('something went wrong')
    except Exception:
      input('something went wrong')


  def update_event():
    
    events = Event.list_all()
    serialized_events = [event.serialize() for event in events]

    event_idx = EventPresenter.select_event(serialized_events)
    selected_event = events[event_idx]

    event_infos = EventPresenter.ask_event_inputs()


  def assign_support():
    events = Event.list_all()
    serialized_events = [event.serialize() for event in events]

    event_idx = EventPresenter.select_event(serialized_events)
    selected_event = events[event_idx]

    #select the support employee
    support_employees = Employee.filter_by_department(department_name='Support')
    serialized_support_employee = [emp.serialize() for emp in support_employees]
    employee_idx = EmployeePresenter.select_employee(serialized_support_employee)
    input(employee_idx)
    selected_employee = serialized_support_employee[employee_idx]
    input(selected_employee)

    updated = selected_event.update(support_employee_id=selected_employee['employee_id'])

    if updated:
      EventPresenter.confirm('Successfully updated.')
    
    else:
      EventPresenter.confirm('Something went Wrong...')

  def list_my_events():
    user_context = UserContext()
    auth_user = user_context.get_current_user()

    events = Event.filter_by_keyword(support_employee_id=auth_user['employee_id'])
    serialized_events = [e.serialize() for e in events]
    return EventPresenter.display_events(serialized_events)

  def update_my_event():
    user_context = UserContext()
    auth_user = user_context.get_current_user()

    events = Event.filter_by_keyword(support_employee_id=auth_user['employee_id'])
    serialized_events = [e.serialize() for e in events]
    event_idx = EventPresenter.select_event(serialized_events)
    selected_event = events[event_idx]
    event_infos = EventPresenter.ask_event_inputs()
    updated = selected_event.update(**event_infos)
    if updated:
      EventPresenter.confirm('Successfully updated.')
    
    else:
      EventPresenter.confirm('Something went Wrong...')





