from src.modules.Candidate.loginCand import email_candidate, pass_email
from src.object_repository.candidate.obj_loginCand import step_login_candidate
from src.object_repository.candidate.registroCand.registerValid.my_data.data_profile import delete_photo, \
    change_photo_profile, profile_search, delete_profile_search, change_profile


def my_data_profile():
    try:
        _, headers, total = step_login_candidate(email_candidate, pass_email)
        steps = [
            ("delete_photo", delete_photo),
            ("change_photo_profile", change_photo_profile),
            ("profile_search", profile_search),
            ("delete_profile_search", delete_profile_search),
            ("change_profile", change_profile)
        ]

        results = []
        function_results = [("step_login_candidate", total)]
        for name, step in steps:
            if step == profile_search:
                _, _, result = step(headers)
                results.append(result)
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
            status_message = 'Pasaron las preubas de los cambios de perfil del candiato \n'
        else:
            status_message = 'No se hicieron los cambios de perfil del candidato \n'

        print(status_message)
        return status_message, total, function_results

    except Exception as e:
        print('No se hicieron los cambios de perfil del candidato', e)
        return 'No se hicieron los cambios de perfil del candidato', None, None

