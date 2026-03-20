import asyncio

import lighter
from decimal import Decimal

LLP_POOL_INDEX = 281474976710654


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

    account_api = lighter.AccountApi(api_client)
    pool_resp = await account_api.account(by="index", value=str(LLP_POOL_INDEX))
    pool_account = pool_resp.accounts[0]

    share_price = Decimal(pool_account.total_asset_value) / Decimal(pool_account.pool_info.total_shares)
    print(f"poolAccountId: {LLP_POOL_INDEX} sharePrice: {share_price}")

    deposit_amount = Decimal(5)
    share_amount = int(deposit_amount / share_price)

    tx_info, response, err = await client.mint_shares(
        public_pool_index=LLP_POOL_INDEX,
        share_amount=share_amount, 
    )

    print(f"Mint Shares {tx_info=} {response=} {err=}")
    if err is not None:
        raise Exception(err)

    await client.close()
    await api_client.close()


if __name__ == "__main__":
    asyncio.run(main())
