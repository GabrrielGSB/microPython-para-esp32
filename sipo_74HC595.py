from Utilitarios import *

"""
EXPLICAÇÃO:
    -> Classe para controlar 74HC595 SIPO (expansor de GPIOs)
    -> O que pode fazer:
        * registrarSaidas: carrega um byte de dados no registrador interno
        * mostrarSaidas:   leva o byte do registrador interno para o registrador de saída
"""
class ShiftRegister595:
    def __init__(self, pinData, pinLatch, pinClock):
        self.pinData  = Pin(pinData,  OUTPUT)
        self.pinClock = Pin(pinClock, OUTPUT)
        self.pinLatch = Pin(pinLatch, OUTPUT)

        self.index    = 0
        self.seqSaida = []

    def registrarSaidas(self, dados):
        for i in dados: self.seqSaida.append(i)

    def mostrarSaidas(self):
        for i in range(8): self._preencherRegistrador()

    def definirSaidas(self, dados):
        if len(dados) < 8:
            diff = 8 - len(dados)
            for i in range(diff):
                dados.append(0)
                
        self.registrarSaidas(dados)
        self.mostrarSaidas()

    def _atualizarSaida(self):
        self.pinData.value(self.seqSaida[self.index])

    def _pulsoClock(self):
        self.pinClock.off()
        self.pinClock.on(); # delay(10) # checar na esp32 real se funciona sem!

    def _mudarSaidasQ(self):
        self.pinLatch.off(); 
        self.pinLatch.on()

    def _preencherRegistrador(self):
        self._atualizarSaida()
        self._pulsoClock()
        
        self.index += 1
        if (self.index >= 8): 
            self.index = 0; self.seqSaida = []
            self._mudarSaidasQ()
   
"""
Exemplo de Uso:
    # Criar objeto do registrador
    reg  = ShiftRegister595(pinDS, pinSTCP, pinSHCP)

    # Definir os dados que vão ser postos em Q0...Q7
    data = ["8 bits de dados"]
    
    # Registrar esses dados na memória interna do objeto
    reg.registrarSaidas(data)

    # Atualizar o registrador de saída do 595 com os dados
    reg.mostrarSaidas()

    OU---------------------------------------------------

    # Criar objeto do registrador
    reg  = ShiftRegister595(pinDS, pinSTCP, pinSHCP)

    # Definir os dados que vão ser postos em Q0...Q7
    data = ["8 bits de dados"]

    # Registra e atualiza a saída ao mesmo tempo
    reg.definirSaidas(data)
"""
   


