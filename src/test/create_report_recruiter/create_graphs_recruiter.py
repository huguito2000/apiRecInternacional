from src.modules.recruiter.change_cupon import change_cupon_client
from src.modules.recruiter.clients import customer_section
from src.modules.recruiter.create_vacancy_recruiter import create_manual_vacant, create_vacant_ia
from src.modules.recruiter.i_forgot_my_pass_recruiter import i_forgot_pass_my_recruiter
from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.modules.recruiter.register_recruiter import register_recruiter
from src.modules.recruiter.settings_recruiter import settings
from src.services.catalogs import obtener_fecha, env, generate_report_graphs, generate_report_graphs_complete

fecha = obtener_fecha()
reports = env["DIR_REPORTS"]


def all_reports_recruiter():
    try:

        _, _, _, total, function_results = login_recruiter(email, pass_email)
        generate_report_graphs(total, function_results, 'Resultado de login_recruiter',
                               f'{reports}/reporte login reclutador {fecha}.pdf')

        _, total, function_results = i_forgot_pass_my_recruiter()
        generate_report_graphs(total, function_results, 'Resultado de i_forgot_pass_my_recruiter',
                               f'{reports}/reporte olvide mi contraseña reclutador {fecha}.pdf')

        _, total, function_results = register_recruiter()
        generate_report_graphs(total, function_results, 'Resultado de registro reclutador',
                               f'{reports}/reporte registro reclutador {fecha}.pdf')

        _, total, function_results = customer_section()
        generate_report_graphs(total, function_results, 'Resultado de customer_section',
                               f'{reports}/reporte seccion de clientes {fecha}.pdf')

        _, total, function_results = change_cupon_client()
        generate_report_graphs(total, function_results, 'Resultado de change_cupon_client',
                               f'{reports}/reporte seccion de canje de cupon {fecha}.pdf')

        _, total, function_results = settings()
        generate_report_graphs(total, function_results, 'Resultado de settings_recruiter',
                               f'{reports}/reporte seccion de ajustes del reclutador {fecha}.pdf')

        _, total, function_results = create_manual_vacant()
        generate_report_graphs(total, function_results, 'Resultado de create_vacant',
                               f'{reports}/reporte seccion de crear vacante manual {fecha}.pdf')

        _, total, function_results = create_vacant_ia()
        generate_report_graphs(total, function_results, 'Resultado de create_vacant_IA',
                               f'{reports}/reporte seccion de crear vacante IA {fecha}.pdf')

        print('Se generan todos los resportes de reclutador')

    except Exception as e:
        print('No se generaron los reportes de reclutador', e)


def report_complete_recruiter():
    try:
        print('inicia el reporte completo del reclutador')
        steps = [
            ("login_recruiter", login_recruiter),
            ("i_forgot_pass_my_recruiter", i_forgot_pass_my_recruiter),
            ("register_recruiter", register_recruiter),
            ("customer_section", customer_section),
            ("change_cupon_client", change_cupon_client),
            ("settings", settings),
            ("create_manual_vacant", create_manual_vacant),
            ("create_vacant_ia", create_vacant_ia),
        ]

        results = []
        function_results = []
        for name, step in steps:
            if name == "login_recruiter":
                _, _, _, _, result = step(email, pass_email)
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

        # Calcular éxito
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        total = {"exito": exito, "fallo": fallo}

        if exito == casos:
            status_message = 'Se creo el reporte completo de reclutador :)\n'
        else:
            status_message = 'No se creo el reporte completo de reclutador \n'

        print(status_message)

        generate_report_graphs_complete(total, function_results, 'Resultado de happy path reclutador',
                                        f'{reports}/happy path reclutador {fecha}.pdf')
        return status_message

    except Exception as e:
        print('No se genero el reporte completo', e)

