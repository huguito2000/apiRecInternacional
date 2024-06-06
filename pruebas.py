import json
import tkinter as tk
from tkinter import ttk
#from objetosReclu.funciones import getRuta

from dotenv import dotenv_values
from src.services.catalogs import env

"""
def ambientes(parameter):
    ruta = getRuta()
    with open(ruta + 'objetosReclu/config.json') as archivo_configuracion:
        configuracion = json.load(archivo_configuracion)

    # Check if parameter is not empty before using it as a key
    if parameter:
        entorno_actual = parameter
        base = configuracion.get(entorno_actual)  # Use get() to avoid KeyError
        return base
    else:
        print("Error: No environment provided")
        return None  # Or handle the missing parameter differently
def my_function(parameter, callback):
    # Perform operations using the received parameter
    print(f"Received parameter: {parameter}")
    base = ambientes(parameter)
    if base:
        # Replace 'function_logic' with your actual function logic using 'base'
        callback(base)  # Call the callback function with the result
    else:
        print("Error: Invalid environment selected")
        callback(None)  # Pass None in case of error


def handle_environment(base):
    if base:
        # Perform actions using the retrieved base data from ambientes
        print(f"Using environment: {base}")
        # You can call ambientes(base) again for further processing here
        return base
    else:
        print("Error: No valid environment retrieved")

main_window = tk.Tk()
main_window.geometry("400x300")

main_window.title("Combobox")
instruction_label = tk.Label(main_window, text="Selecione ambiente:")
instruction_label.pack(pady=10)
environment_value = tk.StringVar()
combo = ttk.Combobox(
    state="readonly",
    values=["qa", "stage", "prod"]
)

combo.place(x=80, y=50)

def execute_function():
    selected_environment = combo.get()
    my_function(selected_environment, handle_environment)  # Pass handle_environment as callback



execute_button = tk.Button(main_window, text="Execute Function", command=execute_function)
execute_button.pack(pady=80)


"""
env = dotenv_values("etc/.env")
url_server = env.get("URL_SERVER")

if url_server:
    print(url_server)
else:
    print("La variable 'URL_SERVER' no está definida en el archivo .env")
