import random
from src.services.catalogs import foto, subir_archivo, env
from src.services.peticiones_HTTP import send_post_headers, send_delete, send_post_headers_sin_body, send_get_headers


def logo_client(client_id, headers):
    try:
        url_client_foto = env["URL_SERVER"] + 'files/upload/client-logo?clientId=' + client_id
        ruta = foto()
        print(ruta)
        resultado = subir_archivo(ruta, url_client_foto, headers, 200)
        if resultado != 0:
            print('Se subio la foto del cliente')
            return 'Se subio la foto del cliente', 1
        else:
            print('No se subio la foto del cliente')
            return 'No se subio la foto del cliente', 0

    except Exception as e:
        print('No se subio la foto del cliente', {e})
        return 'No se subio la foto del cliente'


def step_new_client(headers):
    try:
        name = random.randrange(1, 100)
        name = 'involver' + str(name)
        cliente = {
            "name": name,
            "industryId": "40288088798a3b0501798a589eb30035",
            "employees": "DE51A250",
            "countryId": "2c9f936481969f0aaaa996a00e090002",
            "currencyId": "2c9f9364867665940186849ddb990011",
            "typeCompanyId": "4028818e8e337efb018e3380223e0008",
            "zipCode": "12345",
            "legalName": "demo",
            "address": "madrid",
            "legalId": "A12345678"
        }
        url_cliente = env["URL_SERVER"] + 'user/client'
        print(url_cliente)
        client = send_post_headers(url_cliente, headers, cliente, 200)
        if client != 0:
            client_id = client['clientId']
            logo_client(client_id, headers)
            print('\n se creo un nuevo cliente con el id', client_id)
            return client_id, 1
        else:
            print('No se creo el nuevo cliente')
            return 'No se creo el nuevo cliente', 0
    except Exception as e:
        print('\n No se creo el cliente', {e})
        return 'No se creo el cliente'


def step_delete_client(headers):
    try:
        url_cliente = env["URL_SERVER"] + 'user/client'
        client_id = step_new_client(headers)
        my_body = [client_id[0]]
        respuesta = send_delete(url_cliente, headers, my_body, 200)
        if respuesta != 0:
            print('se elimino el cliente')
            return 'Se elimino el cliente', 1
        else:
            print('No se elimino el cliente')
            return 'No se elimino el cliente', 0
    except Exception as e:
        print('\n No se elimino el cliente', {e})
        return 'No se elimino el cliente', 0


def change_cupon(headers, client_id):
    try:
        url = env["URL_SERVER"] + 'management/discounts/redeem?code=freehugointer&clientId=' + client_id
        print('\n', url)
        respuesta = send_post_headers_sin_body(url, headers, 200)
        if respuesta != 0:
            print(respuesta)
            return respuesta, 1
        else:
            print('No se canjeo el cupón')
            return 'No se canjeo el cupón', 0

    except Exception as e:
        print('No se pudo hacer el canje del cupón', e)
        return 'No se pudo realizar el canje del cupón', 0


def get_client(headers):
    try:
        url = env["URL_SERVER"] + 'user/client/page?pageNumber=0&pageSize=10&sortBy=creationDate&sortDirection=DESC'
        response = send_get_headers(url, headers, 200)
        client_id = str(response["content"][0]["clientId"])
        print('el client is es: ', client_id)
        return client_id
    except Exception as e:
        print('No se pudo obtener el client id', e)
        return 'NO se pudo obtener el client id'

