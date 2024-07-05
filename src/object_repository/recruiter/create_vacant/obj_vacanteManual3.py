from src.services.catalogs import env
from src.services.peticiones_HTTP import  send_post_headers, send_patch


def contract_conditions(vacant_id, headers):
    try:
        print('Inicia las condidicones de contratación')
        url = env["URL_SERVER"] + 'vacancy/management/step7/' + vacant_id
        print(url)
        my_body = {
            "contractConditions": "* tener visa\n* tener una cuenta bancaria internacional\n* tener lugar de residencia"
        }
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('se envia la sección de condiciones de contratación :)\n')
            return 'Se envia la condiciones de contratacion correctamente', 1
        else:
            print('No se crearon las condiciones de contratación\n')
            return 'No se crearon las condiciones de contratación', 0
    except Exception as e:
        print('No se mandan las condciones de contracion :( \n', e)
        return 'No se mandan las condciones de contratacion', 0


def job_skills(vacant_id, headers):
    try:
        print('Se inicia las habilidades del trabajo')
        url = env["URL_SERVER"] + 'vacancy/management/step3/' + vacant_id
        print(url)
        my_body = {
            "academicTitle": "ingeniero",
            "area": [
                {
                    "exclud": False,
                    "area": {
                        "areaId": "40288087797b055a01797b14e5f40001"
                    },
                    "yearExperience": 3
                }
            ],
            "hardSkill": [
                {
                    "level": "BASICO",
                    "skillId": "ff8080818990a16d018994456541004d",
                    "exclud": False
                }
            ],
            "idEducation": "4028818e8e3e2d7c018e3e2de2c90007",
            "levelEducationExclud": False,
            "idStatusEducation": "4028818e8e3e2d7c018e3e2debf5000f",
            "statusEducationExclud": False,
            "institution": [],
            "language": [],
            "softSkill": [
                {
                    "skillId": "ff8080818990a16d0189944565690052"
                }
            ],
            "speciality": [
                {
                    "exclud": False,
                    "speciality": {
                        "specialtyId": "4028808d7c3882b0017cb4464e099002"
                    },
                    "yearExperience": 3
                }
            ]
        }
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se inicia el patch de la vacante\n')
            url = env["URL_SERVER"] + 'vacancy/management/' + vacant_id
            my_patch = [
                {
                    "op": "replace",
                    "path": "/steps",
                    "value": "7"
                }
            ]

            resultado = send_patch(url, headers, my_patch, 200)
            if resultado != 0:
                print('Se crean las habilidades del trabajo :) \n')
            return 'Se crean las habilidades necesarias para el trabajo', 1
        else:
            print('No se crea las habilidades del trabajo \n')
            return 'No se crean las habilidades del trabajo', 0
    except Exception as e:
        print('No se mando las habilidade del trabajo :( \n', e)
        return 'No se mandaron las habilidades del trabajo', 0



