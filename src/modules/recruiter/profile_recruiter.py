from src.objectRepository.recruiter.ajustesReclu.step_company import company
from src.objectRepository.recruiter.ajustesReclu.step_profile import name_profile, photo_profile, change_pass, \
    change_email
from src.objectRepository.recruiter.ajustesReclu.step_clients import step_new_client, step_delete_client


def new_client(headers):
    try:

        step_new_client(headers)
        print('Nuevo cliente creado con éxito')

        step_delete_client(headers)
        print('Cliente eliminado con éxito')

        print('\nSe completaron las pruebas de la sección de clientes')
        return 'Se completaron las pruebas de la sección de clientes'
    except Exception as e:
        print(f'Fallaron las pruebas de la sección de clientes: {e}')
        return 'Fallaron las pruebas de la sección de clientes'


def settings(headers):
    try:
        # Test nombrePerfil functionality
        name_profile(headers)
        print('Nombre de perfil actualizado con éxito')

        # Test fotoPerfil functionality
        photo_profile(headers)
        print('Foto de perfil actualizada con éxito')

        # Test cambioEmail functionality
        change_email(headers)
        print('Correo electrónico actualizado con éxito')

        # Test cambioPass functionality
        change_pass(headers)
        print('Contraseña actualizada con éxito')

        # Test empresa functionality
        company(headers)
        print('Información de la empresa actualizada con éxito')

        print('\nSe completaron las pruebas de la sección de ajustes')
        return 'Se completaron las pruebas de la sección de ajustes'
    except Exception as e:
        print(f'Fallaron las pruebas de la sección de ajustes: {e}')
        return 'Fallaron las pruebas de la sección de ajustes'



