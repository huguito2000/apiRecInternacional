from objetos.obj_login import hacerLogin
import logging


class LoginFailedError:
    pass

def login():
    try:
        resultado, headers, token = hacerLogin()
        print(resultado)
        recruiter = resultado['recruiterId']
        print(recruiter)
        print('el token' + str(headers))
        print('paso el login')
        return 'Se hizo login correctamente', headers, recruiter
    except LoginFailedError as e:
        logging.error(f"Error de login: {str(e)}")
        return {'error': str(e)}
    except Exception as e:
        logging.exception(f"Error inesperado durante el login: {str(e)}")
        return {'error': str(e)}



