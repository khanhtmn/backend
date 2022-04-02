"""
This module is used to import M20 csv file data to the database
"""

import pandas as pd
from werkzeug.security import generate_password_hash
from datetime import datetime

from models import *
from utils import create_list_of_data


#### MAIN ####
# Import csv file for students' data
# df = pd.read_csv(r'/home/khanh/Documents/capstone-hub-backend/csv_files/M20_Student_Capstone_List.csv')
df = pd.read_csv(r'/app/csv_files/M20_Student_Capstone_List.csv')

college_conversion = {
    "CS": "Computational Sciences",
    "BZ": "Business",
    "NS": "Natural Sciences",
    "AH": "Arts & Humanities",
    "SS": "Social Sciences",
    "N/A": ""
}

hashed_password = generate_password_hash("Minerva20", method='sha256')

# Create email, major, minor
names = []
emails = []
primary_majors = []
second_majors = []
minors = []

try:
    for index, row in df.iterrows():
        first_name = row["first_name"]
        last_name = row["last_name"]
        name = first_name + " " + last_name

        first_email = "".join(first_name.lower().split())
        last_email = "".join(last_name.lower().split())
        email = first_email + "_" + last_email + "@uni.minerva.edu"

        major = row["major"].split("/")
        major = [x.upper() for x in major]
        major = [x.strip() for x in major]
        first_major = college_conversion[major[0]]
        second_major = ""
        if len(major) > 1:    
            second_major = college_conversion[major[1]]

        minor = ""
        if type(row["minor"]) != type(float("nan")):
            minor = row["minor"].split("/")
            minor = [x.upper() for x in minor]
            minor = [x.strip() for x in minor]
            if len(minor) > 1:
                minor = college_conversion[minor[0]] + college_conversion[minor[1]]
            else:
                minor = college_conversion[minor[0]]

        names.append(name)
        emails.append(email)
        primary_majors.append(first_major)
        second_majors.append(second_major)
        minors.append(minor)

except Exception as e:
    print("Something happened in transforming data")


df["name"] = names
df["email"] = emails
df["primary_major"] = primary_majors
df["second_major"] = second_majors
df["minor"] = minors


# Function to create lists of data to inject to Models
"""
Take data and put to dictionary
"""


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
            "primary_major", "secondary_major", "minor",\
            "project_link", "title", "abstract", "advisor"]

# Columns from CSV file
user_projects_data_cols = ["id", "id", "name",\
            "primary_major", "second_major", "minor",\
            "project_link", "title", "abstract", "advisor"]

# Default columns and their default values
user_projects_default_cols = ["class_year"]
user_projects_default_vals = [2020]

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