import random

from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_names_candidate
from src.services.funciones import base, send_post_headers, nombres, apellidos

nombre = nombres()
apellidoP = apellidos()

myBody = [
    {
        "name": "",
        "lastName": "",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": "",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": "",
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": "!@#$%^&*()_+=-{}[]|;':\<>,.?/~`",
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": "!@#$%^&*()_+=-{}[]|;':\<>,.?/~`",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": "12345",
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": "12345",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

{
        "name": "Nombre demasiado largo muy muy muy pero de verdad muy largo para hacer una prueba a ver qeu resulta espero que este marqeu un error",
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": "Apellido demasiado largo muy muy muy pero de verdad muy largo para hacer una prueba a ver qeu resulta espero que este marqeu un error",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": "h",
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": "h",
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-32",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-13-23",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2040-12-23",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "1040-12-23",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000/12/23",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2023-01-01",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2023-01",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": " ",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": ""
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a0179344535345345",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },
{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "45435435345435345345345435354545"
    },

{
        "name": nombre,
        "lastName": apellidoP,
        "dateBirth": "2000-12-12",
        "areaId": "40288087797b055a01797b14e5f40036",
        "cityId": "2c9f936481969f0cccc996a00e092521"
    },

]


def names_cand400(headers, data, code):
    try:
        print('Se Envia la seccion de nombre de manera incorrecta')

        url = base + 'auth/registry/candidate/complete'
        respuesta = send_post_headers(url, headers, myBody, 200)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se mandas la seccion de nombres con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio el nombre del candidato {e}')
        return f'No se envio el nombre del candidato {e}'


def step_names_invalid_cand(headers):
    try:
        for data in myBody:
            names_cand400(headers, data, 400)
        step_names_candidate(headers)
        print('Se enviaron las prueba de nombres')
        return 'Se enviaron las prueba de nombres'
    except Exception as e:
        print(f'No se enviaron las prueba de nombres, {e}')
        return f'No se enviaron las prueba de nombres, {e}'

