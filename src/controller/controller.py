class Controller():
    def __init__(self, view, model):

        self.view = view
        self.model = model

    def b1(self, bp1):
        self.model.atbtn1(bp1)

    def b2(self, bp2):
        self.model.atbtn2(bp2)

    def b3(self, bp3):
        self.model.atbtn3(bp3)

    def b4(self, bp4):
        self.model.atbtn4(bp4)

    def b5(self, bp5):
        self.model.atbtn5(bp5)

    def b6(self, bp6):
        self.model.atbtn6(bp6)

    def b7(self, bp7):
        self.model.atbtn7(bp7)

    def b8(self, bp8):
        self.model.atbtn8(bp8)

    def b9(self, bp9):
        self.model.atbtn9(bp9)


    def asentinela(self, sentinela):
        self.model.atsentinela(sentinela)


    def avencedor(self, vencedor):
        self.model.atvencedor(vencedor)


    def aganhador(self, ganhador):
        self.model.atganhador(ganhador)


    def fimdejogo(self):
        self.model.gameover()
        self.view.mostraVencedor()


    def vencedor(self):
        self.model.winner()


    def retornaVencedor(self):
        v = self.model.returnWinner()
        return v

    
    def retornaVX(self):
        vx = self.model.returnVX()
        return vx
        

    def retornaVO(self):
        vo = self.model.returnVO()
        return vo

