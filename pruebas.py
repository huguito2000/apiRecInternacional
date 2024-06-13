from dotenv import dotenv_values

from src.modules.Candidate.loginCand import email_candidate
from src.modules.Candidate.postulacion import postulacion_candidato

postulacion_candidato(email_candidate)