from Utilitarios import *

class Potenciometro:
    def __init__(self, pino):
        self.pot = ADC(Pin(pino))
        self.pot.atten(ADC.ATTN_11DB) 
        self.pot.width(ADC.WIDTH_12BIT)

    def leitura(self):
        return self.pot.read()
    
    def leitura_tensao(self):
        return self.leitura() * (3.3/4095)