import argparse
import glob
import os
import sys
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.insert(0, str(root))
from VEnCode_Django.settings.base import DATABASES


def main(directory, behaviour):
    file_names = getting_files_in_dir(directory)
    for file in file_names:
        file_data = pd.read_csv(file, sep=";", index_col=0, engine="python")
        engine = get_engine()
        db_name, file_extension = os.path.splitext(os.path.basename(file))
        file_data.to_sql(db_name, engine, if_exists=behaviour, index=True)


def getting_files_in_dir(directory):
    directory = os.path.join(directory, "*.csv")
    file_names = list()
    for name in glob.glob(directory):
        file_names.append(name)
    return file_names


def get_engine():
    db_connection_url = "postgresql://{}:{}@{}:{}/{}".format(
        DATABASES['default']['USER'],
        DATABASES['default']['PASSWORD'],
        DATABASES['default']['HOST'],
        DATABASES['default']['PORT'],
        DATABASES['default']['NAME'],
    )
    return create_engine(db_connection_url, paramstyle='format')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
        This script will import all the files ending in .csv to the project's postgres database as Tables. 
        """)
    parser.add_argument("directory", help="Directory with the CSV files to upload to DB")
    parser.add_argument("-b", "--behaviour", help="""
    Behaviour when a table with the same name already exists. 
    "fail" raises a ValueError. 
    "replace" drop the table before inserting new values.
    "append" insert new values to the existing table.
    """, default="fail")
    args = parser.parse_args()
    DIR = args.directory
    BEHAVIOUR = args.behaviour
    main(DIR, BEHAVIOUR)
