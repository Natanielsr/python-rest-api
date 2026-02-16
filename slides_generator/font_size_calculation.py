import math

class FontSizeCalculation:
    def __init__(self, largura=13.33, altura=7.5):
        # Área útil com margens de 1 polegada em cada lado
        self.area_util = (largura - 2) * (altura - 2) 

    def calcular_tamanho_fonte(self, texto):
        num_caracteres = len(texto)
        
        if num_caracteres <= 1:
            return 96 # Tamanho máximo seguro para 1 letra
        
        # Fator de preenchimento equilibrado (0.015)
        # Multiplicador reduzido de 22 para 16 (o "meio termo" ideal)
        fator_preenchimento = 0.028
        
        # A fórmula de raiz quadrada suaviza a diferença entre 10 e 100 caracteres
        tamanho_fonte = math.sqrt(self.area_util / (num_caracteres * fator_preenchimento)) * 16

        # Travas de segurança para evitar que textos pequenos estourem a tela
        # E que textos grandes fiquem ilegíveis
        if num_caracteres < 10:
            return min(math.floor(tamanho_fonte), 100) 
        elif num_caracteres > 150:
            return max(math.floor(tamanho_fonte), 24)
        
        return math.floor(tamanho_fonte)