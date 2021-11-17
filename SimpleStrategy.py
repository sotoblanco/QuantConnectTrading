# Simple strategy:

'''
Buy and hold a given stock or ETF
Stop loss: Create a trailing stop loss that is 5% below the stock price
Wait one month before star investing again

'''

class SimpleStrategy(QCAlgortithm):

    # This method store all the variables that we would eventually need to triger our positions
    def Initialize(self): 
        # This are all for backtesting purpose
        self.SetStartDate(2018, 10, 7) 
        self.SetEndDate(2021, 1, 1)
        self.SetCash(10000) # this is our position which would be our account size in live market

        # store the symbol to trade
        self.qqq = self.AddEquity("QQQ", Resolution.Hour).Symbol

        # to track the order ticket

        self.entryTicket = None 
        self.stopMarketTicket = None

        # to track the time where we invest and to wait 30 days before investing agains
        self.entryTime = datetime.min
        self.stopMarketOrderFillTime = datetime.min

        self.highestPrice = 0

    def OnData(self, data):

        # wait 30 days after last exit
        if (self.Time - self.stopMarketOrderFillTime).days < 30: # not trade if the difference between the current time and the time where it hits the stop is lees than zero
            return
        price = self.Securities[self.qqq].Price

        # send entry limit order
        if not self.Portfolio.Invested and not self.Transactions.GetOpenOrders(self.qqq): # check if you have open positions
            quantity = self.CalcuateOrderQuantity(self.qqq, 0.9) # get 90% of your portfolio
            self.entryTicket = self.LimitOrder(self.qqq, quantity, price, "Entry order") # create a limit order at the price of the qqq
            self.entryTime = self.Time # store the time where you enter the position
        # move limit price if not filled after 1 day
        if (self.Time - self.entryTime).days > 1 and self.entryTicket.Status != OrderStatus.Filled:
            self.entryTime = self.Time
            updateFields = UpdateOrderFields()
            updateFields.LimitPrice = price
            self.entryTicket.Update(updateFields)

        # move up trailing stop price
        if self.stopMarketTicket is not None and self.Portfolio.Invested: # check if you have open holdings
            if price > self.highestPrice: # if the price is greater than the highest price of qqq
                self.highestPrice = price # the highest price would become the current price
                updateFields = UpdateOrderFields()
                updateFields.StopPrice = price * 0.95 # create a stop 5% of the current price
                self.stopMarketTicket.Update(updateFields)


    def OnOrderEvent(self, orderEvent): # this is where we set a stop loss in the OnOrderEvent method
        if orderEvent.Status != OrderStatus.Filled: # evaluate if the ticket has been filled
            return

        # send stop loss order if entry limit order is filled
        if self.entryTicket is not None and self.entryTicket.OrderId == orderEvent.OrderId: # if you have open position
            self.stopMarketTicket = self.stopMarketOrder(self.qqq, -self.entryTicket.Quantity, # stop market order for qqq at 5% of the current price
                                                 0.95*self.entryTicket.AverageFillPrice)
        
        # save fill time of stop loss order
        if self.stopMarketTicket is not None and self.stopMarketTicket.OrderId == orderEvent.OrderId: # if you fill the stop loss
            self.stopMarketOrderFillTime = self.Time # store the time when you close the position
            self.highestPrice = 0 # reset the price of the highest price of the qqq











