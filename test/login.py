from objetos.obj_login import hacerLogin

def login():
    try:
        resultado, headers, token = hacerLogin()
        print(resultado)
        recruiter = resultado['recruiterId']
        print(recruiter)
        print('el token' + str(headers))
        print('paso el login')
        return 'Se hizo login correctamente', headers, recruiter
    except Exception as e:
        print('No se paso el login', str(e))
        return 'No se realizo el login'



