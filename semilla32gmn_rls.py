from solders.keypair import Keypair
from mnemonic import Mnemonic

# Frase semilla de 12 palabras (reemplaza con tu frase real)
mnemonic_phrase = "humble ramp fragile script victory utility salmon concert chalk observe shell flock"

# Passphrase opcional (puedes dejarla vacía)
passphrase = input("Introduce la passphrase (déjala vacía si no tiene): ")

# Inicializa el objeto Mnemonic
mnemo = Mnemonic("english")

# Genera la semilla desde la frase mnemónica y la passphrase
seed = mnemo.to_seed(mnemonic_phrase, passphrase=passphrase)

# Genera las claves para las primeras 10 cuentas (índice 0 a 9)
for i in range(10):
    # Define la ruta de derivación BIP44 para Solana
    path = f"m/44'/501'/{i}'/0'"

    # Genera el par de claves desde la semilla y la ruta de derivación
    keypair = Keypair.from_seed_and_derivation_path(seed, path)

    # Obtiene la clave pública
    public_key = keypair.pubkey()

    # Imprime la información de la billetera
    print(f"Wallet {i+1}:")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {keypair}")
    print("-" * 30)