# Indicators & Historical data

# History request

self.History(self.Symbol("IBM"), 5, Resolution.Minute) # This request the last 5 bars in minute resolution


# Indicators

self.RSI(Symbol, Period, MovingAverageType, Resolution)

self.rsi = self.RSI("SPY", 10, MovingAverageType.Simple, Resolution.Daily)

# Access the current value of your indicator
self.rsi.Current.Value

# customize your indicator more: for instance custom timeperiod 

indicator = RelativeStrengthIndex(10, MovingAverageType.Simple)

# update
self.RegisterIndicator("SPY", indicator, Resolution.Daily)
indicator.Update(price)

pep = Identity("PEP") # pepsi ticker
coke = Identity("KO") # coke ticker

delta = IndicatorExtensions.Minus(pep, coke) # tracks the differences between pepsi and coke