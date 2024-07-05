from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.object_repository.recruiter.ajustesReclu.step_clients import step_new_client, step_delete_client, change_cupon


def customer_section():
    try:
        print('Inicia la sección de clientes')
        _, headers, _, total, _ = login_recruiter(email, pass_email)
        steps = [
            ("step_new_client", step_new_client),
            ("step_delete_client", step_delete_client),
        ]
        results = []
        function_results = [("login_recruiter", total['exito'])]
        for name, step in steps:
            _, result = step(headers)
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
            status_message = 'Paso la sección clientes'
            print(status_message + '\n')
        else:
            status_message = 'No paso la sección de clientes'
            print(status_message + '\n')

        return status_message, total, function_results
    except Exception as e:
        print('No paso la sección de clientes', e)
        return 'No paso la sección de clientes'

