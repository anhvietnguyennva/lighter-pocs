from web3 import Web3

import common


if __name__ == "__main__":
    usdc = Web3.to_checksum_address("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
    usdc_asset_index = 3
    spot_router = 1
    zk_lighter = Web3.to_checksum_address("0x3B4D794a66304F130a4Db8F2551B0070dfCf5ca7")
    value = 0

    # Approve
    # data = common.abi_encode_with_signature(
    #     "approve(address,uint256)", zk_lighter, 1000_000_000
    # )
    # tx = common.boring_vault_contract.functions.manage(usdc, data, value).build_transaction(
    #     {
    #         "from": common.eth_account.address,
    #         "nonce": common.w3.eth.get_transaction_count(
    #             account=common.eth_account.address, block_identifier="pending"
    #         ),
    #         "gasPrice": common.w3.eth.gas_price,
    #     }
    # )
    # gas_estimate = common.w3.eth.estimate_gas(tx)
    # gas_with_buffer = int(gas_estimate * 1.3)
    # tx["gas"] = gas_with_buffer
    # signed_tx = common.w3.eth.account.sign_transaction(tx, common.eth_account.key)
    # tx_hash = common.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    # tx_hash_str = common.add_0x_prefix(tx_hash.hex())
    # print(f"Transaction sent: {tx_hash_str}")

    # Deposit
    data = common.abi_encode_with_signature(
        "deposit(address,uint16,uint8,uint256)", common.BORING_VAULT_ADDRESS, usdc_asset_index, spot_router, 10_000_000
    )
    tx = common.boring_vault_contract.functions.manage(zk_lighter, data, value).build_transaction(
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
    print(f"Transaction sent: {tx_hash_str}")

    # https://mainnet.zklighter.elliot.ai/api/v1/apikeys?account_index=717703&api_key_index=0
