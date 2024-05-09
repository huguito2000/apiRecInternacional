# pip3 install requests
import os
import random
import requests

#base = 'https://pre.micros.involverh.com.mx/'
#∫base = 'https://dev.micros.involverh.com.mx/'
base = 'https://stage.micros.involverh.es/'


def sendGet(url, codeHttp: int):
    req = requests.get(url)
    resultado = str(req.status_code)
    print('Get status: ' + resultado)
    assert req.status_code == codeHttp


def sendPost(url, myBody, codeHttp):
    req = requests.post(url, json=myBody)
    print('Post status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp
    resultado = req.json()
    headers = req.headers
    return resultado, headers


def sendPatch(url, headers, myBody, codeHttp):
    req = requests.patch(url, headers=headers, json=myBody)
    print('Patch status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp


def sendPut(url, headers, codeHttp):
    try:
        req = requests.put(url, headers=headers)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == codeHttp
    except Exception as e:
        print(e)


def sendPutBody(url, headers, myBody, codeHttp):
    try:
        req = requests.put(url, headers=headers, json=myBody)
        print(req.content)
        print('PUT status: ' + str(req.status_code))
        assert req.status_code == codeHttp
    except Exception as e:
        print(e)


def sendPostSinBody(url, codeHttp):
    req = requests.post(url)
    print('Post Sin body status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp


def sendPostHeadersSinBody(url, headers, codeHttp):
    req = requests.post(url, headers=headers)
    print('Post Sin body status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp


def sendPostHeaders(url, headers, myBody, codeHttp):
    req = requests.post(url, headers=headers, json=myBody)
    print('Post status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp
    resultado = req.json()
    return resultado


def sendDelete(url, headers, myBody, codeHttp):
    req = requests.delete(url, headers=headers, json=myBody)
    print('Patch status: ' + str(req.status_code))
    print(req.json())
    assert req.status_code == codeHttp
    resultado = req.json()
    return resultado


def nombres():
    Nombres = ['Hugo', 'Dennis', 'Miguel', 'Gabriel', 'Javi', 'Lucio', 'Jesus', 'Victor', 'Abraham', 'Juan', 'Rafael',
               'Ramiro', 'Pedro', 'Julian', 'Valentin']
    aleatorio = random.choice(Nombres)
    print(aleatorio)
    return aleatorio


def apellidos():
    apellido = ['Álvarez', 'Castillo', 'De León', 'Díaz', 'Espinoza', 'Fernández', 'García', 'Salazar', 'Santana',
                'Zambrano', 'Perez', 'Rodriguez', 'Martinez', 'Garcia', 'Torres', 'Olivera', 'Lopez', 'Sanchez',
                'Ascarragan', 'Hernandez']
    aleatorio = random.choice(apellido)
    print(aleatorio)
    return aleatorio


ruta = ''


def getRuta():
    imgRuta = os.getcwd().split('/')
    print(len(imgRuta))
    baseImg = ''
    for i in range(len(imgRuta)):
        print(imgRuta[i - 1])
        baseImg = baseImg + str(imgRuta[i]) + '/'
    return baseImg


def foto():
    global ruta
    baseImg = getRuta()
    imagen = random.randint(0, 10)
    print(imagen)
    ruta = (baseImg + 'archivos/img/' + str(imagen) + '.jpeg')
    print(ruta)
    return ruta


def subirArchivo(rutaArchivo, url, headers, codeHttp):
    files = {'file': open(rutaArchivo, 'rb')}
    req = requests.post(url, headers=headers, files=files)
    print('post status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == codeHttp


def eliminarFoto(url, headers, codeHttp):
    req = requests.delete(url, headers=headers)
    print('delete status: ' + str(req.status_code))
    print(req.text)
    assert req.status_code == codeHttp

