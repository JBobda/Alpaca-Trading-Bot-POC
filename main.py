from trading_bot import TradingBot

def main():
    bot = TradingBot()
    bot.submit_order("FB", 1, "buy", "market", "day")
    print(bot.list_orders())
    print(bot.list_positions())

if __name__ == "__main__":
    main()