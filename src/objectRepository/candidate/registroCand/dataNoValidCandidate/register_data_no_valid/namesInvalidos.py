from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_names_candidate
from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import send_post_headers

name, last_name, _, birth_date, email_candidate = data_user(env)

myBody = [
    {
        "name": "",
        "lastName": "",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": "",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": "",
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": "!@#$%^&*()_+=-{}[]|;':\<>,.?/~`",
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": "!@#$%^&*()_+=-{}[]|;':\<>,.?/~`",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": "12345",
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": "12345",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

    {
        "name": "Nombre demasiado largo muy muy muy pero de verdad muy largo para hacer una prueba a ver qeu resulta "
                "espero que este marqeu un error",
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": "Apellido demasiado largo muy muy muy pero de verdad muy largo para hacer una prueba a ver que "
                    "resulta espero que este marque un error",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": "h",
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": "h",
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": "2000/12/23",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

    {
        "name": name,
        "lastName": last_name,
        "dateBirth": "2023-01-01",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": "2023-01",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": "",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": " ",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": ""
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a0179344535345345",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "45435435345435345345345435354545"
    },

    {
        "name": name,
        "lastName": last_name,
        "dateBirth": str(birth_date),
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

]


def names_cand400(headers, data, code):
    try:
        print('Se Envia la sección de nombre de manera incorrecta')

        url = env["URL_SERVER"] + 'auth/registry/candidate/complete'
        respuesta = send_post_headers(url, headers, myBody, 400)
        if respuesta != 0:
            print(f"Resultado con datos: {data}, código: {code}")
            print(f'Se mandas la seccion de nombres con respuesta {respuesta}')
            return 'Se realiza la prueba de mandar los nombres errorneos de manera exitosa', 1
        else:
            print('No se envio el nombre del candidato')
            return 'No se envio el nombre del candidato', 0
    except Exception as e:
        print(f'No se envio el nombre del candidato {e}')
        return 'No se envio el nombre del candidato', 0


def step_names_invalid_cand(headers, name, last_name, birth_date):
    try:
        print('Inicia el envio de nombres con datos incorrectos\n')
        results = []
        for data in myBody:
            _, result = names_cand400(headers, data, 400)
            results.append(result)
            print('\n')
        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            step_names_candidate(headers, name, last_name, birth_date)
            print('Se enviaron las prueba de nombres invalidos :) \n')
            return 'Se realizo la pruebas de envio de nombres incorrectos y paso de manera correcta', 1
        else:
            step_names_candidate(headers, name, last_name, birth_date)
            print('No se enviaron las prueba de nombres :( \n')
            return 'No se realizo la prueba de nombres icorrectos', 0
    except Exception as e:
        print('No se enviaron las prueba de nombres :( \n', e)
        return 'No se realizo la prueba de nombres icorrectos', 0
