from dotenv import dotenv_values
from src.services.peticiones_HTTP import send_get_headers

env = dotenv_values("etc/.env")
url_base = env["URL_BUSCADOR"]


def step_search_position(headers):
    try:
        url = url_base + 'position=tester'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por posición')
        return 'Se realizo la busqueda por posicion correctamente'
    except Exception as e:
        print('No se realizo la busqueda por posicion', e)
        return 'No se realizo la busqueda'


def step_search_salary(headers):
    try:
        url = url_base + ('periodicitySalary=4028818e8e337efb018e338018c20004&currencyId'
                          '=2c9f9364867665940186849ddb990011')
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por salario')
        return 'Se realizo la busqueda por salario correctamente'
    except Exception as e:
        print('No se realizo la busqueda por salario', e)
        return 'No se realizo la busqueda por salario'


def step_search_workday(headers):
    try:
        url = url_base + 'workday=4028818e8e337efb018e33804ce40018'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por jornada')
        return 'Se realizo la busqueda por jornada correctamente'
    except Exception as e:
        print('no se realizo la busqueda por jornada', e)
        return 'No se realizo la busqieda por jornada'


def step_search_modality(headers):
    try:
        url = url_base + 'modality=4028818e8e337efb018e3380476c0016'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por modalidad')
        return 'Se realizo la busqueda por modalidad correctamente'
    except Exception as e:
        print('No se realizo la busqeida por modalidad', e)


def step_search_type_contract(headers):
    try:
        url = url_base + 'typeContract=4028818e8e3e1d59018e3e2095f30005'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda pro tipo de contrato')
        return 'Se realizo la busqueda por tipo de contrato correctamente'
    except Exception as e:
        print('No se realizo la busqueda por tipo de contrato', e)
        return 'No se realizo la busqueda por tipo de contrato'


def step_search_type_company(headers):
    try:
        url = url_base + 'typeCompany=4028818e8e337efb018e33801eba0007'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por tipo de compañia')
        return 'Se realizo la busqueda por compañia correctamente'
    except Exception as e:
        print('No se realizo la busqueda por tipo de compañia', e)
        return 'No se realizo la busqueda por tipo de compañia'


def step_search_time(headers):
    try:
        url = url_base + 'time=ESTA_SEMANA'
        send_get_headers(url, headers, 200)
        print('\nSe realizo la busqueda por fecha')
        return 'Se realizo la busqueda por fecha correctamente'
    except Exception as e:
        print('No se realixo la busqueda por fecha', e)
        return 'No se realizo la busqueda por fecha'
