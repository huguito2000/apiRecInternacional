from itertools import product

from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_permission_candidate
from src.services.funciones import base, send_post_headers

def generate_combinations():
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

def legales_invalido_cand(headers, myBody):
    url = base + 'user/permissions/register-list'
    send_post_headers(url, headers, myBody, 200)


def step_send_all_combinations(headers):
    try:
        print('\nSe mandan las combinaciones del los permisos')
        bodies = generate_combinations()
        for body in bodies:
            legales_invalido_cand(headers, body)
        step_permission_candidate(headers)
        return 'se mandaron los permisos correctamente'
    except Exception as e:
        print('no se mandaron a los permisos', e)
        return 'No se mandaron los permisos'





