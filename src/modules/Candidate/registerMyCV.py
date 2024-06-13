from src.modules.Candidate.loginCand import pass_email
from src.objectRepository.candidate.obj_loginCand import step_login_candidate
from src.objectRepository.candidate.registroCand.registerValid.my_cv.stepCVFull import work_experience, education, \
    area_experience, hard_skills, course, certificate, soft_skills, language, upload_cv, upload_photo


def register_cv(email_candidate):
    try:
        print('\ninicia el registro del cv del candidato', email_candidate)
        _, _, headers = step_login_candidate(email_candidate, pass_email)

        work_experience(headers)

        education(headers)

        area_experience(headers)

        hard_skills(headers)

        course(headers)

        certificate(headers)

        soft_skills(headers)

        language(headers)

        upload_cv(headers)

        upload_photo(headers)

        print('se termina el CV del candidato :)\n')
        return 'Se termino el registro del CV en el candidato'
    except Exception as e:
        print('No se realizo el registro del CV :(\n', e)
        return 'No se realizo el registro del CV'
