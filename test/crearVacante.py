from objetos.crearVacante.obj_vacanteIA import publicarIA
from objetos.crearVacante.obj_vacanteManual1 import paso1
from objetos.crearVacante.obj_vacanteManual2 import paso2
from objetos.crearVacante.obj_vacanteManual3 import paso3
from objetos.crearVacante.obj_vacanteManual4 import paso4, paso5, paso6, paso7
from test.login import login

respuesta, headers, recruiterID = login()
def crearVacanteManual(headers, recruiterId):
    try:
        resultado, vacantId = paso1(headers)
        print('\n')
        paso2(vacantId, headers)
        print('\n')
        paso3(vacantId, headers)
        print('\n')
        paso4(vacantId, headers)
        print('\n')
        paso5(vacantId, headers)
        print('\n')
        paso6(vacantId, headers, recruiterId)
        print('\n')
        paso7(vacantId, headers)
        print('\n Se creo la vacante manual')
        return 'Se creo la vacante manual'
    except Exception as e:
        print('\n No se creo la vacante manual', e)
        return 'No se creo la vacante manual'

def CrearVacanteIA(headers):
    try:
        publicarIA(headers)
        print('Se crea la vacante por IA')
        return 'Se crea la vacante por IA'
    except Exception as e:
        print('No se creo la vacante con IA', e)
        return 'No se creo la vacantre con IA'


crearVacanteManual(headers, recruiterID)