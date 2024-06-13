from dotenv import dotenv_values

from src.modules.Candidate.loginCand import pass_email
from src.objectRepository.candidate.obj_loginCand import step_login_candidate
from src.services.peticiones_HTTP import base, send_post, send_post_headers_sin_body

env = dotenv_values("etc/.env")
email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
my_body_no_valido = [
    {
    "email": "@yopmail.com",
    "password": "Abcd.12345",
    },
    {
        "email": "2803yopmail.com",
        "password": "Abcd.12346",
    },
    {
        "email": "2803@",
        "password": "Abcd.12347",
    },
    {
        "email": "2803@yopmail.com",
        "password": "",
    },
    {
        "email": "2803@yopmail.com",
        "password": "Abcd1234",
    },
    {
        "email": "2803❤️@yopmail.com",
        "password": "Abcd.1234",
    },
    {
        "email": "",
        "password": "",
    },
    {
        "email": "noregistrado@yopmail.com",
        "password": "Abcd.1234",
    }
]


def hacer_login400_cand(my_body, code):
    try:
        url = env["URL_SERVER"] + 'auth/login'
        resultado = send_post(url, my_body, (400, 423))
        print(f"Resultado con datos: {my_body}, código: {code}")
        print('se manda los datos para validar el login con codigo 400', resultado)
        print('\n')
        return 'Se mandan los datos para validar el login con datos erroneos'
    except Exception as e:
        print('No se pudo hacer la prueba del login con datos incorretos exitosamente', e)
        return 'No se pudo realizar la prueba del login con datos incorretos exitosamente'



def login_no_valido_cand():
    try:
        print('Inicia la pruebas de candidato con datos no validos \n')
        for data in my_body_no_valido:
            hacer_login400_cand(data.copy(), 400 if data["email"] else 409)
        return 'Se realizaron las pruebas del login con datos no validos'
    except Exception as e:
        print('No se realizaron las pruebas correctamente del login invalido', e)
        return 'No se pudo realizar la prueba del login con datos incorretos exitosamente'


def login_cand_bloqueado():
    try:
        _, _, headers = step_login_candidate(email_candidate, pass_email)
        print('Se hace login para validar que es un usuario activo y obtener los header')
        my_body_no_valido = {
                "email": email_candidate,
                "password": "Abcd.123",
            }
        print('Login valido acesso concedido señor huguito')
        print('Se hace 3 veces login de manera incorrecta para bloquear al usuario \n')
        for _ in range(3):
            hacer_login400_cand(my_body_no_valido, (401, 423))
        print('Se manda la a recuperar la contraseña para desbloquear al usuario \n')
        url = env["URL_SERVER"] + 'auth/confirm-restore-pass?password=Abcd.1234'
        send_post_headers_sin_body(url, headers, 200)
        print('candidato desbloqueado')
        print('Se hizo login con un usuario bloqueado y posteriormente se desbloqueo al usuario \n')
        return 'Se hizo login con un usuario bloqueado y posteriormente se desbloqueo al usuario'
    except Exception as e:
        print('No pasaron las pruebas del usuario bloqueado y tratar de desbloquearlo', e)
        return 'No pasaron las pruebas del usuario bloqueado y tratar de desbloquearlo'

















