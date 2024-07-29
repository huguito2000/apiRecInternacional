from src.modules.Candidate.busquedaVacantes import search_vacancy
from src.modules.Candidate.i_forgot_my_pass import i_forgot_password_candidate
from src.modules.Candidate.loginCand import login_cand, email_candidate, pass_email
from src.modules.Candidate.my_data_profile import my_data_profile
from src.modules.Candidate.postulacion import postulacion_candidato
from src.modules.Candidate.registerMyCV import register_cv
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.modules.Candidate.settings_candidate import settings_candidate
from src.modules.Candidate.testDatosNoValidos import candidate_data_invalid
from src.services.catalogs import generate_report_graphs, obtener_fecha, env, generate_report_graphs_complete
fecha = obtener_fecha()
reports = env["DIR_REPORTS"]


def all_report_graphs():
    try:

        email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]

        _, total, function_results = i_forgot_password_candidate()
        generate_report_graphs(total, function_results, 'Resultado de i_forgot_password_candidate',
                               reports + f'{reports}/olvide mi contraseña {fecha}.pdf')

        _, _, _, total, function_results = login_cand(email_candidate, pass_email)
        generate_report_graphs(total, function_results, 'Resultado de login_cand',
                               f'{reports}/reporte login candidato {fecha}.pdf')

        _, email_candidate2, total, function_results = register_onboarding_candidate()
        generate_report_graphs(total, function_results, 'Resultado de register_onboarding_candidate',
                               f'{reports}/registro onboarding {fecha}.pdf')

        _, email_candidate2, total, function_results = register_onboarding_candidate()
        _, total, function_results = register_cv(email_candidate2)
        generate_report_graphs(total, function_results, 'Resultado de register_cv',
                               f'{reports}/registro con cv {fecha}.pdf')

        _, email_candidate, total, function_results = register_complete_full_cv()
        generate_report_graphs(total, function_results, 'Resultado de register_complete_full_cv',
                               f'{reports}/registro con full cv {fecha}.pdf')

        _, _, _, total, function_results = postulacion_candidato(email_candidate)
        generate_report_graphs(total, function_results, 'Resultado de postulacion_candidato',
                               f'{reports}/postulación {fecha}.pdf')

        _, total, function_results = search_vacancy()
        generate_report_graphs(total, function_results, 'Resultado de search_vacancy',
                               f'{reports}/busqueda de vacantes {fecha}.pdf')

        _, total, function_results = my_data_profile()
        generate_report_graphs(total, function_results, 'Resultado de my_data_profile',
                               f'{reports}/mis datos {fecha}.pdf')

        _, total, function_results = settings_candidate()
        generate_report_graphs(total, function_results, 'Resultado de settings_candidate',
                               f'{reports}/configuración {fecha}.pdf')

        _, total, function_results = candidate_data_invalid()
        generate_report_graphs(total, function_results, 'Resultado de candidate_data_invalid',
                               f'{reports}/reporte candidato datos invalidos {fecha}.pdf')
    except Exception as e:
        print("No se generaron los reporte", e)


def report_graphs_complete():
    try:
        email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
        steps = [
            ("login_cand", login_cand),
            ("candidate_data_invalid", candidate_data_invalid),
            ("search_vacancy", search_vacancy),
            ("i_forgot_password_candidate", i_forgot_password_candidate),
            ("my_data_profile", my_data_profile),
            ("register_complete_full_cv", register_complete_full_cv),
            ("postulacion_candidato", postulacion_candidato),
            ("settings_candidate", settings_candidate)
        ]

        results = []
        function_results = []

        for name, step in steps:
            if name == "login_cand":
                _, _, _, _, result = step(email_candidate, pass_email)

            elif name == "register_complete_full_cv":
                _, email_candidate, _, result = step()

            elif name == "postulacion_candidato":
                _, _, _, _, result = step(email_candidate)

            else:
                _, _, result = step()

            # Manejar caso donde result es una lista de resultados
            if isinstance(result, list):
                for sub_result in result:
                    if isinstance(sub_result, tuple):
                        function_results.append(sub_result)
                        results.append(sub_result[1])
                    else:
                        function_results.append((name, sub_result))
                        results.append(sub_result)
            else:
                if isinstance(result, dict):
                    exito = result.get('exito', 0)
                    fallo = result.get('fallo', 0)
                    function_results.append((name, exito))
                    results.append(exito)
                else:
                    function_results.append((name, result))
                    results.append(result)

        print('Los resultados son:', results)

        # Asegurarse de que todos los resultados sean enteros
        resultados_int = [r if isinstance(r, int) else r.get('exito', 0) for r in results]
        casos = len(resultados_int)
        exito = sum(resultados_int)
        fallo = casos - exito
        print('Pasaron:', exito)
        print('Fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}

        if exito == casos:
            status_message = 'Se hicieron las pruebas de candidato con datos incorrectos de manera exitosa'
        else:
            status_message = 'No pasaron las pruebas de los datos inválidos del candidato'

        print(status_message)

        generate_report_graphs_complete(total, function_results, 'Resultado de happy path',
                                        f'{reports}/happy_path_{fecha}.pdf')

        return status_message
    except Exception as e:
        print('No se hizo el reporte', e)

