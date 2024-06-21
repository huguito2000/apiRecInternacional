import os
from datetime import date, timedelta, datetime
import requests
import json
import random
from json import loads
from dotenv import dotenv_values
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from src.services.peticiones_HTTP import send_get_headers, send_get

env = dotenv_values("etc/.env")


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


def videos():
    global ruta
    base_img = get_ruta()
    video = random.randint(1, 2)
    ruta = (base_img + 'resources/video/' + str(video) + '.mp4')
    print(ruta)
    return ruta


def subir_archivo(ruta_archivo, url, headers, code_http):
    files = {'file': open(ruta_archivo, 'rb')}
    req = requests.post(url, headers=headers, files=files)
    print('post status: ' + str(req.status_code))
    if req.status_code == code_http:
        print('Se subio el archivo correctamente')
        return 1
    else:
        return 0


def eliminar_foto(url, headers, code_http):
    req = requests.delete(url, headers=headers)
    print('delete status: ' + str(req.status_code))
    if req.status_code == code_http:
        print('Se elimino el arhivo')
        return 1
    else:
        return 0


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


def generate_report_graphs(results, function_results, title_report='Resultados de las pruebas datos', report_filename='reports/reporte_pruebas.pdf'):
    try:
        """
        Genera un reporte en PDF con gráficos basados en los resultados de las pruebas y los nombres de las funciones.
    
        :param results: Diccionario con los resultados generales de las pruebas. Ejemplo: {"exito": 5, "fallo": 2}
        :param function_results: Lista de tuplas con los nombres de las funciones y sus resultados. Ejemplo: [("funcion1", True), ("funcion2", False)]
        :param report_filename: Nombre del archivo PDF que se generará. Por defecto es 'reporte_pruebas.pdf'.
        """
        labels = list(results.keys())
        sizes = list(results.values())
        colors = ['lightgreen', 'lightcoral']
        explode = (0.1, 0)  # Solo "explota" el primer segmento

        fig, ax = plt.subplots(figsize=(8, 8))

        # Crear el gráfico de pastel
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.axis('equal')  # Para asegurar que el pie es un círculo

        plt.title(title_report)
        plt.tight_layout()

        # Agregar los nombres de las funciones y sus resultados debajo del gráfico
        function_text = 'Funciones utilizadas:\n' + '\n'.join([f"{name}: {'Éxito' if result else 'Fallo'}" for name, result in function_results])
        plt.figtext(0.5, 0.05, function_text, wrap=True, horizontalalignment='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

        plt.savefig(report_filename)
    except Exception as e:
        print('No se genero el reporte con grafica', e)


def generate_report_graphs_complete(results, function_results, title, report_filename):
    """
    Genera un reporte en PDF con gráficos basados en los resultados de las pruebas y los nombres de las funciones.

    :param results: Diccionario con los resultados generales de las pruebas. Ejemplo: {"exito": 5, "fallo": 2}
    :param function_results: Lista de tuplas con los nombres de las funciones y sus resultados. Ejemplo: [("funcion1", True), ("funcion2", False)]
    :param title: Título del gráfico.
    :param report_filename: Nombre del archivo PDF que se generará.
    """
    labels = list(results.keys())
    sizes = list(results.values())
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # Solo "explota" el primer segmento

    fig, ax = plt.subplots(figsize=(8, 8))

    # Crear el gráfico de pastel
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=90)
    ax.axis('equal')  # Para asegurar que el pie es un círculo

    plt.title(title)
    plt.tight_layout()

    # Guardar el gráfico en un archivo PDF
    with PdfPages(report_filename) as pdf:
        pdf.savefig(fig)

        # Dividir los resultados en bloques manejables
        chunk_size = 30  # Número de filas por página
        for i in range(0, len(function_results), chunk_size):
            fig, ax = plt.subplots(figsize=(10, 12))
            ax.axis('tight')
            ax.axis('off')

            chunk = function_results[i:i + chunk_size]
            table_data = [['#', 'Función', 'Resultado']] + [[str(i + 1 + j), name, 'Éxito' if result else 'Fallo'] for
                                                            j, (name, result) in enumerate(chunk)]
            table = ax.table(cellText=table_data, cellLoc='center', loc='center')
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 1.2)

            pdf.savefig(fig)