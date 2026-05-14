'''
Display 
-> Dimensões:   128x64
-> Comunicação: I2C
-> Controlador: ssd1306
'''
from Utilitarios import *
from machine import SoftI2C
import dht
import ssd1306 


# i2c = SoftI2C(scl=Pin(21), sda=Pin(14))

# largura = 128
# altura = 64
# oled = ssd1306.SSD1306_I2C(largura, altura, i2c)

class Display_ssd1306:
    def __init__(self, pinoSCL=None, pinoSDA=None):
        i2c  = SoftI2C(scl=Pin(pinoSCL), sda=Pin(pinoSDA))
        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)

    def limparTela(self):
        self.oled.clear()

    def atualizar(self):
        self.oled.show()
    
    def escrever(self, texto, x, y):
        self.oled.text(texto, x, y)


