from src.services.catalogs import data_user, env
from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate, \
    step_create_pass_candidate, step_permission_candidate, step_phone_candidate, step_resend_code, \
    step_verify_code_cand, step_names_candidate


def register_onboarding_candidate():
    try:
        # Extraer datos del usuario
        name, last_name, _, birth_date, _ = data_user(env)

        # Registrar al candidato
        headers, email_candidate, total = step_register_candidate()
        print('con el email', email_candidate)

        # Realizar pasos de onboarding
        steps = [
            ("step_create_pass_candidate", step_create_pass_candidate),
            ("step_permission_candidate", step_permission_candidate),
            ("step_phone_candidate", step_phone_candidate),
            ("step_resend_code", step_resend_code),
            ("step_verify_code_cand", step_verify_code_cand),
            ("step_names_candidate", lambda headers: step_names_candidate(headers, name, last_name, birth_date))
        ]

        # Ejecutar cada paso y acumular el resultado
        results = []
        function_results = [("step_register_candidate", total)]
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
            status_message = '\nSe realizó el registro de candidato correctamente :)\n'
        else:
            status_message = 'No se realizó el registro completo \n'

        print(status_message)
        return status_message, email_candidate, total, function_results
    except Exception as e:
        print('No se realizó el registro de candidato :(\n', e)
        return 'No se realizó el registro de candidato', None, None, None




