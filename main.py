#pip install python-dotenv

from dotenv import dotenv_values

from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.recruiter.login_recruiter import login_recruiter, email
from src.modules.recruiter.register_recruiter import register_recruiter
from src.objectRepository.recruiter.ajustesReclu.step_clients import get_client, change_cupon
from src.test.create_report_recruiter.report_happy_path_reclu import happypath_test_reclu

enviroment = dotenv_values("etc/.env")

print("comenzado prueba por consola ", enviroment)

register_onboarding_candidate(enviroment)








