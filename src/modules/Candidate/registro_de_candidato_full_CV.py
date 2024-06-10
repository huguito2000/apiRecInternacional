from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registerMyCV import register_cv


def register_complete_full_cv(enviroment):
    try:
        #Se manda a llamar a la funcion de registro para obtener el correo del candidato
        _, email_candidate = register_onboarding_candidate(enviroment)
        #Se manda a llamar a la funcion de cv para llenar los datos del cv para el usuario
        register_cv(email_candidate)
        email_candidate = str(email_candidate)
        print('Se realiza el registro de un usuario candidato con CV completo :)\n')
        return 'Se realizo el registro completo de un usuario Candidate con CV completo', email_candidate
    except Exception as e:
        print('No se pudo hacer el registro del candidato con el CV comleto :(\n', e)
        return 'No se pudo hacer el registro del candidato con el CV comleto'
