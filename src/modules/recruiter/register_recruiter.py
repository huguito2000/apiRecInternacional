from src.objectRepository.recruiter.register_recruiter import step_register_recruiter, step_verify_email, \
    step_permissions, step_register_complete


def register_recruiter():
    try:
        resultado, headers, correo = step_register_recruiter()
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
        step_verify_email(headers, correo, code)
        print('\n')
        step_permissions(headers)
        print('\n')
        step_register_complete(headers)
        print('\n Se hizo el registro create_report_recruiter correcto')
        return 'Se hizo el registro create_report_recruiter correcto', correo
    except Exception as e:
        print('No se hizo el registro crear Reportes Recruiter', e)
        return 'No se hizo el registro crear Reportes Recruiter'




