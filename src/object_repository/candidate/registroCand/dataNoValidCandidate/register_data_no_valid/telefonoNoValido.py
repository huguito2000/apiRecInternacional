from src.services.catalogs import env
from src.services.peticiones_HTTP import base, send_post_headers_sin_body



data_payloads = [
    "",
    "vacio",
    "41111111114",
    "11",
    "hola",
    "12345678901",
    "!@#$%^&*()",
    "123 456 7890",
    "999999990"
]


def step_phone_invalid_candidate(headers):
    print('Se inicia el envio de teléfonos invalidos')
    global code
    try:
        print('Enviado numeros de telefono ...')
        url = env["URL_SERVER"] + 'auth/send-sms?phone='
        results = []
        for nums_variation in data_payloads:
            full_url = url + str(nums_variation) + '&phoneCode=%2B34'
            code = send_post_headers_sin_body(full_url, headers, 412)
            if code != 0:
                result = 1
                results.append(result)
                print(f"  - Se envió el teléfono: {nums_variation}")
                print('el codigo del número es: ' + str(code))
                print('\n')
            else:
                result = 0
                results.append(result)
                print(f"  - Se envió el teléfono: {nums_variation}")
                print('el codigo del número es: ' + str(code))
                print('\n')
        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            print('Se manda la sección de números de telefono icorrectos :) \n')
            return 'Se manda la sección de números de telefono icorrectos', 1
        else:
            print('fallo la prueba de telefonos invalidos:( \n')
            return 'fallo la prueba de telefonos invalidos:( ', 0
    except Exception as e:
        print('No se obtuvo el codigo :( \n', e)
        return 'No se obtuvo el codigo :(', 0


data_codes = [
    "",
    "no hay codigo",
    "12345678",
    "1111",
    "holaMundo",
    "!·$%&/()"
]


def step_verify_code_invalido_cand(headers):
    print('Inicia la verificacion del codigo\n')
    try:
        print('Enviado los codigos ...')
        url = env["URL_SERVER"] + 'auth/verify-code-sms?code='
        results = []
        for codes_variation in data_codes:
            full_url = url + str(codes_variation) +'&phone=999999990&phoneCode=%2B52'
            respuesta = send_post_headers_sin_body(full_url, headers, 412)
            if respuesta != 0:
                result = 1
                results.append(result)
                print(f"  - Se envió el codigo: {codes_variation}")
                print(respuesta, '\n')
            else:
                result = 0
                results.append(result)
                print(f"  - Se envió el codigo: {codes_variation}")
                print(respuesta, '\n')
        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            print('Se valida la seccion de verificar el codigo con datos incorrectos :)\n')
            return 'Se valida la seccion de verificar el codigo con datos incorrectos', 1
        else:
            print('No se verifico el codigo')
            return 'No se pudos hacer la verificación del codigo', 0
    except Exception as e:
        print(f'No se verifico el codigo {e}')
        return 'No se pudos hacer la verificación del codigo', 0

