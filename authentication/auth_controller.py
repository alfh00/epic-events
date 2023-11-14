import bcrypt

from common.database import Employee, Contact, Department

class AuthenticationController:
  def register(self, registration_data, department):
    departments = Department.list_all()
    if registration_data['password'] == registration_data['confirmed_password']:

      password = registration_data['password']

      hashed_password = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt()) 

      try:
        new_contact = Contact.create(
                    full_name=registration_data['full_name'],
                    email=registration_data['email'],
                    phone_number=registration_data['phone']
                )

        # Create a new Employee and associate with the Contact and Department
        new_employee = Employee.create(
            username=registration_data['username'],
            password=hashed_password.decode('utf-8'),
            contact_id=new_contact.contact_id,
            department_id=department.department_id
            
        )
        
      except:
        pass
    

  def login(self, username, password):

    if username and password:
      user = Employee.read(username=username)
      
      if user:
        if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(user.password, 'utf-8')):
          # del user['password']
          return user.serialize()
        else:
          return
      else:
        print('user not found')


  def get_departments(self):
    return Department.list_all()
