import alpaca_trade_api as tradeapi

class TradingBot:
    def __init__(self):
        # Read Keys
        self.readKeys()

        # Connecting to the API
        self.alpaca_api = tradeapi.REST(self.API_KEY, self.API_SECRET, self.APCA_API_BASE_URL, api_version='v2')
        self.account = self.alpaca_api.get_account()

    def readKeys(self):
        # Reading API Keys from file
        f = open("api_keys.txt")
        keys = f.read().splitlines()
        f.close()
        self.API_KEY = keys[0]
        self.API_SECRET = keys[1]
        self.APCA_API_BASE_URL = keys[2]

    def submit_order(self, symbol, quantity, side, type, time_in_force, limit_price=None, stop_price=None, client_order_id=None):
        self.alpaca_api.submit_order(symbol, quantity, side, type, time_in_force, limit_price, stop_price, client_order_id)

    def list_orders(self, status=None, limit=None, after=None, until=None, direction=None):
        return self.alpaca_api.list_orders(status=None, limit=None, after=None, until=None, direction=None)

    def list_positions(self):
        return self.alpaca_api.list_positions()
