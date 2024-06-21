import tkinter as tk

from dotenv import dotenv_values

from src.modules.Candidate.busquedaVacantes import search_vacancy
from src.modules.Candidate.loginCand import login_cand, pass_email
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.modules.Candidate.registro_de_candidato_full_CV import register_complete_full_cv
from src.objectRepository.candidate.obj_loginCand import email_candidate
from src.services.catalogs import env


def registro_candidato_onboarding():
    register_onboarding_candidate()


def registro_completo():
    register_complete_full_cv()


def busqueda_vacantes():
    search_vacancy()


def login_candidato():
    login_cand(email_candidate, pass_email)


def cancelar():
    ventana.destroy()  # Cierra la ventana


ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("400x300")

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=20)

tk.Label(marco_botones, text="Interfaz de test cases").grid(column=0, row=0)

tk.Button(marco_botones, text="Test Registro", command=login_candidato).grid(row=1, column=0, padx=10,
                                                                             sticky=tk.E)

tk.Button(marco_botones, text="Test Happy Path", command=registro_candidato_onboarding).grid(row=1,
                                                                                             column=1,
                                                                                             padx=10,
                                                                                             sticky=tk.W)

tk.Button(marco_botones, text="Crear vacante manual", command=registro_completo).grid(row=2,
                                                                                      column=0,
                                                                                      padx=10)

tk.Button(marco_botones, text="Crear vacante IA", command=busqueda_vacantes).grid(row=2,
                                                                                  column=1,
                                                                                  padx=10,
                                                                                  sticky=tk.W)

tk.Button(marco_botones, text="Cancelar", command=cancelar).grid(row=3, column=1, padx=20, sticky=tk.E)

ventana.mainloop()
