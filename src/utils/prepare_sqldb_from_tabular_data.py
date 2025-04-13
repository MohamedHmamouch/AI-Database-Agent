import os 
import pandas as pd
from utils.LoadConfig import LoadConfig
from sqlalchemy import create_engine, inspect


class PrepareSQLFromTabularData:


    def __init__(self,files_dir):
        
        configs=LoadConfig()

        self.files_directory=files_dir

        self.file_dir_list=os.listdir(files_dir)
        db_path=configs.stored_csv_xlsx_sqldb_directory
        db_path=f"sqlite:///{db_path}"
        self.engine=create_engine(db_path)
        print("Number of csv files:",len(self.file_dir_list))



    def prepare_db(self):

        for file in self.file_dir_list:
            full_file_path = os.path.join(self.files_directory, file)
            file_name, file_extension = os.path.splitext(file)
            if file_extension == ".csv":
                df = pd.read_csv(full_file_path)
            elif file_extension == ".xlsx":
                df = pd.read_excel(full_file_path)
            else:
                raise ValueError("The selected file type is not supported")
            df.to_sql(file_name, self.engine, index=False)
        print("==============================")
        print("All csv files are saved into the sql database.")


    def _validate_db(self):
        """
        Private method to validate the tables stored in the SQL database.

        It prints out all available table names in the created SQLite database
        to confirm that the tables have been successfully created.
        """
        insp = inspect(self.engine)
        table_names = insp.get_table_names()
        print("==============================")
        print("Available table nasmes in created SQL DB:", table_names)
        print("==============================")

    def run_pipeline(self):
        """
        Public method to run the data import pipeline, which includes preparing the database
        and validating the created tables. It is the main entry point for converting files
        to SQL tables and confirming their creation.
        """
        self.prepare_db()
        self._validate_db()
