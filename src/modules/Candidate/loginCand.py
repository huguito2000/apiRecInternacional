import logging

from dotenv import dotenv_values

from src.objectRepository.candidate.obj_loginCand import step_login_candidate

env = dotenv_values("etc/.env")
correo = 'huguito.candidato.es@yopmail.com'

email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
pass_email = env["PASS_EMAIL_RECRUITER_HAPPY_PATH"]


def login_cand(email_candidate):
    try:
        _, candidate_id, headers = step_login_candidate(email_candidate)
        print('el correo es: ', email_candidate)
        print('paso el login_cand :)\n')
        return 'Se hizo login correctamente del candidato', headers, candidate_id
    except Exception as e:
        logging.error(f"Error inesperado durante el login :( {str(e)}")
        return {'error': str(e)}

