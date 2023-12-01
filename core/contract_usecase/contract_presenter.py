

class ContractPresenter:
    @staticmethod
    def display_contracts(contracts):
        if not contracts:
            return input("No Contracts to display. press any key to be back")
         
        column_widths = {
            
            "Client": 12,
            "Com Employee": 12,
            "Total Amount": 13,
            "Paid Amount": 13,
            "Is Signed": 12,
            "Created": 14,
            "Updated": 14,
        }

        # Print headers
        headers = ["Client", "Com Employee", "Total Amount", "Paid Amount", "Is Signed", "Created", "Updated"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for contract in contracts:
            data = [
                contract['client']['client_contact']['full_name'],
                contract['client']['commercial_employee']['contact']['full_name'],
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
      return {
      'total_amount' : int(input("Enter Total Amount: ")),
      'paid_amount' : int(input("Enter Paid Amount: ")),
      'is_signed' : input("Is the contract signed? (True/False): ").lower() == 'true'
      }

    def select_contact(contracts):
        if not contracts:
            return input("No Contracts to display. press any key to be back")
         
        column_widths = {
            "N°": 3,
            "Client": 12,
            "Com Employee": 12,
            "Total Amount": 13,
            "Paid Amount": 13,
            "Is Signed": 12,
            "Created": 14,
            "Updated": 14,
        }

        # Print headers
        headers = ["N°", "Client", "Com Employee", "Total Amount", "Paid Amount", "Is Signed", "Created", "Updated"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for idx, contract in enumerate(contracts, start=1):
            data = [
                str(idx),
                contract['client']['client_contact']['full_name'],
                contract['client']['commercial_employee']['contact']['full_name'],
                contract['total_amount'],
                contract['paid_amount'],
                contract['is_signed'],
                contract['created_at'],
                contract['updated_at'],
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)

        while True:
            try:
                selected_index = int(input('\n\nEnter contract"s number to select (0 to cancel): '))
                if 0 <= selected_index <= len(contracts):
                    return selected_index - 1 if selected_index > 0 else None
                else:
                    print("Invalid selection. Please enter a number within the valid range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def confirm(message):
        input(message + '\nPress Enter to continue...')