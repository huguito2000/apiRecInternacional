from src.modules.Candidate.loginCand import login_cand, correo
from src.objectRepository.candidate.busqueda.busquedaDeVacantes import step_search_position, \
    step_search_salary, \
    step_search_workday, step_search_modality, step_search_type_contract, step_search_type_company, step_search_time


def search_vacancy():
    try:
        _, headers, _ = login_cand(correo)
        step_search_position(headers)
        step_search_salary(headers)
        step_search_workday(headers)
        step_search_modality(headers)
        step_search_type_contract(headers)
        step_search_type_company(headers)
        step_search_time(headers)
        print('Se realizo la prueba de busqueda de vacantes')
        return 'Se realizo las pruebas de la sección de busqueda de vacantes'
    except Exception as e:
        print('No paso la prueba de busqueda de vacantes', e)
        return 'No paso la prueba de busqueda de vacantes'
