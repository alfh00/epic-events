from common.database import Client, Contact
from .client_presenter import ClientPresenter

from datetime import datetime

class ClientController:
  def list_clients():
    all_clients = Client.list_all()
    serialized_clients = []

    for client in all_clients:
        serialized_clients.append(client.serialize())
    ClientPresenter.Display_all_client(serialized_clients)

  def create_client():
    new_client_infos = ClientPresenter.ask_for_client_infos()
    client_contact = new_client_infos['client_contact']

    client_contact = Contact.create(**client_contact)
    client = Client.create(
      client_contact_id=client_contact.contact_id,
      company_name=new_client_infos['client_company_name'],
      commercial_employee_id=new_client_infos['commercial_empl'].employee_id,
      created_at=datetime.now(),
      updated_at=datetime.now(),
    )

  def update_client():
    all_clients = Client.list_all()
    serialized_clients = []

    for client in all_clients:
        serialized_clients.append(client.serialize())
    
    client_idx = ClientPresenter.select_client(serialized_clients)
    if client_idx is None: return

    selected_client = all_clients[client_idx]

    choice = ClientPresenter.ask_what_to_update()
    if choice == "1":
       updated_company_name = ClientPresenter.field_prompt(f'Enter a new company Name: ')
       selected_client.update(company_name=updated_company_name)
    elif choice == "2":
      updated_com_employee = ClientPresenter.select_com_employee()
      selected_client.update(commercial_employee_id=updated_com_employee.employee_id)
    elif choice == "3":
      serialized_contact = serialized_clients[client_idx]['client_contact']
      print(serialized_contact)
      full_name = ClientPresenter.field_prompt(
         f'New Client Full Name ({serialized_contact["full_name"]}): '
         )
      phone_number = ClientPresenter.field_prompt(
         f'New Client Phone Number({serialized_contact["phone"]}): '
         )
      email = ClientPresenter.field_prompt(
         f'New Client e-mail ({serialized_contact["email"]}): '
         )
      Contact.read(contact_id=selected_client.client_contact_id).update(
         full_name=full_name,
         phone_number=phone_number,
         email=email
         )

    elif choice == "4":
        print("Update canceled.")

  def delete_client():
    all_clients = Client.list_all()
    serialized_clients = [client.serialize() for client in all_clients]
    
    client_idx = ClientPresenter.select_client(serialized_clients)
    selected_client = all_clients[client_idx]
    selected_client.delete()
    client_contact = Contact.read(contact_id=selected_client.client_contact_id)
    client_contact.delete()
    