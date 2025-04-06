from solders.keypair import Keypair
from mnemonic import Mnemonic

mnemo = Mnemonic("english")
seed = mnemo.to_seed("humble ramp fragile script victory utility salmon concert chalk observe shell flock")

for i in range(10):
    path = f"m/44'/501'/{i}'/0'"
    keypair = Keypair.from_seed_and_derivation_path(seed, path)
    public_key = keypair.pubkey()
    print(f"Wallet {i+1}:")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {keypair}")