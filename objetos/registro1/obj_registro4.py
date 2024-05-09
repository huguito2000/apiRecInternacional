from objetos.funciones import base, sendPostHeaders

def registro4(headers):
    try:
        url = base + 'auth/registry/recruiter/complete'
        myBody = {
            "name": "hugo",
            "lastName": "rodriguez",
            "companyName": "involve",
            "industryId": "40288088798a3b0501798a58c2cf0053",
            "invoiceNotification": True,
            "countryId": "2c9f936481969f0aaaa996a00e090001"
        }
        sendPostHeaders(url, headers, myBody, 200)
        print('Se manda el paso 4 del registro')
        return 'Se mando el paso 4 del registro'
    except Exception as e:
        print('No se mando el paso 4', e)
        return 'No se mando el paso 4 '
