import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey
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
        # Add class-level session
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


    @classmethod
    def update(cls, id, **kwargs):
        obj = cls.read(id)
        if obj:
            for key, value in kwargs.items():
                setattr(obj, key, value)
            cls._session.commit()
        return obj

    @classmethod
    def delete(cls, id):
        obj = cls.read(id)
        if obj:
            cls._session.delete(obj)
            cls._session.commit()
    
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

class Client(Entity):
    __tablename__ = "Clients"

    client_id = Column(Integer, primary_key=True)
    client_contact_id = Column(Integer, ForeignKey("Contacts.contact_id"))
    commercial_employee_id = Column(Integer)
    company_name = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Event(Entity):
    __tablename__ = "Events"

    event_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("Clients.client_id"))
    contract_id = Column(Integer)
    event_contact_id = Column(Integer, ForeignKey("Contacts.contact_id"))
    support_employee_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String)
    attendees = Column(Integer)
    note = Column(String)

class Contract(Entity):
    __tablename__ = "Contracts"

    contract_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("Clients.client_id"))
    commercial_employee_id = Column(Integer)
    total_amount = Column(Integer)
    paid_amount = Column(Integer)
    created_at = Column(DateTime)
    is_signed = Column(Boolean)
    updated_at = Column(DateTime)


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

        query = cls._session.query(cls).options(joinedload(cls.department))

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
            'contact_id': self.contact_id,
            'department': self.department.serialize() if self.department else None
        }
    

# Create the database structure
Base.metadata.create_all(engine)