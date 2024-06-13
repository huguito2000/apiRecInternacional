import os
from datetime import date, timedelta, datetime
import requests
import json
import random
from json import loads
from dotenv import dotenv_values

from src.services.peticiones_HTTP import send_get_headers, send_get

env = dotenv_values("/etc/.env")


def nombres():
    Nombres = ['Hugo', 'Dennis', 'Miguel', 'Gabriel', 'Javi', 'Lucio', 'Jesus', 'Victor', 'Abraham', 'Juan', 'Rafael',
               'Ramiro', 'Pedro', 'Julian', 'Valentin', 'Camilo', 'Andrés', 'Gerard', 'Ana', 'Leo', 'Sara', 'Nora',
               'Laura']
    nombre = random.choice(Nombres)
    print(nombre)
    return nombre


def apellidos():
    Apellido = ['Álvarez', 'Castillo', 'De León', 'Díaz', 'Espinoza', 'Fernández', 'García', 'Salazar', 'Santana',
                'Zambrano', 'Perez', 'Rodriguez', 'Martinez', 'Garcia', 'Torres', 'Olivera', 'Lopez', 'Sanchez',
                'Ascarragan', 'Hernandez', 'Hernández', 'García', 'Martínez', 'López', 'González', 'Pérez', 'Rodríguez',
                'Sánchez', 'Aguilar', 'Juárez', 'Ortiz', 'Álvarez', 'Chávez', 'Castillo', 'Rivera', 'Moreno']
    Apellidos = random.choice(Apellido)
    print(Apellidos)
    return Apellidos


ruta = ''


def get_ruta():
    img_ruta = os.getcwd().split('/')
    print(len(img_ruta))
    base_img = ''
    for i in range(len(img_ruta)):
        base_img = base_img + str(img_ruta[i]) + '/'
    print(base_img)
    return base_img


def foto():
    global ruta
    base_img = get_ruta()
    imagen = random.randint(0, 10)
    print(imagen)
    ruta = (base_img + 'resources/img/' + str(imagen) + '.jpeg')
    print(ruta)
    return ruta


def subir_archivo(ruta_archivo, url, headers, code_http):
    files = {'file': open(ruta_archivo, 'rb')}
    req = requests.post(url, headers=headers, files=files)
    print('post status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == code_http


def eliminar_foto(url, headers, code_http):
    req = requests.delete(url, headers=headers)
    print('delete status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == code_http


def pdfs():
    global ruta_pdf
    base = get_ruta()
    pdf = ['alberto', 'carlos', 'cristian', 'daniel', 'diana', 'mario', 'octavio', 'romero']
    aleatorio = random.choice(pdf)
    print(aleatorio)
    ruta_pdf = (base + 'resources/pdf/' + str(aleatorio) + '.pdf')
    print("la ruta es " + ruta_pdf)
    return ruta_pdf


def salary_min():
    sueldo_min = str(random.randint(200, 25000))
    print(sueldo_min)
    return sueldo_min


def salary_max():
    sueldo_max = str(random.randint(25001, 45000))
    print(sueldo_max)
    return sueldo_max


def position():
    puesto = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
    aleatorio = random.choice(puesto)
    print(aleatorio)
    return aleatorio


def datos_json(enviroment):
    with open(enviroment["RESOURCES_DIR"] + "data.json", "r", encoding="utf-8") as jsonFile:
        json_data = json.load(jsonFile)
    return json_data


def get_ramdom_name(json_data, gender):
    key_map = ("namesM", "namesF")[gender == "M"]
    return (json_data[key_map][random.randint(0, len(json_data[key_map]) - 1)]).capitalize()


def get_ramdom_last_name(json_data):
    return (json_data["lastNames"][random.randint(0, len(json_data["lastNames"]) - 1)]).capitalize()


def get_birth_date(is_valid):
    date_start = date(1990, 1, 1)
    date_end = date(2005, 12, 31)

    if not is_valid:
        date_start = date(2018, 1, 1)
        date_end = date(2023, 12, 31)

    randay = random.randrange((date_end - date_start).days)
    return date_start + timedelta(days=randay)


def get_email_by_name(name, last_name, second_last_name, birth_date: date):
    return normalize(
        (name[0:2] + last_name[0:2] + second_last_name + "." + str(birth_date.year) + "@yopmail.com").lower())


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def data_user(env):
    gender = ['M', 'F']
    genero = random.choices(gender)
    json_data = datos_json(env)
    name = get_ramdom_name(json_data, genero)
    last_name = get_ramdom_last_name(json_data)
    second_last_name = get_ramdom_last_name(json_data)
    birth_date = get_birth_date(True)
    correo = get_email_by_name(name, last_name, second_last_name, birth_date)
    return name, last_name, second_last_name, birth_date, correo


def obtener_fecha():
    now = datetime.now()
    fecha = str(now.strftime('%d del %m del %Y a las %H:%M'))
    return fecha


def get_password(name, last_name, second_last_name, birth_date: date):
    return (name[0:2] + last_name[0:2] + second_last_name + "" + str(birth_date.year) + ".").capitalize()


def get_ramdom_nationality():
    response = requests.get(env["URL_SERVER"] + "management/catalog/nationality")
    json_dict = loads(response.text)
    nationality = json_dict[random.randint(0, len(json_dict) - 1)]
    return nationality


def get_states():
    paises = ['ES', 'CO', 'MX']
    pais = random.choice(paises)
    print(pais)
    url = env["URL_SERVER"] + 'management/catalog/state?countryCode=' + pais
    print(url)
    respuesta = requests.get(url)
    json_dict = loads(respuesta.text)
    num = random.randrange(len(json_dict))
    iso2 = json_dict[num]["iso2"]
    # Print the result
    print(iso2)
    return pais, iso2


def get_ramdom_city():
    pais, iso2 = get_states()
    response = requests.get(env["URL_SERVER"] + "management/catalog/city?countryCode=" + pais +"&stateCode=" + iso2)
    json_dict = loads(response.text)
    num = random.randrange(len(json_dict))
    print(num)
    city = json_dict[random.randint(0, len(json_dict) - 1)]
    return city


def get_area_catalogs(headers):
    url = env["URL_SERVER"] + "management/catalog/area"
    response: list = send_get_headers(url, headers, 200)
    try:
        num = random.randint(0, 10)
        area = response[num]['areaId']
        print('se optiene el area id:\n', area)
        return area
    except (json.JSONDecodeError, KeyError) as e:
        print(f'Error al obtener areaIds :( \n: {e}')


def get_nacionality():
    url = env["URL_SERVER"] + "management/catalog/nationality"
    response: list = send_get(url, 200)
    num = random.randint(0, 100)
    nationality_id = response[num]['nationalityId']
    return nationality_id



