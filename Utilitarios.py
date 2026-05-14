"""
EXPLICAÇÃO:
    Arquivo de suporte para renomeação de algumas funções e constantes recorrentes, 
    a fim de deixar a programação mais familiar e dinâmica.
"""

from machine import Pin, ADC, PWM, Timer
import time

OUTPUT = Pin.OUT
INPUT  = Pin.IN
FALLING = Pin.IRQ_FALLING
RISING  = Pin.IRQ_RISING

PULL_UP = Pin.PULL_UP

def millis(): return time.ticks_ms()

def delay(temp):  time.sleep_ms(temp)
def delayS(temp): time.sleep(temp)