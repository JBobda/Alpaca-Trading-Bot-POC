import alpaca_trade_api as tradeapi

def main():
    # Reading API Keys from file
    f = open("api_keys.txt")
    keys = f.read().splitlines()
    f.close()

    # Connecting to the API
    api = tradeapi.REST(keys[0], keys[1], api_version='v2')
    print(api.list_orders)

if __name__ == "__main__":
    main()