from itertools import product

from dotenv import dotenv_values

from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_permission_candidate
from src.services.peticiones_HTTP import base, send_post_headers

env = dotenv_values("etc/.env")


def generate_combinations():
    print('Se generan las combianaciones de las notificaciones')
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
        send_post_headers(url, headers, myBody, 200)
        print('\n')
        return 'Se manda la peticion para el envio de los permisos'
    except Exception as e:
        print('No se manda la peticion para el envio de los permisos :( \n', e)
        return 'No se manda la peticion para el envio de los permisos'


def step_send_all_combinations_legals(headers):
    try:
        print('Se mandan las combinaciones del los permisos \n')
        bodies = generate_combinations()
        for body in bodies:
            permisos_invalido_cand(headers, body)
            #print(f"  - Se envió los permisos: {bodies} \n")
        step_permission_candidate(headers)
        print('se manda todas la combianciones posibles de los permisos de las notificaciones :) \n')
        return 'se manda todas la combianciones posibles de los permisos de  las notificaciones'
    except Exception as e:
        print('no se mandaron a los permisos :( \n', e)
        return 'No se mandaron los permisos de notificaiones'





