import asyncio

import lighter

STAKING_POOL_INDEX = 281474976624800


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
    

    tx_info, response, err = await client.stake_assets(
        staking_pool_index=STAKING_POOL_INDEX,
        share_amount=1000000,  # 1 LIT
    )

    print(f"Mint Shares {tx_info=} {response=} {err=}")
    if err is not None:
        raise Exception(err)

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main())
