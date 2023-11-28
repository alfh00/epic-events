from common.database import Contract
from .contract_presenter import ContractPresenter

class ContractController:

    def list_contracts():
        contracts = Contract.list_all()
        return ContractPresenter.display_contracts(contracts)

    def create_contract():
        contract_inputs = ContractPresenter.ask_for_contract_inputs()
        # new_contract = Contract.create(
        #     client_id=client_id,
        #     commercial_employee_id=commercial_employee_id,
        #     total_amount=total_amount,
        #     paid_amount=paid_amount,
        #     is_signed=is_signed,
        # )

    # def update_contract():
    #     contract = Contract.read(session=self.session, contract_id=contract_id)
    #     if contract:
    #         contract.update(**kwargs)
    #         return contract
    #     else:
    #         return None

    # def delete_contract(self, contract_id):
    #     contract = Contract.read(session=self.session, contract_id=contract_id)
    #     if contract:
    #         contract.delete()
    #         return True
    #     else:
    #         return False


