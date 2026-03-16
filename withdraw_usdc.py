import asyncio

import lighter

AMOUNT = 1.0


async def main():
    client = lighter.SignerClient(
        url="https://mainnet.zklighter.elliot.ai/",
        account_index=717703,
        api_private_keys={0: "0x8102627939eee7424fcc5dd49da865422acac58f77f7eeacaff695e95f3301f875e3443cb122330c"},
    )

    api_client = lighter.ApiClient(configuration=lighter.Configuration(host="https://mainnet.zklighter.elliot.ai/"))
    err = client.check_client()
    if err is not None:
        print(f"CheckClient error: {err}")
        return

    # Note: There is no limit or fee for normal withdrawal
    withdraw_tx, response, err = await client.withdraw(
        asset_id=client.ASSET_ID_USDC,  # change this to `client.ASSET_ID_ETH` to withdraw ETH. Also, change route_type to spot
        route_type=client.ROUTE_PERP,  # change this to `client.ROUTE_SPOT` to withdraw from spot balance
        amount=AMOUNT,
    )
    if err is not None:
        raise Exception(f"error withdrawing {err}")

    print(withdraw_tx, response)

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
