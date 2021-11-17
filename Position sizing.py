# Position sizing

self.SetHoldings(symbol, allocation)

self.SetHoldings("SPY", 0.6, True) # should your existing holdings needs to be liquidated before the allocation

self.SetHoldings([PortfolioTarget("SPY", 0.8), PortfolioTarget("IBM", 0.2)])


# calculateOrderQuantita  takes two arguments the symbol and the percentage
# returns an integer with the amount of shares to buy

quantity = self.CalculateOrderQuantity("APPL", 0.3)
# This would buy appl shares at the given percentge in the current price of the market

self.LimitOrder("APPL", quantity, self.Securities["APPL"].Price)

# create a protection to not run out of cash
self.Settings.FreePortfolioValuePercentage = 0.05 # this would kept 5% of your portfolio in cash


# How to liquidate your position

self.Liquidate() ## liquidate all your holdings

self.Liquidate("SPY") # liquidate all your SPY holdings


# Access to orders

self.Transactions.GetOpenOrders(symbol) # all open orders for a specify symbol
self.Transactions.GetOrderById(orderId) # get order by order ID
self.Transactions.cancelOpenOrders(symbol)  # Cancel all open orders by security or the entire portfolio


# Modeling Trade cost

















