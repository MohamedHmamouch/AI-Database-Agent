from utils.prepare_sqldb_from_tabular_data import PrepareSQLFromTabularData
from utils.LoadConfig import LoadConfig
config=LoadConfig()
if __name__=='__main__':

    preparation_sql_instance=PrepareSQLFromTabularData(config.stored_csv_xlsx_directory)

    preparation_sql_instance.run_pipeline()