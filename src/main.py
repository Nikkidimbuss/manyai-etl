import json
import csv
import xml.etree.ElementTree as ET
from datetime import datetime
from pony import orm
from pony.orm import Required, Optional, Set, PrimaryKey
import logging

logging.basicConfig(
    filename="prompt_security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)





from etl_process import setup_database, load_all_data

if __name__ == "__main__":
    try:
        print("Start of ETL process")
        setup_database()
        load_all_data()
        print("ETL process completed successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
