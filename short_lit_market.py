import asyncio

import lighter


async def main():
    client = lighter.SignerClient(
        url="https://mainnet.zklighter.elliot.ai/",
        account_index=717703,
        api_private_keys={0: "0x8102627939eee7424fcc5dd49da865422acac58f77f7eeacaff695e95f3301f875e3443cb122330c"},
    )

    api_client = lighter.ApiClient(configuration=lighter.Configuration(host="https://mainnet.zklighter.elliot.ai/"))
    client.check_client()

    market_index = 120

    tx, tx_hash, err = await client.create_market_order(
        market_index=market_index,
        client_order_index=0,
        base_amount=100,  # 1 LIT
        avg_execution_price=1_1228,
        is_ask=True,
    )
    print(f"Create Order {tx.to_json()} {tx_hash} {err}")
    if err is not None:
        raise Exception(err)

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
