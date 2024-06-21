from src.modules.Candidate.loginCand import login_cand, email_candidate, pass_email
from src.objectRepository.candidate.registroCand.i_forgot_pass import i_forgot_password, confirm_restore_pass
from src.services.catalogs import generate_report_graphs


def i_forgot_password_candidate():
    try:
        _, headers, _, total, _ = login_cand(email_candidate, pass_email)
        steps = [
            ("i_forgot_password", i_forgot_password),
            ("confirm_restore_pass", confirm_restore_pass),
            ("login_cand", lambda: login_cand(email_candidate, pass_email))
        ]
        results = []
        function_results = [("login_cand", total['exito'])]

        for name, step in steps:
            if name == "confirm_restore_pass":
                _, result = step(headers)
            elif name == "login_cand":
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
            status_message = 'No se mandó la recuperación de contraseña exitosamente'
            print(status_message + '\n')

        return status_message, total, function_results

    except Exception as e:
        print('No se mandó la recuperación de contraseña exitosamente\n', e)
        return 'No se mandó la recuperación de contraseña', None
