import os
from dotenv import load_dotenv
import yaml
import shutil
from pyprojroot import here
import chromadb
from langchain.chat_models import ChatOpenAI
print("Environment variables are loaded:", load_dotenv())


class LoadConfig:

    def __init__(self):
        
        with open(here('configs/config.yaml'),'r') as f:

            app_config=yaml.load(f,Loader=yaml.FullLoader)


        self.load_directories(app_config=app_config)
        self.load_llm_config(app_config=app_config)
        self.load_openai_models()
        self.load_chroma_client()
        self.load_rag_config(app_config=app_config)


    def load_directories(self,app_config):

            self.stored_csv_xlsx_directory = here(app_config["directories"]["stored_csv_xlsx_directory"])
            self.sqldb_directory = here(app_config["directories"]["sqldb_directory"])
            self.uploaded_files_sqldb_directory = here(app_config["directories"]["uploaded_files_sqldb_directory"])
            self.stored_csv_xlsx_sqldb_directory = here(app_config["directories"]["stored_csv_xlsx_sqldb_directory"])
            self.persist_directory = app_config["directories"]["persist_directory"]


        
    
    def load_llm_config(self,app_config):
         

         self.model_name=app_config['llm_config']['model_name']
         self.agent_llm_system_role=app_config['llm_config']['agent_llm_system_role']
         self.temperature=app_config['llm_config']['temperature']
        #  self.embedding_model_name=


    def load_openai_models(self):
         
        openai_key=os.environ['OPENAI_API_KEY']
        langchain_llm = ChatOpenAI(
        model=self.model_name,
        temperature=self.temperature,
        openai_api_key=openai_key)


    def load_chroma_client(self):
         

         self.chroma_client=chromadb.PersistentClient(
              
              path=self.persist_directory
         )


    def load_rag_config(self,app_config):
         
         self.collection_name=app_config['rag_config']['collection_name']
         self.top_k=app_config['rag_config']['top_k']


    def remove_directory(self, directory_path: str):
        """
        Removes the specified directory.

        Parameters:
            directory_path (str): The path of the directory to be removed.

        Raises:
            OSError: If an error occurs during the directory removal process.

        Returns:
            None
        """
        if os.path.exists(directory_path):
            try:
                shutil.rmtree(directory_path)
                print(
                    f"The directory '{directory_path}' has been successfully removed.")
            except OSError as e:
                print(f"Error: {e}")
        else:
            print(f"The directory '{directory_path}' does not exist.")
    