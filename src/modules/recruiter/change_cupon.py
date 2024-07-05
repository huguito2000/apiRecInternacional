from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.object_repository.recruiter.ajustesReclu.step_clients import change_cupon, step_new_client


def change_cupon_client():
    try:
        print('Inicia el canje de cupon')
        _, headers, _, total, _ = login_recruiter(email, pass_email)
        steps = [
            ("step_new_client", step_new_client),
            ("change_cupon", change_cupon)
        ]
        results = []
        function_results = [("login_recruiter", total['exito'])]

        for name, step in steps:
            if name == "step_new_client":
                client_id, result = step(headers)
            else:
                _, result = step(headers, client_id)
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
            status_message = 'Se hace el canje del cupón'
            print(status_message + '\n')
        else:
            status_message = 'No se hace el canje del cupón'
            print(status_message + '\n')

        return status_message, total, function_results
    except Exception as e:
        print('No se canjeo el cupon', e)
        return 'No se canjeo el cupon'