import random
from src.services.funciones import base, foto, subir_archivo, send_post_headers, send_delete


def logo_client(client_id, headers):
    try:
        url_client_foto = base + 'files/upload/client-logo?clientId=' + client_id
        ruta = foto()
        print(ruta)
        subir_archivo(ruta, url_client_foto, headers, 200)
        print('Se subio la foto del cliente')
        return 'Se subio la foto del cliente'
    except Exception as e:
        print('No se subio la foto del cliente', {e})
        return 'No se subio la foto del cliente'


def step_new_client(headers):
    try:
        name = random.randrange(1, 100)
        name = 'involver' + str(name)
        cliente = {
            "name": name,
            "industryId": "40288088798a3b0501798a58ca500059",
            "employees": "DE51A250",
            "countryId": "2c9f936481969f0aaaa996a00e090002",
            "currencyId": "2c9f9364867665940186849ddb990011",
            "typeCompanyId": "4028818e8e337efb018e33801eba0007",
            "zipCode": "56615",
            "legalName": "involver sa de cv",
            "address": "madrid",
            "legalId": "A12345678"
        }
        url_cliente = base + 'user/client'
        print(url_cliente)
        client = send_post_headers(url_cliente, headers, cliente, 200)
        client_id = client['clientId']
        logo_client(client_id, headers)
        print('\n se creo un nuevo cliente con el id', client_id)
        return client_id
    except Exception as e:
        print('\n No se creo el cliente', {e})
        return 'No se creo el cliente'


def step_delete_client(headers):
    try:
        url_cliente = base + 'user/client'
        client_id = step_new_client(headers)
        my_body: list = [client_id]
        send_delete(url_cliente, headers, my_body, 200)
        print('se elimino el cliente')
        return 'Se elimino el cliente'
    except Exception as e:
        print('\n No se elimino el cliente', {e})
        return 'No se elimino el cliente'





