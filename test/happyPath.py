from test.crearVacante import crearVacanteManual, CrearVacanteIA
from test.login import login
from test.perfil import cliente, ajustes
from test.registro import registro

def happypath():
    try:
        registro()
        print('\n')
        respuesta, headers, recruiterID = login()
        print('\n')
        cliente(headers)
        print('\n')
        ajustes(headers)
        print('\n')
        crearVacanteManual(headers, recruiterID)
        print('\n')
        CrearVacanteIA(headers)
        print('\nSe hizo el happy path correctamente')
        return 'Se hizo correctamente el happy path'
    except Exception as e:
        print('No se hizo el happy path', {e})
        return 'No se hizo el happy path'

