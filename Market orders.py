# Market orders 

'''
Takes two arguments:
Symbol 
Quantity

'''

self.MarketOrder(symbol, quantity)


# TSLA EXAMPLE

self.MarketOrder("TSLA", 50) # Take the market price are fill out right away. but wait 5 seconds to move to the next line

# if you don't want to wait you can use
order_ticket = self.MarketOrder("TSLA", True) # moves to the next line without delay that the order get fill out

'''
Buy order are fill out at the Ask price
Sell order are fill out at the Bid price

As default it would wait up to 5 seconds to the order gets fill to move to the next line of code: it can be customize by:

'''

self.Transactions.MarketOrderFillTimeout = timedelta(seconds=30)

