import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, func, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, joinedload
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

load_dotenv()  # Load environment variables from .env file

db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Create a SQLAlchemy engine
engine = create_engine(f"postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()



# Define a metaclass for Entity
class EntityMeta(DeclarativeMeta):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        #class-level session
        new_cls._session = session
        return new_cls

# Define the base Entity class
Base = declarative_base(metaclass=EntityMeta)

class Entity(Base):
    __abstract__ = True

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        cls._session.add(obj)
        cls._session.commit()
        return obj

    @classmethod
    def read(cls, **kwargs):
        if not kwargs:
            return None

        query = cls._session.query(cls)
        
        for attribute, value in kwargs.items():
            if hasattr(cls, attribute):
                filter_expr = getattr(cls, attribute) == value
                query = query.filter(filter_expr)
            else:
                raise AttributeError(f"{cls.__name__} has no attribute '{attribute}'")

        return query.first()


    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key != 'employee_id':  # Exclude updating the ID
                setattr(self, key, value)
        self._session.commit()
        return self
    
    @classmethod
    def filter_by_keyword(cls, **kwargs):
        query = cls._session.query(cls)

        for attribute, value in kwargs.items():
            if hasattr(cls, attribute):
                filter_expr = getattr(cls, attribute) == value
                query = query.filter(filter_expr)
            else:
                raise AttributeError(f"{cls.__name__} has no attribute '{attribute}'")

        return query.all()

    
    def delete(self):
            try:
                self._session.delete(self)
                self._session.commit()
                return True
            except Exception:
                return False
    
    @classmethod
    def list_all(cls):
        return cls._session.query(cls).all()

# Define multiple entities using the base Entity class

class Contact(Entity):
    __tablename__ = "Contacts"

    contact_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)


    def serialize(self):
        return {
            'full_name': self.full_name,
            'email': self.email,
            'phone': self.phone_number,
        }

class Client(Entity):
    __tablename__ = "Clients"

    client_id = Column(Integer, primary_key=True)
    client_contact_id = Column(Integer, ForeignKey("Contacts.contact_id", ondelete="CASCADE"))
    commercial_employee_id = Column(Integer, ForeignKey("Employees.employee_id"))
    company_name = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def serialize(self):
        return {
            'client_contact': Contact.read(contact_id=self.client_contact_id).serialize(),
            'commercial_employee': Employee.read(employee_id=self.commercial_employee_id).serialize(),
            'company_name': self.company_name,
            'created_at': self.created_at.strftime('%d-%m-%y %H:%M'), 
            'updated_at': self.updated_at.strftime('%d-%m-%y %H:%M')
        }


class Event(Entity):
    __tablename__ = "Events"

    event_id = Column(Integer, primary_key=True)
    contract_id = Column(Integer)
    support_employee_id = Column(Integer, ForeignKey("Employees.employee_id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String)
    attendees = Column(Integer)
    note = Column(String)

    def serialize(self):

        return {
            'event_id': self.event_id,
            'contract': Contract.read(contract_id=self.contract_id).serialize(),
            'support_employee': Employee.read(employee_id=self.support_employee_id).serialize(),
            'start_date': self.start_date.strftime('%d-%m-%y %H:%M') if self.start_date else None,
            'end_date': self.end_date.strftime('%d-%m-%y %H:%M') if self.end_date else None,
            'location': self.location,
            'attendees': self.attendees,
            'note': self.note,
        }


class Contract(Entity):
    __tablename__ = "Contracts"

    contract_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("Clients.client_id"))
    commercial_employee_id = Column(Integer, ForeignKey("Employees.employee_id"))
    total_amount = Column(Integer)
    paid_amount = Column(Integer)
    is_signed = Column(Boolean)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def serialize(self):
        return {
        'contract_id': self.contract_id,
        'client': Client.read(client_id=self.client_id).serialize(),
        'total_amount': str(self.total_amount),
        'paid_amount': str(self.paid_amount),
        'is_signed': str(self.is_signed),
        'created_at': self.created_at.strftime('%d-%m-%y %H:%M'),
        'updated_at': self.updated_at.strftime('%d-%m-%y %H:%M'),
    }



class Department(Entity):
    __tablename__ = "Departments"

    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)

    employees = relationship("Employee", back_populates="department")
    def serialize(self):
        return {
            'department_id': self.department_id,
            'name': self.department_name    
        }

class Employee(Entity):
    __tablename__ = "Employees"

    employee_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    department_id = Column(Integer, ForeignKey("Departments.department_id"))
    contact_id = Column(Integer, ForeignKey("Contacts.contact_id", ondelete="CASCADE"))

    department = relationship("Department", back_populates="employees")
    contact = relationship('Contact', backref='Employee', cascade='all, delete')

    @classmethod
    def read(cls, **kwargs):
        if not kwargs:
            return None

        query = cls._session.query(cls).options(
            joinedload(cls.department),
            joinedload(cls.contact)  
        )

        for attribute, value in kwargs.items():
            if hasattr(cls, attribute):
                filter_expr = getattr(cls, attribute) == value
                query = query.filter(filter_expr)
            else:
                raise AttributeError(f"{cls.__name__} has no attribute '{attribute}'")

        return query.first()
        
    def serialize(self):
        return {
            'employee_id': self.employee_id,
            'username': self.username,
            'contact': self.contact.serialize() if self.contact else None,
            'department': self.department.serialize() if self.department else None
        }
    
    @classmethod
    def filter_by_department(cls, department_name):
        if not department_name:
            return []

        query = cls._session.query(cls).options(
            joinedload(cls.department),
            joinedload(cls.contact)
        )

        query = query.join(Department).filter(Department.department_name == department_name)

        return query.all()

# Create the database structure
Base.metadata.create_all(engine)
