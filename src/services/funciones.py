# pip3 install requests
# source venv/bin/activate
import os
import random
import requests

base = 'https://pre.micros.involverh.es/'


# base = 'https://stage.micros.involverh.es/'

def send_get(url, headers, codeHttp: int):
    try:
        req = requests.get(url, headers=headers)
        if req.status_code != codeHttp:
            raise Exception(f"comprueba el status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            print(f"Response: {result}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("la respuesta no un JSON  valido" + result)
            print('get status: ' + str(req.status_code))
        assert req.status_code == codeHttp
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_post(url, myBody, codeHttp):
    try:
        req = requests.post(url, json=myBody)
        print('Post status:' + str(req.status_code))
        print(req.json())

        # Check if codeHttp is a single value or a range
        if isinstance(codeHttp, int):
            # Assert for exact code
            assert req.status_code == codeHttp
        else:
            # Assert for range using tuple unpacking
            min_code, max_code = codeHttp
            assert min_code <= req.status_code <= max_code

        resultado = req.json()
        headers = req.headers
        return resultado, headers
    except Exception as e:
        print('No paso el post', {e})


def send_patch(url, headers, myBody, codeHttp):
    try:
        req = requests.patch(url, headers=headers, json=myBody)
        print('Patch status: ' + str(req.status_code))
        print(req.json())
        assert req.status_code == codeHttp
    except Exception as e:
        print('No paso el patch', {e})


def send_put(url, headers, codeHttp):
    try:
        req = requests.put(url, headers=headers)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == codeHttp
        code = req.status_code
        return code
    except Exception as e:
        print('no paso la funcion put', {e})


def send_put_body(url, headers, myBody, codeHttp):
    try:
        req = requests.put(url, headers=headers, json=myBody)
        print(req.content)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == codeHttp
    except Exception as e:
        print('no paso la funcion put', {e})


def send_post_sin_body(url, codeHttp):
    try:
        req = requests.post(url)
        print('Post Sin body status: ' + str(req.status_code))
        print(req.json())
        assert req.status_code == codeHttp
    except Exception as e:
        print(' no paso el post', {e})


def send_post_headers_sin_body(url, headers, codeHttp):
    try:
        req = requests.post(url, headers=headers)
        if req.status_code != codeHttp:
            raise Exception(f"Unexpected status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            print(f"Response: {result}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("The response is not valid JSON " + result)
            print('Post status: ' + str(req.status_code))

        assert req.status_code == codeHttp
        return result
    except Exception as e:
        print(f"Error: {e}")


def send_post_headers(url, headers, myBody, codeHttp):
    try:
        # Send the POST request
        req = requests.post(url, headers=headers, json=myBody)
        # Check the response status code
        if req.status_code != codeHttp:
            raise Exception(f"Unexpected status code: {req.status_code}")
        # Try to decode the JSON response
        try:
            result = req.json()
            print(f"Status Code: {req.status_code}")
            print(f"Response: {result}")
            return result
        except requests.exceptions.JSONDecodeError:
            result = req.text
            print("The response is not valid JSON " + result)
            print('Post status: ' + str(req.status_code))

        assert req.status_code == codeHttp

    except Exception as e:
        print(f"Error: {e}")


def send_delete(url, headers, myBody, codeHttp):
    try:
        req = requests.delete(url, headers=headers, json=myBody)
        print('Patch status: ' + str(req.status_code))
        print(req.json())
        assert req.status_code == codeHttp
        resultado = req.json()
        return resultado
    except Exception as e:
        print('No paso el delete', {e})


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
    imgRuta = os.getcwd().split('/')
    print(len(imgRuta))
    baseImg = ''
    for i in range(len(imgRuta)):
        baseImg = baseImg + str(imgRuta[i]) + '/'
    print(baseImg)
    return baseImg


def foto():
    global ruta
    baseImg = get_ruta()
    imagen = random.randint(0, 10)
    print(imagen)
    ruta = (baseImg + 'resources/img/' + str(imagen) + '.jpeg')
    print(ruta)
    return ruta


def subir_archivo(rutaArchivo, url, headers, codeHttp):
    files = {'file': open(rutaArchivo, 'rb')}
    req = requests.post(url, headers=headers, files=files)
    print('post status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == codeHttp


def eliminar_foto(url, headers, codeHttp):
    req = requests.delete(url, headers=headers)
    print('delete status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == codeHttp


def pdfs():
    global rutapdf
    base = get_ruta()
    pdf = ['alberto', 'carlos', 'cristian', 'daniel', 'diana', 'mario', 'octavio', 'romero']
    aleatorio = random.choice(pdf)
    print(aleatorio)
    rutapdf = (base + 'archivos/pdf/' + str(aleatorio) + '.pdf')
    print("la ruta es " + rutapdf)
    return rutapdf


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