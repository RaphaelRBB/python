class calculadora:
    area_parede = float 
    area_teto = float 

    def calcular_area_paredes(self, largura, profundidade, altura ):
        self.area_parede =  2 * (largura + profundidade)  *altura