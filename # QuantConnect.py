# QuantConnect

class DancingLightBrownFish(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 1, 1)  # Set Start Date
        self.SetEndDate(2021, 1, 1)
        self.SetCash(100000)  # Set Strategy Cash
        
        
        spy =  self.AddEquity("SPY", Resolution.Daily)
        
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        
        self.spy = spy.Symbol
        
        self.SetBenchmark("SPY")
        
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        
        self.entryPrice = 0
        self.period = timedelta(31)
        self.nextEntryTime = self.Time
        


    def OnData(self, data):
        # check if the data exits
        if not self.spy in data:
            return
        
       # price = data.Bars[self.spy].Close
        price = data[self.spy].Close
        # price = 
        
        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy, 1)
                #self.MarketOrder(self.spy, int(self.Portfolio.Cash / price))
                self.Log("BUY SPY @" + str(price))
                self.entryPrice = price
                
        elif self.entryPrice * 1.1 < price or self.entryPrice * 0.9 > price:
            self.Liquidate()
            self.Log("SELL SPY @" + str(price))
            self.nextEntryTime = self.Time + self.period
        
        
        
        '''OnData event is the primary entry point for your algorithm. Each new data point will be pumped in here.
            Arguments:
                data: Slice object keyed by symbol containing the stock data
        '''

        # if not self.Portfolio.Invested:
        #    self.SetHoldings("SPY", 1)
