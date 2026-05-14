from Utilitarios import *

class Botao:
    def __init__(self, pino=None):
        self.btt = Pin(pino, INPUT, PULL_UP)
        self.timer = 0
    
    def estado(self):
        if (millis() - self.timer) > 200:
            self.timer = millis()

            return self.btt.value()
    
    def estadoBruto(self):
        return self.btt.value()

    def definirInterrupcao(self, callback=None, mode=FALLING):
        self.btt.irq(trigger=mode, handler=callback)