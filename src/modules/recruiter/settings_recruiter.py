from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.object_repository.recruiter.ajustesReclu.step_company import company, photo_company
from src.object_repository.recruiter.ajustesReclu.step_settings import name_profile, photo_profile, change_pass, \
    change_email
from src.object_repository.recruiter.ajustesReclu.step_recruiting_team import recruiting_team
from src.services.catalogs import data_user, env


def settings():
    try:
        print('Inicia la sección de ajustes')
        _, headers, _, total, _ = login_recruiter(email, pass_email)
        name, last_name, second_last_name, _, new_email = data_user(env)
        _, _, _, _, new_email2 = data_user(env)

        steps = [

            ("photo_profile", photo_profile),

            ("change_pass", change_pass),

            ("photo_company", photo_company),

            ("company", company),

            ("recruiting_team", lambda headers: recruiting_team(headers, new_email2)),

            ("change_email", lambda headers: change_email(headers, new_email)),

            ("name_profile", lambda headers: name_profile(headers, name, last_name, second_last_name))
        ]

        results = []
        function_results = [("login_recruiter", total['exito'])]

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
            status_message = 'Se hicieron los cambio en los ajustes :)\n'
        else:
            status_message = 'No se hicieron los cambio en los ajustes \n'

        print(status_message)
        return status_message, total, function_results

    except Exception as e:
        print(f'Fallaron las pruebas de la sección de ajustes: {e}')
        return 'Fallaron las pruebas de la sección de ajustes'



