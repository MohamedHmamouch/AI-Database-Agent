from src.utils.load_config import *
from sqlalchemy import create_engine, inspect
# from load_config import *
import pandas as pd

def PrepareSQLFromTabularData():

    app_config,config_path=load_yaml_config()

    directories=load_directories(app_config=app_config)

    files_dir=directories['stored_csv_xlsx_directory']
    file_dir_list=os.listdir(files_dir)

    db_path=directories['stored_csv_xlsx_sqldb_directory']
    db_path=f"sqlite:///{db_path}"
    engine=create_engine(db_path)


    for file in file_dir_list:

        full_file_path=os.path.join(files_dir,file)
        file_name,file_extension=os.path.splitext(file)

        if file_extension=='.csv':

            df=pd.read_csv(full_file_path)

        elif file_extension=='.xslx':

            df=pd.read_excel(full_file_path)

        else:

            raise ValueError("The selected file type is not supported")
        
        df.to_sql(file_name,engine,index=False,if_exists='replace')

        insp=inspect(engine)
        table_names=insp.get_table_names()

        print("available table names in created sql db",table_names,"in",file_name)
        

if __name__=='__main__':

    PrepareSQLFromTabularData()

