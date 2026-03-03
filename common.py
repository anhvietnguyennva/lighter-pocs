from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from abis import boring_vault_abi
import time
import os

from eth_abi import encode
from web3 import Web3


def now_seconds() -> int:
    return int(time.time())


def now_ms() -> int:
    return int(time.time() * 1000)


def add_0x_prefix(s):
    if s.startswith("0x"):
        return s
    return "0x" + s


def remove_0x_prefix(s):
    if s.startswith("0x"):
        return s[2:]
    return s


def abi_encode_with_signature(signature, *args):
    # Get the function selector (first 4 bytes of the keccak-256 hash of the signature)
    function_selector = Web3().solidity_keccak(["string"], [signature])[:4]

    if len(args) == 0:
        return add_0x_prefix(function_selector.hex())

    # Extract the types from the signature
    types = signature[signature.index("(") + 1 : signature.index(")")].split(",")

    # Encode the arguments
    encoded_args = encode(types, args)

    # Concatenate the function selector and the encoded arguments
    return add_0x_prefix((function_selector + encoded_args).hex())


PRIVATE_KEY = os.getenv("PRIVATE_KEY")
if not PRIVATE_KEY:
    raise ValueError("PRIVATE_KEY environment variable is required but not set")

RPC_URL = "https://eth.drpc.org"
BORING_VAULT_ADDRESS = "0xb0e8Ac7f94f0755e75acD32EA3151EF113e4Ffd2"


provider = Web3.HTTPProvider(RPC_URL)
w3 = Web3(provider)
if not w3.is_connected():
    raise ConnectionError("Failed to connect to the Ethereum network")

eth_account = Account().from_key(PRIVATE_KEY)

boring_vault_contract = w3.eth.contract(address=BORING_VAULT_ADDRESS, abi=boring_vault_abi)
