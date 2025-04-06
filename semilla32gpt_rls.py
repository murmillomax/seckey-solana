from solders.keypair import Keypair
from mnemonic import Mnemonic

# Frase mnemónica utilizada para generar la semilla
mnemonic_phrase = "humble ramp fragile script victory utility salmon concert chalk observe shell flock"

# Solicitar la passphrase (puede dejarse vacía)
passphrase = input("Introduce la passphrase (déjala vacía si no tiene): ")

# Crear objeto Mnemonic y derivar la semilla con la passphrase
mnemo = Mnemonic("english")
seed = mnemo.to_seed(mnemonic_phrase, passphrase=passphrase)

# Generar 10 wallets con distintas rutas de derivación
wallets = []
for index in range(10):
    derivation_path = f"m/44'/501'/{index}'/0'"
    keypair = Keypair.from_seed_and_derivation_path(seed, derivation_path)
    wallets.append({
        "index": index,
        "public_key": keypair.pubkey(),
        "private_key": keypair
    })

# Imprimir resultados
for wallet in wallets:
    print(f"Wallet {wallet['index'] + 1}:")
    print(f"Public Key: {wallet['public_key']}")
    print(f"Private Key: {wallet['private_key']}")
    print("-" * 30)


