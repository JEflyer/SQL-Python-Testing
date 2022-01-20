class Contract:
        def __init__(self, address,standard,chain):
            self.address = address
            self.standard = standard
            self.chain = chain

class Transaction:
        def __init__(self,contractAddress,tokenAmount,usdValue,transactionType):
            self.address = contractAddress
            self.tokenAmount = tokenAmount
            self.usdValue =usdValue
            self.transactionType = transactionType