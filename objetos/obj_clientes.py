import random
from objetos.funciones import base, sendPostHeaders, sendDelete, foto, subirArchivo
from test.login import login


def fotoCliente(clientId, headers):
    try:
        urlClientFoto = base + 'files/upload/client-logo?clientId=' + clientId
        ruta = foto()
        print(ruta)
        subirArchivo(ruta, urlClientFoto, headers, 200)
        print('Se subio la foto del cliente')
        return 'Se subio la foto del cliente'
    except Exception as e:
        print('No se subio la foto del cliente', e)
        return 'No se subio la foto del cliente'
def newClient(headers):
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
        urlCliente = base + 'user/client'
        print(urlCliente)
        client = sendPostHeaders(urlCliente, headers, cliente, 200)
        clientId = client['clientId']
        fotoCliente(clientId, headers)
        print('\n se creo un nuevo cliente con el id', clientId)
        return clientId
    except Exception as e:
        print('\n No se creo el cliente', e)
        return 'No se creo el cliente'

def eliminarCliente(headers):
    try:
        urlCliente = base + 'user/client'
        clientId = newClient(headers)
        myBody: list = [clientId]
        sendDelete(urlCliente, headers, myBody, 200)
        print('se elimino el cliente')
        return 'Se elimino el cliente'
    except Exception as e:
        print('\n No se elimino el cliente', e)
        return 'No se elimino el cliente'





