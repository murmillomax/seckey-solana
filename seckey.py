import json
import base58

byte_list = [126,138,45,152,83,221,120,18,177,91,50,116,235,46,50,95,36,236,75,32,223,51,139,104,159,12,200,43,83,97,43,230,117,96,79,15,248,10,245,1,242,54,55,137,72,229,226,152,103,120,237,217,244,78,167,231,96,230,214,226,179,245,35,7]  # Reemplaza con tu lista completa de números

private_key_bytes = bytes(byte_list)
private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')

print(f"Clave privada en base-58: {private_key_base58}")

# Para crear un archivo en el formato esperado por Solana:
keypair_data = [private_key_base58, ""] # La clave pública se puede obtener a partir de la privada
with open("private_key_converted.json", "w") as f:
    json.dump(keypair_data, f)

print("\nArchivo 'private_key_converted.json' creado.")