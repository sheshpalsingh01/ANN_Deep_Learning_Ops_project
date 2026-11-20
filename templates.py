import os
from pathlib import Path
import logging

os.getcwd()

Project_name = "DeepLearningClassification"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
)

list_of_file =[
    ".github/workflows/.gitkeep",
    f"src/{Project_name}/__init__.py",
    f"src/{Project_name}/components/__init__.py",
    f"src/{Project_name}/config/__init__.py",
    f"src/{Project_name}/config/configuration.py",
    f"src/{Project_name}/logging/__init__.py",
    f"src/{Project_name}/logging/logger.py",
    f"src/{Project_name}/pipeline/__init__.py",
    f"src/{Project_name}/entity/__init__.py",
    f"src/{Project_name}/entity/config_entity.py",
    f"src/{Project_name}/constant/__init__.py",
    f"src/{Project_name}/exception/__init__.py",
    f"src/{Project_name}/exception/exceptions.py",
    "test/app_test.py",
    ".env",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "research/research.ipynb",
    "data",
    "docker-compose.yaml",
    ".dockerignore",
    "templates/index.html"
]

for filepath in list_of_file:
    filepath  = Path(filepath)
    filedir, filename =os.path.split(filepath)
    
    
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory Created : {filedir} for th file {filename}")
        
    if (not os.path.exists(filepath)) or( os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Empty file created : {filepath}")
    else:
        logging.info(f"file already exists : {filepath}")