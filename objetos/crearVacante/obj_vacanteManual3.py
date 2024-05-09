from objetos.crearVacante.obj_vacanteManual1 import paso1
from objetos.crearVacante.obj_vacanteManual2 import paso2
from objetos.funciones import base, sendPostHeaders
from test.login import login

#respuesta, headers, recruiterID = login()
def paso3(vacantId, headers):
    try:
        url = base + 'vacancy/management/step3/' + vacantId
        print(url)
        myBody = {
            "academicTitle": "ingeniero",
            "area": [
                {
                    "exclud": False,
                    "area": {
                        "areaId": "40288087797b055a01797b14e5f40001"
                    },
                    "yearExperience": 2
                }
            ],
            "hardSkill": [
                {
                    "level": "AVANZADO",
                    "skillId": "2c9f8a0a8ee3c5ae018f073dbe950570",
                    "exclud": False
                }
            ],
            "idEducation": "4028818e8e3e2d7c018e3e2de2c90007",
            "levelEducationExclud": False,
            "idStatusEducation": "4028818e8e3e2d7c018e3e2de86d000c",
            "statusEducationExclud": False,
            "institution": [],
            "language": [],
            "softSkill": [
                {
                    "skillId": "2c9f8a0a8ecf64a8018ee2f59c190116"
                }
            ],
            "speciality": [
                {
                    "exclud": False,
                    "speciality": {
                        "specialtyId": "4028808d7c3882b0017cb4464e099002"
                    },
                    "yearExperience": 3
                },
                {
                    "exclud": False,
                    "speciality": {
                        "specialtyId": "4028808d7c3882b0017cb4464e099001"
                    },
                    "yearExperience": 2
                }
            ]
        }
        sendPostHeaders(url, headers, myBody, 200)
        print('\n Se hizo el tercer paso de la creación de la vacante')
        return 'Se hizo el tercep paso de la creación de la vacante '
    except Exception as e:
        print('No se hizo la cración del tercer paso de la vacante', e)
        return 'No se hizo la creación del tercer paso de la vacante'

