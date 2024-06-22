import pandas as pd
from sqlalchemy import create_engine


def csv_to_dataframe(csv_file):
    global_exp_imp_data = pd.read_csv(csv_file)
    return global_exp_imp_data


def dataframe_to_sql(csv_file):
    df = csv_to_dataframe(csv_file)

    db_uri = 'sqlite:///global_imp_exp.db'
    engine = create_engine(db_uri, echo=False)

    df.to_sql('global_business_data', con=engine)


csv_path = "world_export_data.csv"
dataframe_to_sql(csv_path)
