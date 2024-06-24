from src.modules.recruiter.login_recruiter import login_recruiter, pass_email
from src.objectRepository.recruiter.ajustesReclu.step_clients import step_new_client
from src.pruebas_gui import gui_candidate_prueba


email = "huguito.reclutador.es@yopmail.com"
for i in range(11):
    _, headers, recruiter = login_recruiter(email)
    step_new_client(headers)



#gui_candidate_prueba()



