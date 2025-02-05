import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
import yaml



class LoadConfig:


    def __init__(self):

        self.config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "configs", "config.yaml"))

        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Config file not found at {self.config_path}")


        with open(self.config_path ) as f:

            app_config=yaml.load(f,Loader=yaml.FullLoader)

        
        self.load_directories(app_config=app_config)
        self.load_llm_configs(app_config=app_config)
        self.load_openai_models()
        # self.load_chroma_client()
        self.load_rag_config(app_config=app_config)


    def load_directories(self,app_config):

        self.stored_csv_xlsx_directory=app_config['directories']['stored_csv_xlsx_directory']

        self.sqldb_directory=app_config['directories']['sqldb_directory']

        self.uploaded_files_sqldb_directory =app_config["directories"]["uploaded_files_sqldb_directory"]
    
        self.stored_csv_xslx_sqldb_diretory=app_config['directories']['stored_csv_xlsx_sqldb_directory']

        # self.persist_directory=app_config['directories']['presist_directory']


    def load_llm_configs(self,app_config):

        self.model_name=os.getenv('model_name')
        self.temperature=app_config['llm_config']['temperature']



    def load_openai_models(self):
        open_api_key=os.getenv('OPENAI_API_KEY')
        self.langchain_llm=ChatOpenAI(
                    model=self.model_name,
                    temperature=self.temperature,
                    openai_api_key=open_api_key)
        

    def load_rag_config(self, app_config):
        self.collection_name = app_config["rag_config"]["collection_name"]
        self.top_k = app_config["rag_config"]["top_k"]


if __name__=='__main__':

    try:
        lc = LoadConfig()
        print(lc.config_path)
        print(lc.temperature)
        print("Configuration loaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

    