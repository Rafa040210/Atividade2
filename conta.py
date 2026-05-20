class Conta():

    def __init__(self, saldo):
        self.saldo = saldo

    def saca(self, valor):
        self.saldo = self.saldo - valor
    
        

    def deposita(self, valorM):
        self.saldo = self.saldo + valorM
        
    
    def calculaRendimento(self):
        return self.saldo*0.1


