from pony import orm
from models import db, ManyAIEmployee, ManyAICustomer, ManyAIPrompt
from data_readers import (
    read_employees_csv,
    read_employees_xml,
    read_customers_csv,
    read_customers_xml,
    read_salaries,
    read_prompts
)
import json

def setup_database():
    db.bind(
        provider='mysql',
        host='europa.ashley.work',
        user='student_bi77cc',
        password='iE93F2@8EhM@1zhD&u9M@K',
        db='student_bi77cc'
    )
    db.generate_mapping(create_tables=True)

@orm.db_session
def load_all_data():
    # Load data from all sources
    employees_csv = read_employees_csv()
    employees_xml = read_employees_xml()
    customers_csv = read_customers_csv()
    customers_xml = read_customers_xml()
    salaries = read_salaries()
    prompts = read_prompts()
    
    employees = {}

    # Processing of salary data
    for salary_info in salaries:
        emp_id = salary_info['employee_id']
        emp_csv = employees_csv.get(str(emp_id), {})

        name_key = f"{emp_csv.get('first_name')}_{emp_csv.get('last_name')}"
        emp_xml = employees_xml.get(name_key, {})

        employee = ManyAIEmployee(
            employee_id=emp_id,
            first_name=emp_csv.get('first_name'),
            last_name=emp_csv.get('last_name'),
            role=emp_csv.get('role'),
            department=emp_csv.get('department'),
            age=int(emp_csv['age']) if emp_csv.get('age', '').isdigit() else None,
            retired=emp_csv.get('retired') == 'True',
            dependants=emp_csv.get('dependants'),
            marital_status=emp_csv.get('marital_status'),
            salary=salary_info.get('salary'),
            pension=salary_info.get('pension'),
            commute_distance=salary_info.get('commute_distance'),
            registration_number=emp_xml.get('registration', ''),
            vehicle_make=emp_xml.get('make', ''),
            vehicle_model=emp_xml.get('model', ''),
            vehicle_year=emp_xml.get('year', '')
        )
        employees[str(emp_id)] = employee

    # Process prompts
    for prompt_info in prompts:
        emp_id = prompt_info['employee_id']
        if emp_id in employees:
            ManyAIPrompt(
                employee=employees[emp_id],
                timestamp=prompt_info['timestamp'],
                text=prompt_info['text'][:1000]
            )

    # Process customers
    with open('customers_subscriptions.json', 'r') as file:
        customers_json = json.load(file)
        
        for customer in customers_json:
            key = f"{customer['first_name']}_{customer['last_name']}"
            csv_data = customers_csv.get(key, {})
            xml_data = customers_xml.get(key, {})

            ManyAICustomer(
                customer_type=csv_data.get('customer_type', customer['customer_type']),
                first_name=customer['first_name'],
                last_name=customer['last_name'],
                company_name=customer['company_name'],
                email=csv_data.get('email'),
                phone_number=csv_data.get('phone_number'),
                dob=csv_data.get('dob'),
                sex=csv_data.get('sex'),
                subscription_type=customer['subscription_type'],
                payment_method=xml_data.get('payment_method'),
                street=xml_data.get('street'),
                city=xml_data.get('city'),
                postcode=xml_data.get('postcode')
            )
