from src.modules.recruiter.login_recruiter import login_recruiter, email, pass_email
from src.object_repository.recruiter.create_vacant.obj_vacanteIA import vacante_ia
from src.object_repository.recruiter.create_vacant.obj_vacanteManual1 import position_title
from src.object_repository.recruiter.create_vacant.obj_vacanteManual2 import job_description
from src.object_repository.recruiter.create_vacant.obj_vacanteManual3 import job_skills, contract_conditions
from src.object_repository.recruiter.create_vacant.obj_vacanteManual4 import question_soft_skill, video_psicometricas, \
    review_vacant, post_vacancy


def create_manual_vacant():
    try:
        print('Inicia la creación de la vacante manual')
        _, headers, recruiter_id, total, _ = login_recruiter(email, pass_email)
        global vacant_id
        steps = [
            ("position_title", position_title),

            ("job_description", job_description),

            ("contract_conditions", contract_conditions),

            ("job_skills", job_skills),

            ("question_soft_skill", question_soft_skill),

            ("video_psicometricas", video_psicometricas),

            ("review_vacant", review_vacant),

            ("post_vacancy", post_vacancy)

        ]

        results = []
        function_results = [("login_recruiter", total['exito'])]
        for name, step in steps:
            if name == "position_title":
                _, vacant_id, result = step(headers)
            elif name == "review_vacant":
                _, result = step(vacant_id, headers, recruiter_id)
            else:
                _, result = step(vacant_id, headers)
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
            status_message = 'Se publico la vacante manual :)\n'
        else:
            status_message = 'No se publico la vacante manual \n'

        print(status_message)
        return status_message, total, function_results
    except Exception as e:
        print('\n No se creo la vacante manual :(', e)
        return 'No se creo la vacante manual'


def create_vacant_ia():
    try:
        print('Inicia la creación de vacante por IA')
        _, headers, _, total, _ = login_recruiter(email, pass_email)
        steps = [
            ("vacante_ia", vacante_ia)
        ]

        results = []
        function_results = [("login_recruiter", total['exito'])]
        for name, steps in steps:
            _, result = steps(headers)
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
            status_message = 'Se publico la vacante con IA :)\n'
        else:
            status_message = 'No se publico la vacante con IA \n'

        print(status_message)
        return status_message, total, function_results
    except Exception as e:
        print('No se creo la vacante con IA', e)
        return 'No se creo la vacantre con IA'
