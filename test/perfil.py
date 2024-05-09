from objetos.ajustes.obj_empresa import empresa
from objetos.ajustes.obj_perfil import fotoPerfil, cambioPass, cambioEmail, nombrePerfil
from objetos.obj_clientes import newClient, eliminarCliente
from test.login import login

#respuesta, headers, recruiterID = login()

def cliente(headers):
    try:
        # Test newClient functionality
        newClient(headers)
        print('Nuevo cliente creado con éxito')

        # Test eliminarCliente functionality
        eliminarCliente(headers)
        print('Cliente eliminado con éxito')

        print('\nSe completaron las pruebas de la sección de clientes')
        return 'Se completaron las pruebas de la sección de clientes'
    except Exception as e:
        print(f'Fallaron las pruebas de la sección de clientes: {e}')
        return 'Fallaron las pruebas de la sección de clientes'

def ajustes(headers):
    try:
        # Test nombrePerfil functionality
        nombrePerfil(headers)
        print('Nombre de perfil actualizado con éxito')

        # Test fotoPerfil functionality
        fotoPerfil(headers)
        print('Foto de perfil actualizada con éxito')

        # Test cambioEmail functionality
        cambioEmail(headers)
        print('Correo electrónico actualizado con éxito')

        # Test cambioPass functionality
        cambioPass(headers)
        print('Contraseña actualizada con éxito')

        # Test empresa functionality
        empresa(headers)
        print('Información de la empresa actualizada con éxito')

        print('\nSe completaron las pruebas de la sección de ajustes')
        return 'Se completaron las pruebas de la sección de ajustes'
    except Exception as e:
        print(f'Fallaron las pruebas de la sección de ajustes: {e}')
        return 'Fallaron las pruebas de la sección de ajustes'



