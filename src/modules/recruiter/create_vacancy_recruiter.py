from src.objectRepository.recruiter.create_vacant.obj_vacanteIA import post_vacancy_ia
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual1 import position_title
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual2 import job_description
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual3 import job_skills, contract_conditions
from src.objectRepository.recruiter.create_vacant.obj_vacanteManual4 import question_soft_skill, video_psicometricas, review_vacant, post_vacancy


def create_manual_vacant(headers, recruiter_id):
    try:
        _, vacant_id = position_title(headers)
        print('\n')
        job_description(vacant_id, headers)
        print('\n')
        contract_conditions(vacant_id, headers)
        print('\n')
        job_skills(vacant_id, headers)
        print('\n')
        question_soft_skill(vacant_id, headers)
        print('\n')
        video_psicometricas(vacant_id, headers)
        print('\n')
        review_vacant(vacant_id, headers, recruiter_id)
        print('\n')
        respuesta = post_vacancy(vacant_id, headers)
        print('Se crea la vacante manual con exito:) \n', respuesta)
        return respuesta
    except Exception as e:
        print('\n No se creo la vacante manual :(', e)
        return 'No se creo la vacante manual'


def create_vacant_ia(headers):
    try:
        respuesta = post_vacancy_ia(headers)
        print('Se crea la vacante por IA')
        return respuesta
    except Exception as e:
        print('No se creo la vacante con IA', e)
        return 'No se creo la vacantre con IA'


