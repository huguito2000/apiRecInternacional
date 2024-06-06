from src.modules.Candidate.loginCand import login_cand
from src.objectRepository.candidate.postulacion.step_postulacion import postulacion, \
    exp_laboral_cuestionario, habilidad_profesional, expectativa_salarial, condiciones_de_contratacion, \
    seleccion_de_permisos



def postulacion_candidato(correo):
    try:
        _, headers, _ = login_cand(correo)

        _, postulationID = postulacion(headers)
        print('se obtuvo la postulacionID')


        exp_laboral_cuestionario(headers, postulationID)
        print('Paso la experiencia laboral')

        habilidad_profesional(headers, postulationID)
        print('paso la habilidad profecional')

        expectativa_salarial(headers, postulationID)
        print('Paso la expectativa salarial')

        condiciones_de_contratacion(headers, postulationID)
        print('paso las condiciones de contratación')

        seleccion_de_permisos(headers, postulationID)

        print('Se mandaron los permisos de VP, VE, Psicometricas')
        return 'Se hizo la postulacion de un candidato correctamente'
    except Exception as e:
        print('No se hizo la postulacion', e)
        return 'No se hizo la postulacion del candidato'



