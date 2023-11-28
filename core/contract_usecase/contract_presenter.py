

class ContractPresenter:
    @staticmethod
    def display_contracts(contracts):
        if not contracts:
            print("No Contracts to display.")
                    
        column_widths = {
            
            "Client": 12,
            "Com Employee": 18,
            "Total Amount": 22,
            "Paid Amount": 15,
            "Is Signed": 12,
            "Created": 12,
            "Updated": 12,
        }

        # Print headers
        headers = ["Client", "Com Employee", "Total Amount", "Paid Amount", "Is Signed", "Created", "Updated"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for contract in contracts:
            data = [
                contract['client']['company_name'],
                contract['commercial_employee']['full_name'],
                contract['total_amount'],
                contract['paid_amount'],
                contract['is_signed'],
                contract['created_at'],
                contract['updated_at'],
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)

        key = input('\n\nPress any key to continue...')

    @staticmethod
    def ask_for_contract_inputs():
      
    

      client_id = int(input("Enter Client ID: "))
      commercial_employee_id = int(input("Enter Commercial Employee ID: "))
      total_amount = int(input("Enter Total Amount: "))
      paid_amount = int(input("Enter Paid Amount: "))
      is_signed = input("Is the contract signed? (True/False): ").lower() == 'true'
