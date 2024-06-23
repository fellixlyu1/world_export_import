import pandas as pd
from sqlalchemy import create_engine


# The 'csv_to_dataframe' method uses the csv file from the 'csv_to_db' folder and turns it into a dataframe
# using the functions from the pandas library.
def csv_to_dataframe(csv_file):
    global_exp_imp_data = pd.read_csv(csv_file)
    return global_exp_imp_data


# The 'dataframe_to_sql' method uses the csv file from the 'csv_to_db' folder and creates a SQLite database
# named after the csv file provided. Using the method above, 'csv_to_dataframe', we use the 'to_sql()' function
# to establish a table named 'global_business_data'. The user will need to provide the database name and table
# name as arguments for the method's parameters.
def dataframe_to_sql(csv_file, db_name, table_name):
    df = csv_to_dataframe(csv_file)

    db_uri = f'sqlite:///{db_name}.db'
    engine = create_engine(db_uri, echo=False)

    df.to_sql(f'{table_name}', con=engine)


# For this specific dataset, we'll use the variable 'csv_path' to act as the 'csv_file' arguments for the methods
# in this file. If you wish to use this file and its methods, you'll have to change the variable and a csv file
# in the 'csv_to_db' folder. Once you've done that, you'll have to edit the variable and put the name of your
# csv file in between the double quotations. In between the single quotations in the 'dataframe_to_sql()' method,
# you'll have to edit the names of the database and table.
csv_path = "world_export_data.csv"
dataframe_to_sql(csv_path, 'global_imp_exp', 'global_business_data')
