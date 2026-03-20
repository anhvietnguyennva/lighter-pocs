import lighter
import asyncio


async def main():
    client = lighter.ApiClient()
    try:
        account_api = lighter.AccountApi(client)
        account = await account_api.account(by="l1_address", value="0xb0e8Ac7f94f0755e75acD32EA3151EF113e4Ffd2")
        print(account.to_json())
    finally:
        await client.close()  # Make sure connection is cleanly closed

if __name__ == "__main__":
    asyncio.run(main())
