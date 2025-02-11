from dotenv import dotenv_values

from src.services.peticiones_HTTP import base, send_put

env = dotenv_values("etc/.env")
data_payloads =[
    {"Abcd.1234"},
    {"abcd.1234"},
    {"ABCD.1234"},
    {"Abcd."},
    {"1234"},
    {'Ab!"·$%&/()=?'},
    {"   "},
    {"Abcd.1234"},
]

def create_pass_invalido_cand(headers):
    try:
        print("Enviando contraseñas...")  # More descriptive message

        url = env["URL_SERVER"] + 'auth/create-pass?password='

        for password_variation in data_payloads:
            full_url = url + str(password_variation)
            send_put(full_url, headers, 200)  # Assuming success code is 200
            print(f"  - Se envió la contraseña: {password_variation}")
        return 'Se hicieron las pruebas de la sección de  contraseñas icorrectas'
    except Exception as e:
        print('No se mandaron las contraseñas', e)
        return 'No se hizo las pruebas de la sección de contraseñas icorrectas'









