import random
from src.services.catalogs import env
from src.services.peticiones_HTTP import send_post_headers, send_get_headers


def recruiting_team(headers, new_email):
    try:
        print('Inicia la seccion de equipo de reclutamiento\n')
        url = env["URL_SERVER"] + "user/recruitment-team/invitation"
        my_body = [
            {
                "email": new_email,
                "rol": "RECRUITER"
            }
        ]
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('Se hace invitacion a un reclutador invitado', new_email)
            url = env["URL_SERVER"] + "user/recruitment-team?pageNumber=0&pageSize=10&sortBy=us.name&sortDirection=ASC"
            respuesta = send_get_headers(url, headers, 200)
            if respuesta != 0:
                num: int = len(respuesta['content'])
                num = random.randint(0, num - 1)
                recruiter_id = respuesta['content'][num]
                recruiter_id = recruiter_id['recruiterId']
                url = env["URL_SERVER"] + "user/recruitment-team/invitation?recruiterId=" + recruiter_id
                respuesta = send_post_headers(url, headers, my_body, 200)
                if respuesta != 0:
                    print('Se reenvia la invitación')
            return 'Se hace invitacion a un reclutador auxiliar', 1
        else:
            print('No se mando la invitación al reclutador invitado')
            return 'No se mando la invitación al reclutador invitado', 0
    except Exception as e:
        print('No paso la sección de reclutamiento', e)
        return 'No paso la sección de reclutamiento', 0




