from src.services.catalogs import data_user, env, generate_report_graphs
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.createPassInvalido import create_pass_invalido_cand
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.legalesInvalido import step_send_all_combinations_legals
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.loginNoValido import login_no_valido_cand, login_cand_bloqueado
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.namesInvalidos import step_names_invalid_cand
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.registro_invalido import register_invalid_candidate
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.telefonoNoValido import step_phone_invalid_candidate, step_verify_code_invalido_cand


def candidate_data_invalid():
    try:
        # Extraer datos del usuario
        name, last_name, _, birth_date, _ = data_user(env)

        # Pasos de prueba de datos inválidos del candidato
        steps = [
            ("login_no_valido_cand", login_no_valido_cand),
            ("login_cand_bloqueado", login_cand_bloqueado),
            ("register_invalid_candidate", register_invalid_candidate),
            ("create_pass_invalido_cand", create_pass_invalido_cand),
            ("step_send_all_combinations_legals", step_send_all_combinations_legals),
            ("step_phone_invalid_candidate", step_phone_invalid_candidate),
            ("step_verify_code_invalido_cand", step_verify_code_invalido_cand),
            ("step_names_invalid_cand", lambda headers: step_names_invalid_cand(headers, name, last_name, birth_date))
        ]

        # Ejecutar cada paso con manejo de parámetros
        headers = None
        results = []
        function_results = []
        for name, step in steps:
            if name == "register_invalid_candidate":
                _, headers, _, result = step()
            elif name == "step_names_invalid_cand":
                _, result = step(headers)
            elif headers is not None:
                _, result = step(headers)
            else:
                _, result = step()

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
            status_message = 'Se hicieron las pruebas de candidato con datos incorrectos de manera exitosa'
        else:
            status_message = 'No pasaron las pruebas de los datos inválidos del candidato'

        print(status_message)

        return status_message, total, function_results
    except Exception as e:
        print('No pasaron los datos inválidos del candidato', e)
        return 'No pasaron las pruebas de los datos inválidos del candidato', None









