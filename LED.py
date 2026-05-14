from Utilitarios import *

"""
Classe para controlar qualquer LED conectado ao micro, podendo
ser executada as seguintes ações:
    * ligar o led
    * desligar o led
    * deixar o led em brilho especificado (usa o PWM)
    * deixar o led piscando a uma certa frequência em Hz¹

¹ O led fica piscando sem travar o micro, logo a função deve ser chamada
  de forma contínua dentro do loop para o timer interno ser atualizado.
"""

class LED:
    def __init__(self, pino=None):
        self.pino = pino
        self.LED = Pin(pino, OUTPUT)

        self.PWM = None

        self.timer = 0

        self.aux1 = 0

    def ligar(self):    self.LED.on()
    def desligar(self): self.LED.off()

    def brilho(self, intensidade=50):
        if self.PWM == None:
            self.PWM = PWM(Pin(self.pino), freq=5000, duty=0)

        self.PWM.duty(intensidade)

    def _piscar(self, temp):
        if(millis() - self.timer) > temp:
            self.timer = millis()

            self.LED.value(not self.LED.value())
    def piscar(self, freq_hz=1):
        temp = int((1/freq_hz) * 1000)

        self._piscar(temp)
    


        



        
