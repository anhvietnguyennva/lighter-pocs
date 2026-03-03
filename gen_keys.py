import lighter

if __name__ == "__main__":
    private_key, public_key, err = lighter.create_api_key()
    print(
        f"private key: {private_key}"
    )  # 0x8102627939eee7424fcc5dd49da865422acac58f77f7eeacaff695e95f3301f875e3443cb122330c
    print(
        f"public key: {public_key}"
    )  # 0xc0b5503802e5e1ccbf8b493b62fcff3bfa9e21a5d5e8c6296bc0e0ebbb8985753e773f430f2dbf3b
