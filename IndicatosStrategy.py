# IndicatosStrategy

class IndicatorStrategy(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021, 1, 1)
        self.SetCash(10000)
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol


        self.sma = CustomSimpleMovingAverage("CustomSMA", 30)
        self.RegisterIndicator(self.spy, self.sma, Resolution.Daily)

        #self.sma = self.SMA(self.spy, 30, Resolution.Daily) # 30 perod Simple Moving Average
        #closing_prices = self.History(self.spy, 30, Resolution.Daily)['close']
        # this get the simple moving average for the days before the start data so it would be ready from the begining
        #for time, price in closing_prices.loc[self.spy].items():
         #   self.sma.Update(time, price)


    def OnData(self, data):
        if not self.sma.IsReady:
            return

        # get historical data for 1 year
        hist = self.History(self.spy, timedelta(365), Resolution.Daily)
        low = min(hist["low"]) # get the low of that period
        high = max(hist["high"]) # get the maximun value of that period

        price = self.Securities[self.spy].Price

        # is the spy price is within 5% of the 365 day high and the price is above the simple moving average?
        if price * 1.05 >= high and self.sma.Current.Value < price:
            # if yest check if we have a open position
            if not self.Portfolio[self.spy].IsLong:
                # if you don't have open posittion invest 100% of the portfolio
                self.SetHoldings(self.spy, 1)

        # if the price is 5% of the low and the SMA is above the current price
        elif price * 0.95 <= low and self.sma.Current.Value > price:
            if not self.Portfolio[self.spy].IsShort:
                self.SetHoldings(self.spy, -1)


        else:
            self.Liquidate()

        self.Plot("Benchmark", "52w-High", high)
        self.Plot("Benchmark", "52w-low", low)
        self.Plot("Benchmark", "SMA", self.sma.Current.Value)

        





