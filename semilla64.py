from mnemonic import Mnemonic
import hashlib
from solders.keypair import Keypair
import base58
from solders.pubkey import Pubkey
import sys

# Reemplaza con tu frase semilla de 12 palabras
mnemonic_phrase = "gravity torch beef armed glue motion arrive hurdle region antenna fit winner employ kid arrow skill rich reveal goat learn attract mansion scrap syrup"

# Inicializa el generador de mnemónicos para inglés
mnemonic_generator = Mnemonic('english')

try:
    # Imprimir el sys.path
    print(sys.path)
    print("Solana importado exitosamente")

    # 1. Generar la semilla (con opción de passphrase)
    passphrase = input("Introduce la passphrase (déjala vacía si no tiene): ")
    seed_bytes = mnemonic_generator.to_seed(mnemonic_phrase, passphrase=passphrase)

    # **Importante:** solders.Keypair.from_seed() espera 32 bytes
    # La semilla generada por mnemonic.to_seed() es de 64 bytes.
    # Para Solana, generalmente se usan los primeros 32 bytes.
    seed_32_bytes = seed_bytes[:32]

    # 2. Generar el Keypair de Solana directamente desde los bytes de la semilla
    keypair = Keypair.from_seed(seed_32_bytes)

    # Obtener la clave pública (de solders)
    public_key_solders = keypair.pubkey()
    print(f"Clave pública (Pubkey): {public_key_solders}")
    print(f"Clave pública en base-58 (solders): {public_key_solders}")

    # **Obtener la clave privada completa (64 bytes) directamente del objeto Keypair**
    full_private_key_bytes = bytes(keypair)

    # Codificar la clave privada completa a Base58
    full_private_key_base58 = base58.b58encode(full_private_key_bytes).decode('utf-8')
    print(f"Clave privada completa (64 bytes) en base-58 (solders): {full_private_key_base58}")

except Exception as e:
    print(f"Error al generar el Keypair de Solana: {e}")
    print("Asegúrate de que la frase semilla y la passphrase sean correctas.")