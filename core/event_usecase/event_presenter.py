from datetime import datetime
from dateutil import parser

class EventPresenter:
    @staticmethod
    def display_events(events):
        if not events:
            return input("No Events to display. press any key to be back")
         
        column_widths = {
            
            "Client": 12,
            "Supp Employee": 15,
            "Total Amount": 13,
            "Start Date": 18,
            "End Date": 18,
            "Location": 14,
            "Attendees": 14,
        }

        # Print headers
        headers = ["Client", "Supp Employee", "Start Date", "End Date", "Location", "Attendees"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for event in events:
            data = [
                event['contract']['client']['client_contact']['full_name'],
                event['support_employee']['contact']['full_name'],
                event['start_date'],
                event['end_date'],
                event['location'],
                str(event['attendees']),
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)
            print('-Note->>', event['note'])

        key = input('\n\nPress any key to continue...')


    @staticmethod
    def validate_date(input_date):
        try:
            parsed_date = parser.parse(input_date)
            return parsed_date
        except ValueError:
            print("Invalid date format. Please enter a valid date.")
            return None

    @staticmethod
    def ask_event_inputs():
        while True:
            start_date_str = input("Enter Start Date (YYYY-MM-DD HH:MM): ")
            start_date = EventPresenter.validate_date(start_date_str)

            end_date_str = input("Enter End Date (YYYY-MM-DD HH:MM): ")
            end_date = EventPresenter.validate_date(end_date_str)

            location = input("Enter Location: ")

            attendees_str = input("Enter Number of Attendees: ")
            try:
                attendees = int(attendees_str)
            except ValueError:
                print("Invalid input. Number of attendees should be an integer.")
                continue

            note = input("Enter Note: ")

            if start_date and end_date and location and attendees is not None:
                return {
                    'start_date': start_date,
                    'end_date': end_date,
                    'location': location,
                    'attendees': attendees,
                    'note': note,
                }
            else:
                print("Invalid inputs. Please provide valid values for all fields.")

    @staticmethod
    def select_event(events):
        if not events:
            return input("No Events to display. press any key to be back")
         
        column_widths = {
            "N°":3,
            "Client": 12,
            "Supp Employee": 15,
            "Total Amount": 13,
            "Start Date": 18,
            "End Date": 18,
            "Location": 14,
            "Attendees": 14,
        }

        # Print headers
        headers = ["N°","Client", "Supp Employee", "Start Date", "End Date", "Location", "Attendees"]
        header_line = "|".join(f"{header.center(column_widths[header])}" for header in headers)
        print(header_line)
        print("-" * len(header_line))

        # Print data
        for idx, event in enumerate(events, start=1):
            data = [
                str(idx),
                event['contract']['client']['client_contact']['full_name'],
                event['support_employee']['contact']['full_name'],
                event['start_date'],
                event['end_date'],
                event['location'],
                str(event['attendees']),
            ]
            data_line = "|".join(f"{item.ljust(column_widths[headers[i]])}" for i, item in enumerate(data))
            print(data_line)
            print('-Note->>', event['note'])

        while True:
            try:
                selected_index = int(input('\n\nEnter contract"s number to select (0 to cancel): '))
                if 0 <= selected_index <= len(events):
                    return selected_index - 1 if selected_index > 0 else None
                else:
                    print("Invalid selection. Please enter a number within the valid range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    def confirm(message):
       input(message + '\nPress Enter to continue...')