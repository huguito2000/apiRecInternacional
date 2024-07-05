from src.modules.Candidate.loginCand import login_cand, pass_email, email_candidate
from src.objectRepository.candidate.busqueda.busquedaDeVacantes import step_search_position, \
    step_search_salary, \
    step_search_workday, step_search_modality, step_search_type_contract, step_search_type_company, step_search_time



def search_vacancy():
    try:
        _, headers, _, total, _ = login_cand(email_candidate, pass_email)
        steps = [
            ("step_search_position", step_search_position),
            ("step_search_salary", step_search_salary),
            ("step_search_workday", step_search_workday),
            ("step_search_modality", step_search_modality),
            ("step_search_type_contract", step_search_type_contract),
            ("step_search_type_company", step_search_type_company),
            ("step_search_time", step_search_time)
            ]
        # Ejecutar cada paso y acumular el resultado
        results = []
        function_results = [("login_cand", total['exito'])]
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
            status_message = 'Se realizo la prueba de busqueda de vacantes'
        else:
            status_message = 'No paso la prueba de busqueda de vacantes'
        print(status_message)

        return status_message, total, function_results
    except Exception as e:
        print('No paso la prueba de busqueda de vacantes', e)
        return 'No paso la prueba de busqueda de vacantes', None, None
