import tkinter as tk
from src.test.crearReportesRecruiter.ReportCrearVacanteIAReclu import crear_vacante_ia_test
from src.test.crearReportesRecruiter.ReportCrearVancanteTestReclu import crear_vacante_manual_test
from src.test.crearReportesRecruiter.reportHappyPathReclu import happypath_test_reclu
from src.test.crearReportesRecruiter.reportRegisterReclu import report_register_recruiter


def registro_reclutador():
    report_register_recruiter()

def happypath_reclutador():
    happypath_test_reclu()

def crear_vacante_manual():
    crear_vacante_manual_test()

def crear_vacante_ia():
    crear_vacante_ia_test()

def cancelar():
    ventana.destroy()  # Cierra la ventana

ventana = tk.Tk()
ventana.title("Mi aplicación")
ventana.geometry("400x300")

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=20)

etiqueta_titulo = tk.Label(marco_botones, text="Interfaz de test cases").grid(column=0, row=0)



boton_registrar = tk.Button(marco_botones, text="Test Registro", command=registro_reclutador).grid(row=1, column=0, padx=10, sticky=tk.E)

boton_happyPath = tk.Button(marco_botones, text="Test Happy Path", command=happypath_reclutador).grid(row=1, column=1, padx=10, sticky=tk.W)

boton_crearVacanteManual = tk.Button(marco_botones, text="Crear vacante manual", command=crear_vacante_manual).grid(row=2, column=0, padx=10)

boton_crearVacanteIA = tk.Button(marco_botones, text="Crear vacante IA", command=crear_vacante_ia_test).grid(row=2, column=1, padx=10, sticky=tk.W)

boton_cancelar = tk.Button(marco_botones, text="Cancelar", command=cancelar).grid(row=3, column=1, padx=20, sticky=tk.E)

ventana.mainloop()
