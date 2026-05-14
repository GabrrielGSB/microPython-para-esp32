from Utilitarios import * 
import network
import urequests

class WIFI:
    def __init__(self, SSID="Wokwi-GUEST", SENHA=""):
        self.wifi = network.WLAN()
        self.wifi.active(True)

        self.SSID = SSID
        self.SENHA = SENHA
    
    def escanear(self):
        lista_redes = self.wifi.scan()

        print(f"{len(lista_redes)} redes encontradas:\n")
        print("-" * 40)
        print(f"{'SSID (Nome)':<20} | {'RSSI (Sinal)':<10}")
        print("-" * 40)

        for rede in lista_redes:
            ssid = rede[0].decode('utf-8')
            rssi = rede[3]
            
            print(f"{ssid:<20} | {rssi} dBm")
            print("-" * 40)

    def conectar(self):
        if not self.wifi.isconnected():
            self.wifi.connect(self.SSID, self.SENHA)

            tentativas = 0
            while not self.wifi.isconnected() and tentativas < 10:
                print(".", end="") 
                time.sleep(1)
                tentativas += 1

        if self.wifi.isconnected():
            print("\n✅ Conectado com Sucesso!")
            print("Dados da Rede (IP, Máscara, Gateway, DNS):")
            
            print(self.wifi.ifconfig())
            return True
        else:
            print("\n❌ Falha ao conectar. Verifique a senha.")
            return False

    def obterTempoReal(self):
        url = "https://timeapi.io/api/Time/current/zone?timeZone=America/Sao_Paulo"
        try:
            print("Atualizando horário...")
            resposta = urequests.get(url)
            
            if resposta.status_code == 200:
                dados = resposta.json()

                data_hora_completa = dados["dateTime"]

                hora_certa = data_hora_completa[11:19]
                
                print(f"⏰ Hora Oficial: {hora_certa}")
                
            else:
                print(f"Erro no Servidor. Código: {resposta.status_code}")
                
            resposta.close()
        
        except Exception as e:
            print(f"Erro de Conexão: {e}")    