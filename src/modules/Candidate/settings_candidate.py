from src.modules.Candidate.loginCand import email_candidate, pass_email, login_cand
from src.object_repository.candidate.settings_candidate.security import change_email_candidate, verify_change_phone, \
    change_phone, change_pass_candiate, change_permisssion, delete_account


def settings_candidate():
    try:
        print('Inicia el cambio de ajustes del candidato\n')

        # Login del candidato
        _, headers, _, total, _ = login_cand(email_candidate, pass_email)

        # Lista de pasos de ajustes del candidato
        steps = [
            ("change_email_candidate", change_email_candidate),
            ("change_phone", change_phone),
            ("verify_change_phone", verify_change_phone),
            ("change_pass_candiate", change_pass_candiate),
            ("change_permisssion", change_permisssion),
            ("delete_account", delete_account)
        ]
        results = []
        function_results = [("login_cand", total['exito'])]

        # Ejecutar cada paso con manejo de parámetros
        for name, step in steps:
            if step == change_phone:
                _, lada, phone, result = step(headers)
                results.append(result)
            elif step == verify_change_phone:
                _, result = step(headers, lada, phone)
                results.append(result)
            elif step == delete_account:
                _, result = step()
                results.append(result)
            else:
                _, result = step(headers)
                results.append(result)
            function_results.append((name, result))
        print('Los resultados son:', results)

        # Calcular éxito
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}

        if exito == casos:
            status_message = 'Se hicieron los cambios de los ajustes del candidato\n'
        else:
            status_message = 'No pasaron los ajustes del candidato\n'

        print(status_message)
        return status_message, total, function_results
    except Exception as e:
        print(f'No pasaron los ajustes del candidato {e} \n')
        return 'No se cambiaron los ajustes del candidato', None
