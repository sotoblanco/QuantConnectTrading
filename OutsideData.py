class OutsideData(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2012, 11, 1)
        self.SetEndDate(2021, 11, 19) #Y-M-D
        self.SetCash(10000)

        self.qqq = self.AddEquity("QQQ", Resolution.Minute).Symbol

        self.marketprofile = self.AddData(MP, "MPROFILE", Resolution.Daily).Symbol

        self.Schedule.On(self.DateRules.EveryDay(self.tsla), 
                        self.TimeRules.BeforeMarketClose(self.qqq, 15), 
                        self.ExitPositions)


    def OnData(self, data):
        if self.marketprofile in data:
            score = data[self.musk].Value
            content = data[self.musk].Tweet

            if score > 0.5:
                self.SetHoldings(self.tsla, 1)

            elif score < -0.5:
                self.SetHoldings(self.tsla, -1)

            if abs(score) > 0.5:
                self.Log("Score" + str(score) + ", Tweet: " + content)

    def ExitPositions(self):
        self.Liquidate()
        

class MustTweet(PythonData):

    def GetSource(self, config, date):
        # use your url and use dl=1 to donwload the data
        source = "https://www.dropbox.com/s/ovnsrgg1fou1y0r/MuskTweetsPreProcessed.csv?dl=1"
        return SubscriptionDataSource(source, SubscriptionTransportMedium.RemoteFile)
        

    def Reader(self, config, line, date, isLive):
        if not (line.strip() and line[0].isdigit()):
            return None

        data = line.split(",")
        tweet = MuskTweet()

        try:
            tweet.Symbol = config.Symbol
            tweet.Time = datetime.strptime(data[0], "%Y-%m-%d %H:%M:%S")+timedealt(minutes=1)
            content = data[1].lower()

            if "tsla" in content or "tsla" in content:
                tweet.Value = self.sia.polarity_scores(content)["compound"]

            else:
                tweet.Value = 0

            tweet["Tweet"] = str(content)

        except ValueError:
            return None

        return tweet


