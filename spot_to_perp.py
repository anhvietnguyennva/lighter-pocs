import asyncio
import lighter


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

    # You can find more notes on transfers in the README.md file, under `Transfer Notes`
    transfer_tx, response, err = await client.transfer_same_master_account(
        to_account_index=client.account_index,
        asset_id=client.ASSET_ID_USDC,
        amount=2,  # decimals are added by sdk
        route_from=client.ROUTE_SPOT,
        route_to=client.ROUTE_PERP,
        fee=0,
        memo="0x" + "00" * 32,
    )
    if err is not None:
        raise Exception(f"error transferring {err}")
    print(transfer_tx, response)
    
    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
