from dotenv import dotenv_values

from src.services.catalogs import pdfs, subir_archivo, foto
from src.services.peticiones_HTTP import send_post_headers, send_put_body

env = dotenv_values("etc/.env")

def work_experience(headers):
    try:
        my_body = [
            {
                "company": "involve",
                "dateDeparture": None,
                "dateEntry": "2000-12-12",
                "dependents": False,
                "functions": "hola mundo ",
                "numberDependents": 0,
                "position": {
                    "position": "tester"
                },
                "positionType": {
                    "positionTypeId": "40288086796be11e01796c18e66f0064"
                },
                "working": True,
                "candidateId": "ff8080818e9a6892018e9a743f60001b"
            }
        ]

        url = env["URL_SERVER"] + 'user/candidate/work-experience'
        response = send_post_headers(url, headers, my_body, 200)
        print('Se manda la experiencia laboral', response)
        return 'Se manda la experiencia laboral del candidato'
    except Exception as e:
        print('No paso la experiencia laboral', e)
        return 'No paso la experiancia laboral del candidato'


def education(headers):
    try:
        my_body = [
            {
                "educationStatus": {
                    "catalogSystemId": "4028818e8e3e2d7c018e3e2ded120010",
                    "name": "Titulado",
                    "type": "educationStatus",
                    "level": 5,
                    "status": True,
                    "keySystem": None,
                    "shown": True
                },
                "educationLevel": {
                    "catalogSystemId": "4028818e8e3e2d7c018e3e2de60f000a",
                    "name": "Doctorado",
                    "type": "educationLevel",
                    "level": 8,
                    "status": True,
                    "keySystem": None
                },
                "countryInstitute": "México",
                "degree": "ingeniero",
                "instituteName": "unam",
                "startYear": "2010",
                "endYear": "2015",
                "candidateId": "ff8080818e9f641f018e9fa35d270022",
                "institute": {
                    "name": "(enap) hoy (fad) de la unam",
                    "idInstitution": "2c9fc61583f3fea50184e357a04e7db7",
                    "codeCountry": "mx"
                }
            }
        ]
        url = env["URL_SERVER"] + 'user/candidate/education'
        response = send_post_headers(url, headers, my_body, 200)
        print('Se manda la educacion', response)
        return 'Se manda la educaion'
    except Exception as e:
        print('No manda la educación del candidato', e)
        return 'No se mando la educación del candidato'


def area_experience(headers):
    try:
        my_body = [
            {
                "areaId": "40288087797b055a01797b14e5f40036",
                "name": "Tecnología de la información",
                "specialties": [
                    {
                        "specialtyId": "4028808d7c3882b0017cb4464e099434",
                        "name": "QA",
                        "areaId": "40288087797b055a01797b14e5f40036"
                    }
                ]
            }
        ]
        url = env["URL_SERVER"] + 'user/candidate/area'
        response = send_post_headers(url, headers, my_body, 200)
        print('Se manda el area de experiencia del candidato', response)
        return 'Se manda la experiencia laboral'
    except Exception as e:
        print('No se mandao la experiencia', e)
        return 'No se mando la experiencia laboral'


def hard_skills(headers):
    try:
        my_body = [
            {
                "level": "EXPERTO",
                "skill": "Conocimiento avanzado de Microsoft Excel. "
            }
        ]
        url = env["URL_SERVER"] + 'user/candidate/hard-skill'
        response = send_post_headers(url, headers, my_body, 200)
        print(response)
        return 'Se manda las habilidades duras'
    except Exception as e:
        print('No se mandaron las habilidades duras', e)
        return 'No se mandan las habilidades duras del candidato'

def course(headers):
    try:
        my_body = {
            "dateExpedition": "2022-12-12",
            "hours": "82",
            "insitute": "udemy",
            "name": "istbq"
        }
        url = env["URL_SERVER"] + 'user/candidate/course'
        response = send_put_body(url, headers, my_body, 200)
        print('Se manda el curso del candidato', response)
        return 'Se manda el curso del candidato'
    except Exception as e:
        print('No se mando el curso del candidato', e)
        return 'No se mando el curso del candidato'


def certificate(headers):
    try:
        my_body = {
            "credentialId": "udemy121212",
            "institute": "IPN",
            "dateExpedition": "2022-12-12",
            "dateExpire": "",
            "name": "istbq",
            "url": "www.google.com",
            "isExpire": False,
            "candidateCertificationId": "ff8080818b82167a018bb0cf881300fc"
        }
        url = env["URL_SERVER"] + 'user/candidate/certification'
        response = send_put_body(url, headers, my_body, 200)
        print('se mandan las certificaciones del candidate', response)
        return 'Se mandan las certificaiones del candidate'
    except Exception as e:
        print('No se envio la certificacion', e)
        return 'No se envio la certificacion del candidato'


def soft_skills(headers):
    try:
        my_body = [
            {
                "skill": "Trabajo en equipo"
            }
        ]
        url = env["URL_SERVER"] + 'user/candidate/soft-skill'
        response = send_post_headers(url, headers, my_body, 200)
        print('se manda las habilidades blandas', response)
        return 'Se mandan las habilidades blandas'
    except Exception as e:
        print('No se mandan las habilidades blandas', e)
        return 'No se mandan las habilidades blandas'


def language(headers):
    try:
        my_body = [
            {
                "language": {
                    "languageId": "402880de7abf2e1e017abf8cdc1e0000",
                    "spanishName": "Africano"
                },
                "level": "NATIVO"
            }
        ]
        url = env["URL_SERVER"] + 'user/candidate/language'
        response = send_post_headers(url, headers, my_body, 200)
        print('Se mandan los idiomas', response)
        return 'Se manda los idiomas'
    except Exception as e:
        print('No se mandaron los lenguajes', e)
        return 'No se mandan los lenguajes'


def upload_cv(headers):
    try:
        url = env["URL_SERVER"] + 'files/upload/upload-candidate-cv?md5Hash=123'
        ruta = pdfs()
        print("esta es la ruta del pdf" + ruta)
        response = subir_archivo(ruta, url, headers, 201)
        print('Se subio el cv', response)
        return 'Se sube el CV'
    except Exception as e:
        print('No se subio el cv', e)
        return 'No se subio el CV'


def upload_photo(headers):
    try:
        url = env["URL_SERVER"] + 'files/upload/uploadFile?typeFile=URL_PHOTO'
        ruta = foto()
        print(ruta)
        response = subir_archivo(ruta, url, headers, 201)
        print('Se subio la foto de perfil', response)
        return 'Se subio la foto de perfil'
    except Exception as e:
        print('No se subio la foto de perfil', e)
        return 'No se subio la foto de perfil'

