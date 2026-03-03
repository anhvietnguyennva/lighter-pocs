import logging

import common

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    target = "0x3B4D794a66304F130a4Db8F2551B0070dfCf5ca7"
    value = 0

    account_idx = 717703
    api_key_idx = 0
    pubkey = "0xc0b5503802e5e1ccbf8b493b62fcff3bfa9e21a5d5e8c6296bc0e0ebbb8985753e773f430f2dbf3b"
    data = common.abi_encode_with_signature(
        "changePubKey(uint48,uint8,bytes)", account_idx, api_key_idx, bytes.fromhex(common.remove_0x_prefix(pubkey))
    )

    tx = common.boring_vault_contract.functions.manage(target, data, value).build_transaction(
        {
            "from": common.eth_account.address,
            "nonce": common.w3.eth.get_transaction_count(
                account=common.eth_account.address, block_identifier="pending"
            ),
            "gasPrice": common.w3.eth.gas_price,
        }
    )
    gas_estimate = common.w3.eth.estimate_gas(tx)
    gas_with_buffer = int(gas_estimate * 1.3)
    tx["gas"] = gas_with_buffer
    signed_tx = common.w3.eth.account.sign_transaction(tx, common.eth_account.key)
    tx_hash = common.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_hash_str = common.add_0x_prefix(tx_hash.hex())
    logger.info(f"Transaction sent: {tx_hash_str}")

    # https://mainnet.zklighter.elliot.ai/api/v1/apikeys?account_index=717703&api_key_index=0
