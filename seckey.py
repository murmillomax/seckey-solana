import json
import base58

byte_list = [142,63,207,56,205,154,32,197,238,189,212,228,27,56,19,0,235,78,108,139,60,84,143,108,44,138,19,146,237,203,48,240,220,236,212,189,212,29,27,54,39,123,94,102,171,54,0,180,202,163,168,239,22,151,54,170,207,41,164,238,64,66,251,218]  # Reemplaza con tu lista completa de números

private_key_bytes = bytes(byte_list)
private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')

print(f"Clave privada en base-58: {private_key_base58}")

# Para crear un archivo en el formato esperado por Solana:
keypair_data = [private_key_base58, ""] # La clave pública se puede obtener a partir de la privada
with open("private_key_converted.json", "w") as f:
    json.dump(keypair_data, f)

print("\nArchivo 'private_key_converted.json' creado.")