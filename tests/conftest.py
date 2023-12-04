import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from dotenv import load_dotenv
load_dotenv()

import pytest
from common.database import Base, engine

# Import necessary modules and classes
from common.database import session, Contact, Client, Event, Contract, Department, Employee

@pytest.fixture(autouse=True)
def check_testing_variable():
    testing = os.getenv("TESTING") == '1'

    if not testing:
        pytest.skip("Skipping tests because TESTING variable is not set to '1' in the .env file.")


@pytest.fixture(scope='session')
def setup_test_database(request):
    with engine.connect() as connection:
        Base.metadata.reflect(bind=engine)
        Base.metadata.drop_all(connection)
    # Setup code
    # Create dummy data for Contact
    contact1 = Contact.create(full_name='John Doe', email='john@example.com', phone_number='123-456-7890')
    contact2 = Contact.create(full_name='Jane Doe', email='jane@example.com', phone_number='987-654-3210')
    contact3 = Contact.create(full_name='Marc Doe', email='marc@example.com', phone_number='987-654-6548')

    # Create dummy data for Department
    department1 = Department.create(department_name='Gestion')
    department2 = Department.create(department_name='Commercial')
    department3 = Department.create(department_name='Support')

    # Create dummy data for Employee
    employee1 = Employee.create(username='emp1', contact_id=contact1.contact_id, department_id=department1.department_id)
    employee2 = Employee.create(username='emp2', contact_id=contact2.contact_id, department_id=department2.department_id)
    employee3 = Employee.create(username='emp_to_delete', contact_id=contact3.contact_id, department_id=department1.department_id)

    # Create dummy data for Client
    client1 = Client.create(
        client_contact_id=contact1.contact_id,
        commercial_employee_id=employee1.employee_id,
        company_name='ABC Corp'
    )

    # Create dummy data for Event
    event1 = Event.create(
        contract_id=1,
        support_employee_id=employee2.employee_id,
        start_date='2023-01-01 10:00:00',
        end_date='2023-01-01 12:00:00',
        location='Conference Room',
        attendees=50,
        note='Some notes about the event'
    )

    # Create dummy data for Contract
    contract1 = Contract.create(
        client_id=1,
        commercial_employee_id=employee1.employee_id,
        total_amount=10000,
        paid_amount=5000,
        is_signed=True
    )


    # Commit the changes to the database
    session.commit()
    request.addfinalizer(teardown_test_database)

    # Yielding so that the tests can run
    yield

def teardown_test_database():
    # Teardown code
    session.commit()
    Base.metadata.drop_all(bind=engine)