from src.modules.Candidate.loginCand import pass_email, login_cand
from src.object_repository.candidate.registroCand.registerValid.my_cv.stepCVFull import work_experience, education, \
    area_experience, hard_skills, course, certificate, soft_skills, language, upload_cv, upload_photo


def register_cv(email_candidate):
    try:
        print('\ninicia el registro del cv del candidato', email_candidate)
        _, headers, _, total, _ = login_cand(email_candidate, pass_email)

        steps = [
            ("work_experience", work_experience),

            ("education", education),

            ("area_experience", area_experience),

            ("hard_skills", hard_skills),

            ("course", course),

            ("certificate", certificate),

            ("soft_skills", soft_skills),

            ("language", language),

            ("upload_cv", upload_cv),

            ("upload_cv", lambda headers: upload_cv(headers))
            ]
        # Ejecutar cada paso y acumular el resultado
        results = []
        function_results = [("login_cand", total['exito'])]
        for name, step in steps:
            _, result = step(headers)
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
            status_message = 'Se termino el registro del CV en el candidato :)\n'
        else:
            status_message = 'No se realizo el registro del CV \n'

        print(status_message)
        return status_message, total, function_results
    except Exception as e:
        print('No se realizo el registro del CV :(\n', e)
        return 'No se realizo el registro del CV', None, None, None
