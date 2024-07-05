import logging
from src.object_repository.candidate.obj_loginCand import step_login_candidate
from src.services.catalogs import env, generate_report_graphs

email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
pass_email = env["PASS_EMAIL_RECRUITER_HAPPY_PATH"]


def login_cand(email_candidate, pass_email):
    print('Inicia el login del candidato', email_candidate)
    global result, headers, candidate_id
    try:
        steps = [
            ("step_login_candidate", step_login_candidate)
        ]
        results = []
        function_results = []
        for name, step in steps:
            candidate_id, headers, result = step_login_candidate(email_candidate, pass_email)
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
            print('el correo es: ', email_candidate)
            print('paso el login_cand :)\n')
            return 'Se hizo login correctamente del candidato', headers, candidate_id, total, function_results
        else:
            print('No se hizo el login')
        return 'No paso el login', None, None, total, function_results

    except Exception as e:
        logging.error(f"Error inesperado durante el login :( {str(e)}")
        return {'error': str(e)}


