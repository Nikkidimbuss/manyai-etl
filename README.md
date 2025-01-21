# ManyAI ETL Process

## Description
This Python program performs extract, transform and load (ETL) operations of ManyAI company data from different sources (CSV, JSON, TXT, XML) into a single MySQL database using Pony ORM.

## Features
- Extract employee data from various file formats
- Process customer information
- Process AI query data
- Implement data validation and security measures
- Use PonyORM for database operations
- Include query validation for security

## Project Structure
```src/```
- ```main.py``` - Main entry point and program execution
- ```validator.py``` - Security validation for prompts
- ```models.py``` - Database models for employees, customers and prompts
- ```data_readers.py``` - Functions for reading different data sources
- ```etl_process.py``` - Main ETL process implementation

## Setup
1. Install requirements:
   ```bash
   pip install -r requirements.txt
