from src.objectRepository.recruiter.crearVacante.obj_vacanteIA import publicar_ia
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual1 import paso1
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual2 import paso2
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual3 import paso3
from src.objectRepository.recruiter.crearVacante.obj_vacanteManual4 import paso4, paso5, paso6, paso7


def crear_vacante_manual(headers, recruiter_id):
    try:
        _, vacant_id = paso1(headers)
        print('\n')
        paso2(vacant_id, headers)
        print('\n')
        paso3(vacant_id, headers)
        print('\n')
        paso4(vacant_id, headers)
        print('\n')
        paso5(vacant_id, headers)
        print('\n')
        paso6(vacant_id, headers, recruiter_id)
        print('\n')
        respuesta = paso7(vacant_id, headers)
        print('\n', respuesta)
        return respuesta
    except Exception as e:
        print('\n No se creo la vacante manual', {e})
        return 'No se creo la vacante manual'


def crear_vacante_ia(headers):
    try:
        respuesta = publicar_ia(headers)
        print('Se crea la vacante por IA')
        return respuesta
    except Exception as e:
        print('No se creo la vacante con IA', e)
        return 'No se creo la vacantre con IA'


