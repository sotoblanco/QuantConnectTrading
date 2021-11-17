# Stop market orders

# It is a Market order that gets trigger at specify price

self.StopMarketOrder(symbol, quantity, stopPrice)

'''
Symbol: to trade
Quantity: Amount of shares
stopPrice: To trigger a market order

'''

# if the price drops 10% of the market order sell 200 shares of SPY

SPY_close = data[self.spy].Close
self.StopMarketOrder("SPY", -200, SPY_close*0.9)


# Stop limit order

self.StopLimitOrder("SPY", 10, stopPrice, limitPrice)