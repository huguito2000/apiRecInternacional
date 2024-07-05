from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.object_repository.recruiter.step_i_forgot_pass_recruiter import confirm_restore_pass_recruiter, \
    i_forgot_password_recruiter


def i_forgot_pass_my_recruiter():
    try:
        _, headers, _, total, _ = login_recruiter(email, pass_email)
        steps = [
            ("i_forgot_password_recruiter", i_forgot_password_recruiter),
            ("confirm_restore_pass_recruiter", confirm_restore_pass_recruiter),
            ("login_recruiter", lambda: login_recruiter(email, pass_email))
        ]
        results = []
        function_results = [("login_recruiter", total['exito'])]

        for name, step in steps:
            if name == "confirm_restore_pass_recruiter":
                _, result = step(headers)
            elif name == "login_recruiter":
                _, _, _, result, _ = step()
                result = result['exito']
            else:
                _, result = step()

            results.append(result)
            function_results.append((name, result))

        print(f'Los resultados son: {results} \n')

        # Calcular éxito
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}

        if exito == casos:
            status_message = 'Se manda la sección de recuperación de contraseña'
            print(status_message + '\n')
        else:
            status_message = 'No se mandó la recuperación de contraseña'
            print(status_message + '\n')

        return status_message, total, function_results

    except Exception as e:
        print('No se mandó la recuperación de contraseña\n', e)
        return 'No se mandó la recuperación de contraseña', None
