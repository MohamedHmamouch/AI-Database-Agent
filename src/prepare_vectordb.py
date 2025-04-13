from utils.prepare_vectordb_from_tab_data import PrepareVectorDBFromTabularData
from pyprojroot import here

if __name__=="__main__":
    titanic_dir = here("data/uploaded_data/titanic.csv")
    data_prep_instance = PrepareVectorDBFromTabularData(file_directory=titanic_dir)
    data_prep_instance.run_pipeline()