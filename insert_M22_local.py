"""
This module is used to insert csv file to the database
"""

import pandas as pd
from werkzeug.security import generate_password_hash

from models import * 
from utils import create_list_of_data

#### MAIN ####
# Import csv file for students' data
df = pd.read_csv(r'/home/khanh/Documents/capstone-hub-backend/csv_files/M22_Capstone_info_(fall_2021).csv')

hashed_password = generate_password_hash("Minerva22", method='sha256')

# Logins model
logins_cols = ["id", "public_id", "email"]
logins_data_cols = ["id", "id","email"]
logins_default_cols = ["password"]
logins_default_vals = [hashed_password]
logins_to_add = create_list_of_data(\
    data=df,\
    data_cols=logins_data_cols,\
    model_cols=logins_cols,\
    default_cols=logins_default_cols,\
    default_vals=logins_default_vals\
    )

# Columns in projects model
user_projects_cols = ["id", "user_id", "name",\
            "primary_major", "secondary_major",\
            "primary_concentration", "secondary_concentration",\
            "special_concentration", "minor", "minor_concentration",\
            "title", "abstract",\
            "keywords", "feature", "hsr_review", "skills",\
            "los", "custom_los", "advisor", "skills_offering",\
            "skills_requesting", "last_updated"]

# Columns from CSV file
user_projects_data_cols = ["id", "id", "name",\
            "primary_major", "second_major",\
            "primary_concentration", "second_concentration",\
            "special_concentration", "minor", "minor_concentration",\
            "title", "abstract",\
            "keywords", "features", "hsr_status", "skills",\
            "los", "custom_los", "advisor", "skills_offering",\
            "skills_requesting", "timestamp"]

# Default columns and their default values
user_projects_default_cols = ["class_year"]
user_projects_default_vals = [2022]

# Create list of data from all columns and values above
user_projects_to_add = create_list_of_data(\
    data=df,\
    data_cols=user_projects_data_cols,\
    model_cols=user_projects_cols,\
    default_cols=user_projects_default_cols,\
    default_vals=user_projects_default_vals\
    )


def insert_data():
    """To insert data generated above to the database"""

    # Create application context to add data to the database
    from app import create_app
    my_app = create_app()
    my_app.app_context().push()

    # List of keys with (list_of_data, model) to iterate
    keys = [(logins_to_add, Login), (user_projects_to_add, UserProject)]
    # Insert data
    for dict_to_add, table in keys:
        for dict_row in dict_to_add:
            try:
                stmt = table(**dict_row)
                db.session.add(stmt)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print(e)
                continue
            finally:
                db.session.close()

insert_data()
