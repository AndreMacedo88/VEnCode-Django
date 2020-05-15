import argparse
import glob
import os
import pandas as pd


def main(directory):
    file_names = getting_files_in_dir(directory)
    for file in file_names:
        file_data = pd.read_csv(file, sep=";", index_col=0, engine="python")
        file_data.to_sql()


def getting_files_in_dir(directory):
    directory = os.path.join(directory, "*.csv")
    file_names = list()
    for name in glob.glob(directory):
        file_names.append(name)
    return file_names


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
        This script will import all the files ending in .csv to the project's postgres database. 
        """)
    parser.add_argument("directory", help="directory with the CSV files to upload to DB")
    args = parser.parse_args()
    DIR = args.directory

    main(DIR)
