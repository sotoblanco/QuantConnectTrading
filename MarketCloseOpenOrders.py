# Market On Open-Close Orders

self.MarketOnOpenOrder(symbol, quantity)

self.MarketOnCloseOrder(symbol, quantity)



# Time in force

# Good until canceled
TimeInForce.GoodTilCanceled

TimeInForce.Day

TimeInForce.GoodTilDate()

self.DefaultOrderProperties.TimeInForce = TimeInForce.Day
