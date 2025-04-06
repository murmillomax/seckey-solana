import json
import base58

byte_list = [180, 229, 198, 186, 22, 248, 170, 203, 32, 150, 188, 87, 189, 118, 229, 43, 210, 70, 74, 166, 72, 249, 199, 43, 139, 182, 9, 126, 14, 97, 109, 117, 59, 244, 218, 2, 199, 204, 132, 168, 51, 125, 1, 133, 124, 56, 122, 68, 57, 200, 254, 156, 7, 80, 130, 83, 0, 220, 85, 169, 255, 114, 115, 246]  # Reemplaza con tu lista completa de números

private_key_bytes = bytes(byte_list)
private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')

print(f"Clave privada en base-58: {private_key_base58}")

# Para crear un archivo en el formato esperado por Solana:
keypair_data = [private_key_base58, ""] # La clave pública se puede obtener a partir de la privada
with open("private_key_converted.json", "w") as f:
    json.dump(keypair_data, f)

print("\nArchivo 'private_key_converted.json' creado.")