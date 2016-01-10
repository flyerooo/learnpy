class Stock:
    def __init__(self, symbol, name, perviousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.__perviousClosingPrice = perviousClosingPrice
        self.__currentPrice = currentPrice
    def getName(self):
        return self.name
    def getSymbol(self):
        return self.symbol

