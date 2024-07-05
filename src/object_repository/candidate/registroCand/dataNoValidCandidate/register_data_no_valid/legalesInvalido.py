from itertools import product
from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_permission_candidate
from src.services.catalogs import env
from src.services.peticiones_HTTP import base, send_post_headers


def generate_combinations():
    print('Se generan las combinaciones de las notificaciones')
    permission_types = [
        "NOTIFICATION_PROCESS",
        "REMINDER",
        "JOB_VACANCIES",
        "NEWSLETTER_INTERNAL",
        "NEWSLETTER_EXTERNAL",
        "RECOMMENDATIONS"
    ]

    combinations = list(product([False, True], repeat=len(permission_types)))
    bodys = []
    for combination in combinations:
        body = []
        for status, permission_type in zip(combination, permission_types):
            body.append({
                "status": status,
                "permissionType": permission_type
            })
        bodys.append(body)
    return bodys


def permisos_invalido_cand(headers, myBody):
    try:
        print('Se inicio el envio de los permisos \n')
        url = env["URL_SERVER"] + 'user/permissions/register-list'
        resultado =send_post_headers(url, headers, myBody, 200)
        if resultado != 0:
            print('Se mandaron los permisos\n')
            return 'Se manda la peticion para el envio de los permisos', 1
        else:
            print('No se manda la peticion para el envio de los permisos :( \n')
            return 'No se manda la peticion para el envio de los permisos', 1
    except Exception as e:
        print('No se manda la peticion para el envio de los permisos :( \n', e)
        return 'No se manda la peticion para el envio de los permisos', 0


def step_send_all_combinations_legals(headers):
    try:
        print('Se mandan las combinaciones del los permisos \n')
        bodies = generate_combinations()
        results = []
        n = 0
        for body in bodies:
            _, result = permisos_invalido_cand(headers, body)
            results.append(result)
            print('combinacion', n)
            n += 1
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            step_permission_candidate(headers)
            print('se manda todas la combianciones posibles de los permisos de las notificaciones :) \n')
            return 'se manda todas la combianciones posibles de los permisos de  las notificaciones', 1
        else:
            step_permission_candidate(headers)
            print('no se mandaron a los permisos :( \n')
            return 'No se mandaron los permisos de notificaiones', 0
    except Exception as e:
        print('no se mandaron a los permisos :( \n', e)
        return 'No se mandaron los permisos de notificaiones'





