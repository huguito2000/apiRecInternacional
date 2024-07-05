import logging
from dotenv import dotenv_values
from src.object_repository.recruiter.step_login_recruiter import step_login_recruiter
from src.services.catalogs import env

email = env["EMAIL_RECRUITER_HAPPY_PATH"]
pass_email = env["PASS_EMAIL_RECRUITER_HAPPY_PATH"]


def login_recruiter(email, pass_email):
    try:
        print(f'Inicia el login del reclutador, {email}\n')
        global headers, recruiter, result
        steps = [
            ("step_login_recruiter", step_login_recruiter)
        ]
        results = []
        function_results = []
        for name, step in steps:
            headers, recruiter, result = step_login_recruiter(email, pass_email)
            results.append(result)
            function_results.append((name, result))

        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}

        if exito == casos:
            print('el correo es: ', email)
            print('paso el login reclutador :)\n')
            return 'Se hizo login correctamente del reclutador', headers, recruiter, total, function_results
        else:
            print('No se hizo el login')
        return 'No paso el login', None, None, total, function_results

    except Exception as e:
        logging.error(f"Error inesperado durante el login :( \n {str(e)}")
        return {'error': str(e)}




