import logging
from src.objectRepository.recruiter.stepj_login_recruiter import step_login_recruiter


def login_recruiter(correo):
    try:
        resultado, headers = step_login_recruiter(correo)
        print(correo)
        print(resultado)
        recruiter = resultado['recruiterId']
        print(recruiter)
        print('el token' + str(headers))
        print('paso el login')
        return 'Se hizo login correctamente', headers, recruiter
    except Exception as e:
        logging.error(f"Error inesperado durante el login: {str(e)}")
        return {'error': str(e)}


