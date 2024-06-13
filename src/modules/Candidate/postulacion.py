from src.modules.Candidate.loginCand import login_cand, pass_email
from src.objectRepository.candidate.postulacion.step_postulacion import postulacion, \
    exp_laboral_cuestionario, habilidad_profesional, expectativa_salarial, condiciones_de_contratacion, \
    seleccion_de_permisos


def postulacion_candidato(email_candidate):
    try:
        _, headers, _ = login_cand(email_candidate, pass_email)

        _, postulationID = postulacion(headers)

        exp_laboral_cuestionario(headers, postulationID)

        habilidad_profesional(headers, postulationID)

        expectativa_salarial(headers, postulationID)

        condiciones_de_contratacion(headers, postulationID)

        seleccion_de_permisos(headers, postulationID)

        print('Se hizo la postulacion correctamente :) \n')
        return 'Se hizo la postulacion de un candidato correctamente'

    except Exception as e:
        print('No se hizo la postulacion :( \n', e)
        return 'No se hizo la postulacion del candidato'



