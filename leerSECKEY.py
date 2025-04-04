import json

file_path = "private_key_converted.json"

try:
    with open(file_path, 'r') as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print(f"El archivo {file_path} no fue encontrado.")
except json.JSONDecodeError:
    print(f"Error al decodificar el archivo JSON en {file_path}.")