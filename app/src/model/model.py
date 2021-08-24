class Model():
    def __init__(self):

        # Variáveis 
        self.vitX = 0
        self.vitO = 0
        self.sentinela = 0
        self.vencedor = 0
        self.ganhador = ' ' 
        self.bp1 = 0
        self.bp2 = 0
        self.bp3 = 0
        self.bp4 = 0
        self.bp5 = 0
        self.bp6 = 0
        self.bp7 = 0
        self.bp8 = 0
        self.bp9 = 0

    
    # Funções para atualizar o valor da variável de acordo com o botão e evento (at = atualiza)

    def atbtn1(self, bp1):
        self.bp1 = bp1

    def atbtn2(self, bp2):
        self.bp2 = bp2

    def atbtn3(self, bp3):
        self.bp3 = bp3

    def atbtn4(self, bp4):
        self.bp4 = bp4

    def atbtn5(self, bp5):
        self.bp5 = bp5

    def atbtn6(self, bp6):
        self.bp6 = bp6

    def atbtn7(self, bp7):
        self.bp7 = bp7

    def atbtn8(self, bp8):
        self.bp8 = bp8

    def atbtn9(self, bp9):
        self.bp9 = bp9


    def atsentinela(self, sentinela):
        self.sentinela = sentinela


    def atvencedor(self, vencedor):
        self.vencedor = vencedor


    def atganhador(self, ganhador):
        self.ganhador = ganhador


    # Função para verificar se há um vencedor + função para guardar vencedor
    # Jogador X - 1  Jogador O - 2   Empate - 3  Nenhum - 0
    def gameover(self):
        self.sentinela += 1
        # 1 2 3
        if self.bp1 == self.bp2 and self.bp1 == self.bp3 and self.bp1 != 0:
            self.vencedor = self.bp1
            self.winner()
            
        # 4 5 6
        elif self.bp4 == self.bp5 and self.bp4 == self.bp6 and self.bp4 != 0:
            self.vencedor = self.bp4
            self.winner()

        # 7 8 9
        elif self.bp7 == self.bp8 and self.bp7 == self.bp9 and self.bp7 != 0:
            self.vencedor = self.bp7
            self.winner()

        # 1 4 7
        elif self.bp1 == self.bp4 and self.bp1 == self.bp7 and self.bp1 != 0:
            self.vencedor = self.bp1
            self.winner()
           
        # 2 5 8
        elif self.bp2 == self.bp5 and self.bp2 == self.bp8 and self.bp2 != 0:
            self.vencedor = self.bp2
            self.winner()
            
        # 3 6 9
        elif self.bp3 == self.bp6 and self.bp3 == self.bp9 and self.bp3 != 0:
            self.vencedor = self.bp3
            self.winner()
            
        # 1 5 9
        elif self.bp1 == self.bp5 and self.bp1 == self.bp9 and self.bp1 != 0:
            self.vencedor = self.bp1
            self.winner()
            
        # 3 5 7
        elif self.bp3 == self.bp5 and self.bp3 == self.bp7 and self.bp3 != 0:
            self.vencedor = self.bp3
            self.winner()
            
        # Empate
        else:
            if self.sentinela == 9:
                self.vencedor = 3
                self.winner()
        
       
    # Função guarda vencedor da partida
    # Jogador X - 1  Jogador O - 2   Empate - 3  Nenhum - 0
    def winner(self):
        if self.vencedor == 1:
            self.vitX +=1
            self.ganhador = 'Vencedor: Jogador X'

        elif self.vencedor == 2:
            self.vitO +=1
            self.ganhador = 'Vencedor: Jogador O'

        elif self.vencedor == 3:
            self.ganhador = 'Empate entre os jogadores!'
        
        else:
            self.ganhador = ' '


    # Função retorna vencedor da partida
    def returnWinner(self):
        return self.ganhador


    # Funções para retornar o número de vitórias de cada jogador

    # Jogador X
    def returnVX(self):
        return self.vitX

    # Jogador O 
    def returnVO(self):
        return self.vitO