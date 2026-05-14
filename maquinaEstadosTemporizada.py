import time
from machine import Timer

class StateMachineTemp:
    def __init__(self, tempEstados=[], funcao=None, escalaTemp='s', info=False):
        self.estados = [False] * len(tempEstados)
        self.estado_atual = 0

        self.timer = Timer(0)

        self.func = funcao
        self.info = info

        multi = 1000 if escalaTemp == 's' else 1
        self.intervalos = [tempo * multi for tempo in tempEstados]

        # Novas variáveis para o controle de Pausa
        self.pausado = False
        self.tempo_inicio_estado = 0
        self.tempo_restante = 0

        self._iniciar()

    def _agendarProximo(self, tempo_ms):
        self.tempo_inicio_estado = time.ticks_ms() 
        self.timer.init(period=tempo_ms, 
                        mode=Timer.ONE_SHOT, 
                        callback=self._callback)

    def _iniciar(self):
        self.pausado = False
        self._atualizarMaquina()
        self._agendarProximo(self.intervalos[self.estado_atual])

    def _atualizarMaquina(self):
        self.estados = [False] * len(self.estados)
        self.estados[self.estado_atual] = True

        if self.info: 
            print(f"Estado atual: {self.estado_atual + 1} | Tempo Alocado: {self.intervalos[self.estado_atual]}ms")

        if self.func is not None:
            self.func(self.estados)

    def _callback(self, t):
        if self.pausado: return 

        self.estado_atual = (self.estado_atual + 1) % len(self.intervalos)
        
        self._atualizarMaquina()
        self._agendarProximo(self.intervalos[self.estado_atual])

    def pausar(self):
        if not self.pausado:

            self.timer.deinit()
            self.pausado = True
            
            tempo_passado = time.ticks_diff(time.ticks_ms(), self.tempo_inicio_estado)
            
            self.tempo_restante = self.intervalos[self.estado_atual] - tempo_passado
            
            if self.tempo_restante < 0: 
                self.tempo_restante = 1 
                
            if self.info:
                print(f"*** MÁQUINA PAUSADA. Faltavam {self.tempo_restante}ms para trocar de estado. ***")

    def resumir(self):
        if self.pausado:
            self.pausado = False
            
            if self.info:
                print(f"*** MÁQUINA RETOMADA. Rodando os {self.tempo_restante}ms restantes. ***")
                
            self._agendarProximo(self.tempo_restante)