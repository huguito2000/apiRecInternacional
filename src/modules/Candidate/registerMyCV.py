from src.objectRepository.candidate.obj_loginCand import step_login_candidate
from src.objectRepository.candidate.registroCand.registerValid.my_cv.stepCVFull import work_experience, education, \
    area_experience, hard_skills, course, certificate, soft_skills, language, upload_cv, upload_photo

def register_cv(correo):
    try:
        _, headers = step_login_candidate(correo)

        work_experience(headers)
        print('se manda la experiencia laboral')

        education(headers)
        print('se manda la educación')

        area_experience(headers)
        print("se manda el area de exp")

        hard_skills(headers)
        print("se manda habilidades duras")

        course(headers)
        print("se manda curso")

        certificate(headers)
        print("se manda certificado")

        soft_skills(headers)
        print("se manda habilidad blanda")

        language(headers)
        print("se manda el idioma")

        upload_cv(headers)
        print("Se sube el archivo de CV")

        upload_photo(headers)
        print("se sube la imagen de perfil")

        print('se termina el CV del candidato')
        return 'Se termino el CV el candidato'
    except Exception as e:
        print('No se realizo el registro del CV', e)
        return 'No se realizo el registro del CV'


