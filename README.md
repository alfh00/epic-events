# Epic Events CRM

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [General Requirements](#general-requirements)
  - [Individual Needs: Management Team](#individual-needs-management-team)
  - [Individual Needs: Sales Team](#individual-needs-sales-team)
  - [Individual Needs: Support Team](#individual-needs-support-team)
- [Technical Requirements](#technical-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Epic Events is an event management company that specializes in organizing various events for its clients. To enhance its workflow, Epic Events aims to develop a Customer Relationship Management (CRM) software. The CRM software will facilitate the collection and processing of client and event data, improving communication across different departments within the company.

## Features

### General Requirements

- The application will be a command-line interface (CLI) application.
- Python 3 (version 3.9 or newer) will be used for development.
- SQL injection prevention is a priority.
- The principle of least privilege will be implemented when granting data access to users.
- Effective logging using Sentry for exceptions and errors.

### Individual Needs: Management Team

- Create, update, and delete employees in the CRM system.
- Create and modify all contracts.
- Filter event display, e.g., display events without an associated support member.
- Modify events (associate a support team member with an event).

### Individual Needs: Sales Team

- Create clients (automatically associated with the sales team member).
- Update clients for whom they are responsible.
- Modify/update contracts of clients for whom they are responsible.
- Filter contract display, e.g., display unsigned or unpaid contracts.
- Create an event for a client who has signed a contract.

### Individual Needs: Support Team

- Filter event display, e.g., display only events assigned to them.
- Update events for which they are responsible.

## Technical Requirements

- Python 3 (version 3.9 or newer)
- SQLAlchemy for database operations
- Sentry for effective logging
- CLI implementation
- SQL injection prevention measures
- Principle of least privilege for data access

## Installation

1. Clone the repository: `git clone https://github.com/your-username/epic-events-crm.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Database Setup:
   You should have PostgreSQL installed

Before running the application, you need to set up the database. We use SQLAlchemy and Alembic for database migrations.

Alembic Migration
To create and apply database migrations, run the following commands:

    bash```
    alembic init alembic
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    This sets up Alembic and applies the initial migration to create the necessary database tables.
    ```

## Usage

1. Run the application: `python main.py`
2. Follow the on-screen instructions to navigate through the application.
3. A Menu shoul apprear on the Terminal, use the arrow to navigate.

### SQLAlchemy

We leverage SQLAlchemy as the ORM (Object-Relational Mapping) tool for interacting with our database. This allows us to work with the database using Python objects.

### Alembic

Alembic is used for database migrations. It helps manage changes to the database schema over time, making it easy to evolve the database along with the application.

### pytest

Our test suite is built using pytest. It ensures the reliability and correctness of our codebase through automated tests.
To run test:

    bash```
    pytest -s
    ```

dont forget the flag -s because we use 'capsys' for capturation printed data on the Terminal.

![coverage test](https://github.com/alfh00/epic-events/blob/main/db_schema/coverage.PNG?raw=true)


#### Other Dependencies

Other dependencies can be found in the requirements.txt file. We use these libraries to enhance various aspects of the application, from handling forms to managing user authentication like 'bcrypt' for password hashing.
