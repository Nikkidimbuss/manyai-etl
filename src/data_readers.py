import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime

def read_employees_xml():
    vehicle_data = {}
    tree = ET.parse('employees_vehicles.xml')
    root = tree.getroot()

    for employee in root.findall('.//Employee'):
        emp_data = {
            'first_name': employee.get('FirstName'),
            'last_name': employee.get('SecondName'),
            'department': employee.get('Department'),
            'age': employee.get('Age')
        }

        vehicle = employee.find('.//VehicleInfo')
        if vehicle is not None:
            emp_data['registration'] = vehicle.findtext('RegistrationNumber')
            emp_data['make'] = vehicle.findtext('Make')
            emp_data['model'] = vehicle.findtext('Model')
            emp_data['year'] = vehicle.findtext('Year')

        key = f"{emp_data['first_name']}_{emp_data['last_name']}"
        vehicle_data[key] = emp_data
    
    return vehicle_data

def read_customers_xml():
    billing_data = {}
    tree = ET.parse('customers_billing.xml')
    root = tree.getroot()

    for customer in root.findall('.//Customer'):
        cust_data = {
            'first_name': customer.findtext('FirstName'),
            'last_name': customer.findtext('LastName'),
            'phone_no': customer.findtext('PhoneNo'),
            'payment_method': customer.findtext('PaymentMethod')
        }

        billing = customer.find('BillingAddress')
        if billing is not None:
            cust_data['street'] = billing.findtext('Street')
            cust_data['city'] = billing.findtext('City')
            cust_data['postcode'] = billing.findtext('Postcode')

        key = f"{cust_data['first_name']}_{cust_data['last_name']}"
        billing_data[key] = cust_data
    
    return billing_data

def read_employees_csv():
    employees_data = {}
    with open('employees.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees_data[row['employee_id']] = row
    return employees_data

def read_customers_csv():
    customers_data = {}
    with open('customers.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = f"{row['first_name']}_{row['last_name']}"
            customers_data[key] = row
    return customers_data

def read_salaries():
    with open('employees_salaries.json', 'r') as file:
        return json.load(file)

def read_prompts():
    prompts_data = []
    current_id = None
    current_timestamp = None

    with open('flagged_prompts.txt', 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('Employee ID:'):
                current_id = line.split(':')[1].strip()
            elif line.startswith('Timestamp:'):
                timestamp_str = line.split(':', 1)[1].strip()
                current_timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
            elif line.startswith('Prompt:') and current_id and current_timestamp:
                prompt_text = line.split(':', 1)[1].strip()
                prompts_data.append({
                    'employee_id': current_id,
                    'timestamp': current_timestamp,
                    'text': prompt_text
                })
    
    return prompts_data
