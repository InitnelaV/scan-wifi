import subprocess
import re
import matplotlib.pyplot as plt


def get_wifi_networks():
    # Exécute la commande netsh pour scanner les réseaux Wi-Fi
    networks_output = subprocess.check_output("netsh wlan show networks mode=bssid", shell=True).decode("utf-8")

    # Expressions régulières pour extraire SSID et Signal
    ssid_regex = r"SSID\s+\d+\s+:\s(.+)"
    signal_regex = r"Signal\s+:\s(\d+)%"

    ssids = re.findall(ssid_regex, networks_output)
    signals = re.findall(signal_regex, networks_output)

    # Convertir les signaux en nombres entiers et limiter les doublons
    networks = {}
    for ssid, signal in zip(ssids, signals):
        if ssid not in networks:  # Pour éviter les doublons de SSID
            networks[ssid] = int(signal)

    return networks


def plot_networks(networks):
    # Extraire les SSID et la puissance des signaux
    ssid_names = list(networks.keys())
    signals = list(networks.values())

    # Créer un graphique en barres
    plt.figure(figsize=(10, 6))
    plt.bar(ssid_names, signals, color='skyblue')
    plt.xlabel("SSID (Nom du réseau)")
    plt.ylabel("Signal (%)")
    plt.title("Réseaux Wi-Fi détectés")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Scanner les réseaux et les afficher
networks = get_wifi_networks()
plot_networks(networks)
