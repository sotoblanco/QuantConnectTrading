# Updating and canceling order

# This might be used to make a trailing stop
updateFields = UpdateOrderFields()

updateFields.StopPrice = newPrice

self.stopMarketTicket.Update(updateFields)

# How to cancel a order

ticket = self.LimitOrder(symbol, quantity, price)

ticket.Cancel("Cancel Tag")