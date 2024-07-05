from src.object_repository.recruiter.step_register_recruiter import step_register_recruiter, step_verify_email, \
    step_permissions, step_register_complete
from src.services.catalogs import env, data_user


def register_recruiter():
    global headers, code
    try:
        _, _, _, _, email = data_user(env)
        steps = [
            ("step_register_recruiter", step_register_recruiter),

            ("step_verify_email", step_verify_email),

            ("step_permissions", step_permissions),

            ("step_register_complete", step_register_complete)
        ]

        results = []
        function_results = []

        for name, step in steps:
            if name == "step_register_recruiter":
                code, headers, email, result = step(email)
            elif name == "step_verify_email":
                _, result = step(code, headers, email)
            else:
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
            status_message = 'Se registro el reclutador correctamente :)\n'
        else:
            status_message = 'No se registro el reclutador \n'

        print(status_message)
        return status_message, total, function_results

    except Exception as e:
        print('No se hizo el registro', e)
        return 'No se hizo el registro '




