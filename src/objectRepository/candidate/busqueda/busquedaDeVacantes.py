from src.services.catalogs import env
from src.services.peticiones_HTTP import send_get_headers


url_base = env["URL_BUSCADOR"]


def step_search_position(headers):
    try:
        print('\nInicia la busqueda por posición\n')
        url = url_base + 'position=tester'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('\nSe realizo la busqueda por posición')
            return 'Se realizo la busqueda por posicion correctamente', 1
        else:
            print('No se realizo la busqueda por posicion')
            return 'No se realizo la busqueda', 0
    except Exception as e:
        print('No se realizo la busqueda por posicion', e)
        return 'No se realizo la busqueda'


def step_search_salary(headers):
    try:
        print('\nInicia la busqueda por salario\n')
        url = url_base + ('periodicitySalary=4028818e8e337efb018e338018c20004&currencyId'
                          '=2c9f9364867665940186849ddb990011')
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('\nSe realizo la busqueda por salario')
            return 'Se realizo la busqueda por salario correctamente', 1
        else:
            print('No se realizo la busqueda por salario')
            return 'No se realizo la busqueda por salario', 0
    except Exception as e:
        print('No se realizo la busqueda por salario', e)
        return 'No se realizo la busqueda por salario'


def step_search_workday(headers):
    try:
        print('\nInicia la busqueda por jornada laboral\n')
        url = url_base + 'workday=4028818e8e337efb018e33804ce40018'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('Se realizo la busqueda por jornada\n')
            return 'Se realizo la busqueda por jornada correctamente', 1
        else:
            print('no se realizo la busqueda por jornada\n')
            return 'No se realizo la busqieda por jornada', 0
    except Exception as e:
        print('no se realizo la busqueda por jornada', e)
        return 'No se realizo la busqieda por jornada'


def step_search_modality(headers):
    try:
        print('\nInicia la busqueda por modalidad\n')
        url = url_base + 'modality=4028818e8e337efb018e3380476c0016'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('Se realizo la busqueda por modalidad\n')
            return 'Se realizo la busqueda por modalidad correctamente', 1
        else:
            print('No se realizo la busqeida por modalidad\n')
            return 'No se realizo la busqeida por modalidad', 0
    except Exception as e:
        print('No se realizo la busqeida por modalidad\n', e)
        return 'No se realizo la busqeida por modalidad', 0


def step_search_type_contract(headers):
    try:
        print('\nInicia la busqueda por tipo de contrato\n')
        url = url_base + 'typeContract=4028818e8e3e1d59018e3e2095f30005'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('Se realizo la busqueda pro tipo de contrato\n')
            return 'Se realizo la busqueda por tipo de contrato correctamente', 1
        else:
            print('No se realizo la busqueda por tipo de contrato\n')
            return 'No se realizo la busqueda por tipo de contrato', 0
    except Exception as e:
        print('No se realizo la busqueda por tipo de contrato\n', e)
        return 'No se realizo la busqueda por tipo de contrato', 0


def step_search_type_company(headers):
    try:
        print('\nInicia la busqueda por tipo de compañia\n')
        url = url_base + 'typeCompany=4028818e8e337efb018e33801eba0007'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('Se realizo la busqueda por tipo de compañia\n')
            return 'Se realizo la busqueda por compañia correctamente', 1
        else:
            print('No se realizo la busqueda por tipo de compañia')
            return 'No se realizo la busqueda por tipo de compañia', 0
    except Exception as e:
        print('No se realizo la busqueda por tipo de compañia', e)
        return 'No se realizo la busqueda por tipo de compañia', 0


def step_search_time(headers):
    try:
        print('\nInicia la busqueda por fecha\n')
        url = url_base + 'time=ESTA_SEMANA'
        resultado = send_get_headers(url, headers, 200)
        if resultado != 0:
            print('Se realizo la busqueda por fecha\n')
            return 'Se realizo la busqueda por fecha correctamente', 1
        else:
            print('No se realizo la busqueda por fecha\n')
            return 'No se realizo la busqueda por fecha', 0
    except Exception as e:
        print('No se realizo la busqueda por fecha\n', e)
        return 'No se realizo la busqueda por fecha', 0
