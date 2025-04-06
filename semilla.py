from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import base58
from solders.keypair import Keypair

# Frase semilla de 12 palabras
mnemonic_phrase = "chronic right bachelor tank moral below few inflict sister sad pigeon suspect"

# Passphrase opcional
passphrase = input("Introduce la passphrase (déjala vacía si no tiene): ")

# Generar la semilla desde la frase mnemónica
seed_generator = Bip39SeedGenerator(mnemonic_phrase)
seed_bytes = seed_generator.Generate(passphrase)

# Derivar la clave usando la ruta de Solana: m/44'/501'/0'/0'
bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

# Obtener la clave privada en bytes (Solana usa 32 bytes)
private_key_bytes = bip44_acc_ctx.PrivateKey().Raw().ToBytes()

# ✅ Obtener la clave pública sin comprimir (Solana usa 32 bytes)
public_key_bytes = bip44_acc_ctx.PublicKey().RawUncompressed().ToBytes()[1:]  # Quitamos el primer byte (0x04)

# ✅ Generar el Keypair correctamente en Solana (clave privada + clave pública)
keypair = Keypair.from_bytes(private_key_bytes + public_key_bytes)

# Obtener la clave pública
public_key_solders = keypair.pubkey()
print(f"\n✅ Clave pública (Solana Pubkey): {public_key_solders}")

# Codificar la clave privada en Base58
full_private_key_base58 = base58.b58encode(bytes(keypair)).decode('utf-8')
print(f"🔑 Clave privada en Base58: {full_private_key_base58}")
