from src.services.peticiones_HTTP import send_get_headers

url_base = ('https://searchvacant.qa.ia.involverh.es/search-vacancy/search-vacancies/?offset=0&limit=10&countryId'
            '=2c9f936481969f0aaaa996a00e090002&')


def step_search_position(headers):
    try:
        url = url_base + 'position=tester'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por posición')
    except Exception as e:
        print('No se realizo la busqueda por posicion', e)
        return 'no se realizo la busqueda'


def step_search_salary(headers):
    try:
        url = url_base + ('periodicitySalary=4028818e8e337efb018e338018c20004&currencyId'
                          '=2c9f9364867665940186849ddb990011')
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqeuda por salario')
    except Exception as e:
        print('No se realizo la busqueda por salario', e)
        return 'No se realizo la busqueda por salario'


def step_search_workday(headers):
    try:
        url = url_base + 'workday=4028818e8e337efb018e33804ce40018'
        send_get_headers(url, headers, 200)
        print('\nse realizo la busqueda por jornada')
    except Exception as e:
        print('no se realizo la busqueda por jornada', e)
        return 'No se realizo la busqieda por jornada'


def step_search_modality(headers):
    try:
        url = url_base + 'modality=4028818e8e337efb018e3380476c0016'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por modalidad')
    except Exception as e:
        print('No se realizo la busqeida por modalidad', e)


def step_search_type_contract(headers):
    try:
        url = url_base + 'typeContract=4028818e8e3e1d59018e3e2095f30005'
        send_get_headers(url, headers, 200)
        print('\nse realizo la busqueda pro tipo de contrato')
    except Exception as e:
        print('No se realizo la busqueda por tipo de contrato', e)
        return 'No se realizo la busqueda por tipo de contrato'


def step_search_type_company(headers):
    try:
        url = url_base + 'typeCompany=4028818e8e337efb018e33801eba0007'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por tipo de compañia')
    except Exception as e:
        print('No se realizo la busqueda por tipo de compañia', e)
        return 'No se realizo la busqueda por tipo de compañia'


def step_search_time(headers):
    try:
        url = url_base + 'time=ESTA_SEMANA'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por fecha')
    except Exception as e:
        print('No se realixo la busqueda por fecha', e)
        return 'No se realizo la busqueda por fecha'
