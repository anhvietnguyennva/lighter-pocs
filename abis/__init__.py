import json

with open("abis/boring_vault.json", "r", encoding="utf-8") as file:
    boring_vault_abi = json.load(file)