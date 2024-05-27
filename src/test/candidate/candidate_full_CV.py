from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registerMyCV import register_cv


def register_complete_full_cv():
    try:
        #Se manda a llamar a la funcion de registro para obtener el correo del candidato
        _, correo = register_onboarding_candidate()
        #Se manda a llamar a la funcion de cv para llenar los datos del cv para el usuario
        register_cv(correo)
        print('Se realiza el registro completo de un usuario candidato con CV completo')
        return 'Se realizo el registro completo de un usuario Candidate con CV completo'
    except Exception as e:
        print('No se pudo hacer el registro del candidato con el CV comleto', e)
        return 'No se pudo hacer el registro del candidato con el CV comleto'
