from bip_utils import *

MNEMONIC = "humble ramp fragile script victory utility salmon concert chalk observe shell flock"

seed_bytes = Bip39SeedGenerator(MNEMONIC).Generate("")

bip44_mst_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)

bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)

bip44_chg_ctx = bip44_acc_ctx.Change(Bip44Changes.CHAIN_EXT)

print(bip44_chg_ctx.PublicKey().ToAddress())