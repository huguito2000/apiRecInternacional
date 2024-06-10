#pip install python-dotenv
#source venv/bin/activate
from dotenv import dotenv_values

from src.test_by_gui import gui_candidate

enviroment = dotenv_values("etc/.env")

gui_candidate()














