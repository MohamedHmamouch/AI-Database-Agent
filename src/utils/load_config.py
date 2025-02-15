import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import yaml

def load_yaml_config():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "configs", "config.yaml"))
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found at {config_path}")
    with open(config_path, "r") as f:
        app_config = yaml.load(f, Loader=yaml.FullLoader)
    return app_config, config_path

def load_directories(app_config):
    directories = {
        "stored_csv_xlsx_directory": app_config["directories"]["stored_csv_xlsx_directory"],
        "sqldb_directory": app_config["directories"]["sqldb_directory"],
        "uploaded_files_sqldb_directory": app_config["directories"]["uploaded_files_sqldb_directory"],
        "stored_csv_xlsx_sqldb_directory": app_config["directories"]["stored_csv_xlsx_sqldb_directory"]
    }
    return directories

def load_llm_config(app_config):
    model_name = os.getenv("model_name")
    temperature = app_config["llm_config"]["temperature"]
    return model_name, temperature

def load_openai_model(model_name, temperature):
    open_api_key = os.getenv("OPENAI_API_KEY")
    langchain_llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        openai_api_key=open_api_key
    )
    return langchain_llm

def load_rag_config(app_config):
    rag_config = {
        "collection_name": app_config["rag_config"]["collection_name"],
        "top_k": app_config["rag_config"]["top_k"]
    }
    return rag_config

def main():
    load_dotenv()
    app_config, config_path = load_yaml_config()
    directories = load_directories(app_config)
    model_name, temperature = load_llm_config(app_config)
    langchain_llm = load_openai_model(model_name, temperature)
    rag_config = load_rag_config(app_config)
    print(f"Config path: {config_path}")
    print(f"LLM temperature: {temperature}")
    print("Configuration loaded successfully!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
