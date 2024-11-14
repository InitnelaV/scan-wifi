import subprocess
import re
import matplotlib.pyplot as plt

def wifi_networks():
    # Exécute la commande netsh sur invite cmd pour scanner les réseaux Wi-Fi (Specifique Windows)
    networks_output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode("cp850")

    # Extraction SSID et Signal
    ssid_regex = r"SSID\s+\d+\s+:\s(.+)"
    signal_regex = r"Signal\s+:\s(\d+)%"

    # Trouve tous les SSID et signaux correspondants
    ssids = re.findall(ssid_regex, networks_output)
    signals = re.findall(signal_regex, networks_output)

    # Dico pour stocker les SSID et signaux
    networks = {}
    for ssid, signal in zip(ssids, signals):
        if ssid not in networks:
            networks[ssid] = int(signal)

    return networks


def plot_networks(networks):
    # Listage des SSID et le pourcentage de captation des signaux
    ssid_names = list(networks.keys())
    signals = list(networks.values())

    # Création du graphique avec matplotlib
    plt.figure(figsize=(12, 8))
    bars = plt.bar(ssid_names, signals, color='skyblue', edgecolor='black')

    # Valeurs signaux sur les barres réseaux
    for bar, signal in zip(bars, signals):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{signal}%", ha='center', va='bottom')

    plt.xlabel("SSID (Nom du réseau)")
    plt.ylabel("Signal (%)")
    plt.title("Réseaux Wi-Fi détectés")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Scanner les réseaux et les afficher sur le graphique
networks = wifi_networks()
plot_networks(networks)
