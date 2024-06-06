import logging
from src.objectRepository.candidate.obj_loginCand import step_login_candidate

correo = 'huguito.candidato.es@yopmail.com'


def login_cand(correo):
    try:
        _, candidate_id, headers = step_login_candidate(correo)
        print('el correo es: ', correo)
        print('paso el login_cand \n')
        return 'Se hizo login correctamente', headers, candidate_id
    except Exception as e:
        logging.error(f"Error inesperado durante el login: {str(e)}")
        return {'error': str(e)}

