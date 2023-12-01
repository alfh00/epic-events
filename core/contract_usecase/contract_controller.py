from common.database import Contract, Client
from .contract_presenter import ContractPresenter
from ..client_usecase.client_presenter import ClientPresenter

from authentication.user_context import UserContext

from datetime import datetime

class ContractController:

    def list_contracts():
        contracts = Contract.list_all()
        serialized_contracts = [contract.serialize() for contract in contracts]
        return ContractPresenter.display_contracts(serialized_contracts)

    def create_contract():
        clients = Client.list_all()
        serialized_clients = [client.serialize() for client in clients]
        client_idx = ClientPresenter.select_client(serialized_clients)
        client_id = clients[client_idx].client_id
        contract_infos = ContractPresenter.ask_for_contract_inputs()

        try:
            new_contract = Contract.create(
                client_id=client_id,
                total_amount=contract_infos['total_amount'],
                paid_amount=contract_infos['paid_amount'],
                is_signed=contract_infos['is_signed'],
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            if new_contract:
                ContractPresenter.confirm('Contract created. Press any key to continue...')
        except Exception:
            ContractPresenter.confirm('something went wrong while creating the contract')


    def update_contract():
        user_context = UserContext()
        auth_user = user_context.get_current_user()
        if auth_user['department']['name'] == 'Gestion':
            contracts = Contract.list_all()
        else:
            contracts = Contract.filter_by_keyword(commercial_employee_id=auth_user['employee_id'])
        
        serialized_contracts = [contract.serialize() for contract in contracts]
        contract_idx = ContractPresenter.select_contact(serialized_contracts)
        if contract_idx is None: return
        selected_contract = contracts[contract_idx]
        updated_info = ContractPresenter.ask_for_contract_inputs()
        try:
            updated_contract = selected_contract.update(**updated_info)
            if updated_contract:
                ContractPresenter.confirm('Contract has been updated.')
        except Exception:
            ContractPresenter.confirm('Something went wrong when updating.')

    def filter_contract():
        choice = ContractPresenter.ask_what_to_filter()
        if choice == '1':
            contracts = Contract.get_all_unpaid_contracts()
        elif choice == '2':
            contracts = Contract.get_all_unsigned_contracts()

        return ContractPresenter.display_contracts([c.serialize() for c in contracts])
    

    def delete_contract():
        contracts = Contract.list_all()
        serialized_contracts = [contract.serialize() for contract in contracts]
        contract_idx = ContractPresenter.select_contact(serialized_contracts)
        if contract_idx:
            try:
                selected_contract = contracts[contract_idx]
                is_contract_deleted = selected_contract.delete()
                if is_contract_deleted:
                    ContractPresenter.confirm('Contract deleted successfully.')
                else:
                    ContractPresenter.confirm('Something went wrong while deletion.')
            except Exception:
                ContractPresenter.confirm('Something went wrong while deletion.')

        else: return


