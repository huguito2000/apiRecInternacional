import logging
from dotenv import dotenv_values
from src.objectRepository.recruiter.stepj_login_recruiter import step_login_recruiter

env = dotenv_values("etc/.env")
email = env["EMAIL_RECRUITER_HAPPY_PATH"]
pass_email = env["PASS_EMAIL_RECRUITER_HAPPY_PATH"]


def login_recruiter(email):
    try:
        resultado, headers = step_login_recruiter(email, pass_email)
        print(email)
        recruiter = resultado['recruiterId']
        print('se obtuvo el recruiterID del login :) \n')
        return 'Se hizo login correctamente', headers, recruiter
    except Exception as e:
        logging.error(f"Error inesperado durante el login :( \n {str(e)}")
        return {'error': str(e)}




