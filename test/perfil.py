from objetos.ajustes.obj_empresa import empresa
from objetos.ajustes.obj_perfil import nombrePerfil, fotoPerfil, cambioPass, cambioEmail
from objetos.obj_clientes import newClient, eliminarCliente
from test.login import login

#respuesta, headers, recruiterID = login()

def cliente(headers):
    try:
        newClient(headers)
        print('\n')
        eliminarCliente(headers)
        print('Se hizo la prueba correctamente de la sección de clientes')
        return 'Se hizo la prueba correctamente de la sección de clientes'
    except Exception as e:
        print('No pasaron las pruebas de la sección de clientes', e)
        return 'No pasaron las pruebas de la sección de clientes'

def ajustes(headers):
    try:
        nombrePerfil(headers)
        print('\n')
        fotoPerfil(headers)
        print('\n')
        cambioEmail(headers)
        print('\n')
        cambioPass(headers)
        print('\n')
        empresa(headers)
        print('\n Se hicieron las pruebas de la sección de perfil')
        return 'Se hicieron las pruebas de la sección de perfil'
    except Exception as e:
        print('No se hizo la pruena de la seccion de perfil', e)
        return 'No se hizo la pruena de la seccion de perfil'