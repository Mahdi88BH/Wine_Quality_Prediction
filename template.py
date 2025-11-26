import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s]: %(message)s')

projectName = "Wine_Quality_Prediction"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/entity/config_entity.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "DockerFile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating the directory for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:

            pass
            logging.info(f"Creating empty file : {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")