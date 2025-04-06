import base58
import json

def convert_phantom_private_key_to_json(phantom_private_key_base58, output_filename="phantom_private_key.json"):
    """
    Convierte una clave privada de Phantom (en formato Base58) a un archivo JSON
    que contiene una lista de 64 números (bytes) en una sola línea.
    """
    try:
        # Decodificar la clave privada de Base58 a bytes
        private_key_bytes = base58.b58decode(phantom_private_key_base58)

        # Asegurarse de que la clave privada tenga 64 bytes
        if len(private_key_bytes) != 64:
            raise ValueError(f"La clave privada debe tener 64 bytes, pero se encontraron {len(private_key_bytes)}")

        # Convertir los bytes a una lista de enteros
        private_key_list = list(private_key_bytes)

        # Guardar la lista de enteros en un archivo JSON sin indentación
        with open(output_filename, 'w') as f:
            json.dump(private_key_list, f)  # Se omite el parámetro indent

        print(f"Clave privada guardada en {output_filename} en formato JSON (una sola línea).")
        return True

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False

# --- Ejemplo de uso ---
# 1. Reemplaza con tu clave privada de Phantom en formato Base58
phantom_private_key = "4cmeogrSnYkCXkt2jfjjyfKNamCM4jct9N8QAGdR1umMtxErHGVS9MZ4Vda8jphHGxBFFUFUL2MWApG1251WUAEy"

# 2. Convierte la clave privada de Phantom a un archivo JSON (una sola línea)
output_json_filename = "phantom_private_key.json"
convert_phantom_private_key_to_json(phantom_private_key, output_json_filename)