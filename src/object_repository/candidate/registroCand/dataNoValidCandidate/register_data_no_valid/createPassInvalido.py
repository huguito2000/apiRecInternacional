from src.object_repository.candidate.registroCand.registerValid.stepRegisterCandidate import step_create_pass_candidate
from src.services.catalogs import env
from src.services.peticiones_HTTP import send_put

data_payloads =[
    {"@bcd.1234"},
    {"abcd.1234"},
    {"ABCD.1234"},
    {"Abcd."},
    {"1234"},
    {'Ab!"·$%&/()=?'},
    {"   "},
    {".-·$%&/()=12423424"},
]


def create_pass_invalido_cand(headers):
    try:
        print("Enviando contraseñas incorreectas...")  # More descriptive message

        url = env["URL_SERVER"] + 'auth/create-pass?password='
        results = []
        for password_variation in data_payloads:
            full_url = url + str(password_variation)
            result = send_put(full_url, headers, 412)  # Assuming success code is 200
            if result != 0:
                result = 1
                results.append(result)
                print(f"Se envió la contraseña: {password_variation}")
                print('\n')
            else:
                result = 0
                results.append(result)
                print(f"Se envió la contraseña: {password_variation}")
                print('\n')
        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            step_create_pass_candidate(headers)
            print('Se mandaron las contraseñas invalidas :) \n')
            return 'Se hicieron las pruebas de la sección de  contraseñas icorrectas', 1
        else:
            step_create_pass_candidate(headers)
            print('No se mandaron las contraseñas :( \n')
            return 'No se hizo las pruebas de la sección de contraseñas icorrectas', 0
    except Exception as e:
        print('No se mandaron las contraseñas :( \n', e)
        return 'No se hizo las pruebas de la sección de contraseñas icorrectas', 0












