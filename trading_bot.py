import alpaca_trade_api as tradeapi

class TradingBot:
    def __init__(self):
        self.readKeys()

        # Connecting to the API
        self.alpaca_api = tradeapi.REST(self.API_KEY, self.API_SECRET, self.APCA_API_BASE_URL, api_version='v2')
        account = self.alpaca_api.get_account()
        print(account.status)
        print(self.alpaca_api.list_orders())

    def readKeys(self):
        # Reading API Keys from file
        f = open("api_keys.txt")
        keys = f.read().splitlines()
        f.close()
        self.API_KEY = keys[0]
        self.API_SECRET = keys[1]
        self.APCA_API_BASE_URL = keys[2]
