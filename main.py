import lighter
import asyncio


async def main():
    client = lighter.ApiClient()
    try:
        account_api = lighter.AccountApi(client)
        account = await account_api.account(by="l1_address", value="0xF0319B7cBdEE7DD3684f8f32d6e53A26B4f0FE10")
        print(account.to_json())
    finally:
        await client.close()  # Make sure connection is cleanly closed

if __name__ == "__main__":
    asyncio.run(main())
