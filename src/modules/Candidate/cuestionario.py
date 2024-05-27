from src.modules.Candidate.loginCand import login_cand
from src.objectRepository.candidate.registroCand.postulacion.obtenerVacanteId import postulacion, \
    exp_laboral_cuestionario, habilidad_profesional, expectativa_salarial, condiciones_de_contratacion, \
    seleccion_de_permisos


def cuestionario(correo):
    candidateId, headers = login_cand(correo)

    postulationID = postulacion(headers)
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


