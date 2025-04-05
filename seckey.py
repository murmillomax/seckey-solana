import json
import base58

byte_list = [208,24,13,240,19,74,163,62,203,75,83,11,31,36,124,132,126,124,29,253,25,192,26,139,206,236,39,188,208,154,241,210,245,161,208,88,163,227,114,215,129,67,87,8,193,61,6,132,10,169,183,82,88,19,189,96,31,162,214,145,89,134,69,133]  # Reemplaza con tu lista completa de números

private_key_bytes = bytes(byte_list)
private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')

print(f"Clave privada en base-58: {private_key_base58}")

# Para crear un archivo en el formato esperado por Solana:
keypair_data = [private_key_base58, ""] # La clave pública se puede obtener a partir de la privada
with open("private_key_converted.json", "w") as f:
    json.dump(keypair_data, f)

print("\nArchivo 'private_key_converted.json' creado.")