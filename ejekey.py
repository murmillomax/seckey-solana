import json
import base58
from nacl.signing import SigningKey
import sys

if len(sys.argv) < 2:
    print("Uso: python seckey.py <ruta_del_archivo.json>")
    sys.exit(1)

json_file_path = sys.argv[1]

try:
    with open(json_file_path, 'r') as f:
        data = json.load(f)
        if isinstance(data, list) and all(isinstance(item, int) for item in data):
            byte_list = data
        else:
            print("El archivo JSON debe contener una lista de números enteros.")
            sys.exit(1)
except FileNotFoundError:
    print(f"Error: El archivo '{json_file_path}' no fue encontrado.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"Error: No se pudo decodificar el archivo JSON '{json_file_path}'.")
    sys.exit(1)

if len(byte_list) != 64:
    print("Error: La lista de bytes en el archivo JSON debe contener exactamente 64 elementos.")
    sys.exit(1)

# Toma solo los primeros 32 bytes para la semilla de la clave privada
private_key_bytes_seed = bytes(byte_list[:32])
private_key_base58_seed = base58.b58encode(private_key_bytes_seed).decode('utf-8')

print(f"Semilla de la clave privada en base-58: {private_key_base58_seed}")

# Genera la clave pública a partir de la semilla
signing_key = SigningKey(private_key_bytes_seed)
public_key_bytes = signing_key.verify_key.encode()
public_key_base58 = base58.b58encode(public_key_bytes).decode('utf-8')

print(f"Clave pública en base-58: {public_key_base58}")

# Concatena la semilla y la clave pública en formato de bytes
full_private_key_bytes = private_key_bytes_seed + public_key_bytes

# Codifica la clave privada completa (64 bytes) en base-58
full_private_key_base58 = base58.b58encode(full_private_key_bytes).decode('utf-8')

print(f"Clave privada completa (64 bytes) en base-58: {full_private_key_base58}")

keypair_data = [private_key_base58_seed, public_key_base58]
with open("private_key_converted.json", "w") as f:
    json.dump(keypair_data, f)

print("\nArchivo 'private_key_converted.json' creado con clave pública (usando la semilla).")

# Adicional: Guarda la clave privada completa en otro archivo por si Phantom la requiere así
with open("full_private_key.txt", "w") as f:
    f.write(full_private_key_base58)

print("\nArchivo 'full_private_key.txt' creado con la clave privada completa en base-58.")