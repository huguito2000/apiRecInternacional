from objetos.registro1.obj_registro import registro1
from objetos.registro1.obj_registro2 import registro2
from objetos.registro1.obj_registro3 import registro3
from objetos.registro1.obj_registro4 import registro4

def registro():
    try:
        resultado, headers, correo = registro1()
        code = str(resultado['user']['checkCode'])
        print('el codigo es: ' + code)
        print('los headers son: ' + str(headers))
        token = headers['token']
        token = str(token.replace('Bearer ', ''))
        print('el token es: ' + token)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        print('\n')
        registro2(headers, correo, code)
        print('\n')
        registro3(headers)
        print('\n')
        registro4(headers)
        print('\n Se hizo el registro correcto')
        return 'Se hizo el registro correcto'
    except Exception as e:
        print('No se hizo el registro', {e})
        return 'No se hizo el registro'



