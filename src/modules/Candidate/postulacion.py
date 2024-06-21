from src.modules.Candidate.loginCand import login_cand, pass_email
from src.objectRepository.candidate.postulacion.step_postulacion import postulacion, \
    exp_laboral_cuestionario, habilidad_profesional, expectativa_salarial, condiciones_de_contratacion, \
    seleccion_de_permisos, habilidad_blandas, change_permission_postulation, upload_questions_video_presentation, \
    upload_video_interview, delete_postulation


def postulacion_candidato(email_candidate):
    try:
        # Login del candidato
        _, headers, _, total, _ = login_cand(email_candidate, pass_email)

        # Realizar la postulación inicial
        _, postulation_id, total2 = postulacion(headers)

        # Lista de pasos de postulación
        steps = [
            ("exp_laboral_cuestionario", exp_laboral_cuestionario),
            ("habilidad_profesional", habilidad_profesional),
            ("habilidad_blandas", habilidad_blandas),
            ("habilidad_blandas", expectativa_salarial),
            ("condiciones_de_contratacion", condiciones_de_contratacion),
            ("seleccion_de_permisos", seleccion_de_permisos)
        ]
        # Ejecutar cada paso y acumular el resultado
        results = []
        function_results = [("login_cand", total['exito']), ("postulacion", total2['exito'])]

        for name, step in steps:
            _, result = step(headers, postulation_id)
            results.append(result)
            function_results.append((name, result))

        print(f'los resultados son: {results} \n')
        # Calcular éxito
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}
        if exito == casos:
            print('Se hizo la postulación correctamente :) \n')
            return 'Se hizo la postulación de un candidato correctamente', postulation_id, headers, total, function_results
        else:
            print('No se hizo la postulación :( \n')
            return 'No se hizo la postulación del candidato', None, None, total, function_results
    except Exception as e:
        print('No se hizo la postulación :( \n', e)
        return 'No se hizo la postulación del candidato', None, None, None, None


def postulacion_video(email_candidate, postulation_id, headers):
    try:
        # Lista de pasos de postulación de video
        steps = [
            change_permission_postulation,
            upload_questions_video_presentation,
            upload_video_interview
        ]

        # Ejecutar cada paso
        results = []
        for step in steps:
            if step == upload_questions_video_presentation:
                _, result = step(headers)
                results.append(result)
            else:
                _, result = step(headers, postulation_id)
                results.append(result)
            print('El resultado es:', result)
        print('los resultados son:', results)
        exito = sum(results)
        fallo = len(results) - exito
        print('fallarón:', fallo)
        total = {"exito": exito,
                 "fallo": fallo}
        if exito >= 3:
            print(f'Se hace la postulación con videos de {email_candidate} :)\n')
            return 'Se hace la postulación de videos', total
        else:
            print('No se hizo la postulación con video\n')
            return 'No se hizo la postulación con videos', total
    except Exception as e:
        print(f'No se hizo la postulación con video {e}\n')
        return 'No se hizo la postulación con videos', None


def delete_postulation_candidate(headers, postulation_id):
    try:
        print('Se incia la eliminacion de la postulación\n')
        _, exito = delete_postulation(headers, postulation_id)
        fallo = exito - 1
        print('Pasaron:', exito)
        print('Fallarón', fallo)
        total = {"exito": exito,
                 "fallo": fallo}
        if exito >= 1:
            print('Se realizo la eliminacion de la postulacion :)\n')
            return 'Se realizo la eliminación de la postulación', total
        else:
            print('no se hace la eliminación de la postulación\n')
            return 'No se hace la eliminacion de la postulacion', total
    except Exception as e:
        print(f'no se hace la eliminación de la postulación{e}\n')
        return 'No se hace la eliminacion de la postulacion'



