"""
This module is used to insert csv file to the database
"""

import pandas as pd
from models import * 
from utils import create_list_of_data

#### MAIN ####
# Import csv file for students' data
df = pd.read_csv(r'/home/khanh/Documents/capstone-hub/backend/M22_Capstone_descriptions.csv')

# Logins model
logins_cols = ["id", "public_id", "email"]
logins_data_cols = ["id", "id","email"]
logins_default_cols = ["password"]
logins_default_vals = ["Minerva22"]
logins_to_add = create_list_of_data(\
    data=df,\
    data_cols=logins_data_cols,\
    model_cols=logins_cols,\
    default_cols=logins_default_cols,\
    default_vals=logins_default_vals\
    )

# Users model
users_cols = ["id", "login_id", "name",\
            "primary_major", "secondary_major",\
            "primary_concentration", "secondary_concentration",\
            "special_concentration", "minor", "minor_concentration"]
users_data_cols = ["id", "id", "name",\
                "primary_major", "second_major",\
                "primary_concentration", "second_concentration",\
                "special_concentration", "minor", "minor_concentration"]
users_default_cols = ["class_year"]
users_default_vals = [2022]
users_to_add = create_list_of_data(\
    data=df,\
    data_cols=users_data_cols,\
    model_cols=users_cols,\
    default_cols=users_default_cols,\
    default_vals=users_default_vals\
    )

print(users_to_add[:1])
print(len(users_to_add))


# Projects model
projects_cols = ["id", "user_id", "title", "abstract",\
                "keywords", "feature", "hsr_review", "skills",\
                "los", "custom_los", "advisor", "skills_offering",\
                "skills_requesting", "location", "last_updated"]
projects_data_cols = ["id", "id", "title", "abstract",\
                "keywords", "features", "hsr_status", "skills",\
                "los", "custom_los", "advisor", "skills_offering",\
                "skills_requesting", "location", "timestamp"]
projects_to_add = create_list_of_data(\
    data=df,\
    data_cols=projects_data_cols,\
    model_cols=projects_cols,\
    )


def insert_data():
    """To insert data"""
    # import sqlite3

    # db = sqlite3.connect("database.db")
    # cur = db.cursor()


    # Create application context to add data to the database
    from app import create_app
    my_app = create_app()
    my_app.app_context().push()

    # List of keys with (list_of_data, model) to iterate
    keys = [(logins_to_add, Login), (users_to_add, User), (projects_to_add, Project)]
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