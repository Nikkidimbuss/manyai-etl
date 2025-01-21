from pony import orm
from pony.orm import Required, Optional, Set, PrimaryKey
from datetime import datetime

db = orm.Database()

class ManyAIEmployee(db.Entity):
    _table_ = 'many_ai_employees'
    employee_id = PrimaryKey(int)
    
    # fields from employees.csv
    first_name = Optional(str)
    last_name = Optional(str)
    role = Optional(str)
    department = Optional(str)
    age = Optional(int)
    retired = Optional(bool)
    dependants = Optional(str)
    marital_status = Optional(str)
    
    # fields from employees_salaries.json
    salary = Optional(float)
    pension = Optional(float)
    commute_distance = Optional(float)

    # fields from employees_vehicles.xml
    registration_number = Optional(str)
    vehicle_make = Optional(str)
    vehicle_model = Optional(str)
    vehicle_year = Optional(str)

    # Prompt communication
    prompts = Set('ManyAIPrompt')

class ManyAICustomer(db.Entity):
    _table_ = 'many_ai_customers'
    customer_id = PrimaryKey(int, auto=True)

    # fields from customers.csv
    customer_type = Optional(str)
    first_name = Optional(str)
    last_name = Optional(str)
    company_name = Optional(str)
    email = Optional(str)
    phone_number = Optional(str)
    dob = Optional(str)
    sex = Optional(str)

    # fields from customers_subscriptions.json
    subscription_type = Optional(str)

    # fields from customers_billing.xml
    payment_method = Optional(str)
    street = Optional(str)
    city = Optional(str)
    postcode = Optional(str)

class ManyAIPrompt(db.Entity):
    _table_ = 'many_ai_prompts'
    prompt_id = PrimaryKey(int, auto=True)
    employee = Required(ManyAIEmployee)
    timestamp = Required(datetime)
    text = Required(str, max_len=1000)
