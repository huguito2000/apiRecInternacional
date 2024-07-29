from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registerMyCV import register_cv


def register_complete_full_cv():
    try:
        """Se manda a llamar a la función de registro para obtener el correo del candidato"""
        _, email_candidate, t1, fr1 = register_onboarding_candidate()

        """Se manda a llamar a la función de CV para llenar los datos del CV para el usuario"""
        _, t2, fr2 = register_cv(email_candidate)

        casos = t1['exito'] + t1['fallo'] + t2['exito'] + t2['fallo']

        exito = (t1['exito'] + t2['exito'])
        print('\nLos casos de éxito son:', exito)

        fallo = casos - exito
        print('\nLos casos fallidos son:', fallo)

        print('El total de los casos son:', casos)

        total = {"exito": exito, "fallo": fallo}

        function_results = fr1 + fr2

        if exito == casos:
            status_message = 'Se realiza el registro de un usuario candidato con CV completo :)\n'
        else:
            status_message = 'No se pudo hacer el registro del candidato con el CV completo :(\n'

        print(status_message)

        return status_message, email_candidate, total, function_results

    except Exception as e:
        print('No se pudo hacer el registro del candidato con el CV completo :(\n', e)
        return 'No se pudo hacer el registro del candidato con el CV completo', None
