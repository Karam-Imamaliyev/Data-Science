import pandas as pd
import matplotlib.pyplot as plt


# ------------------------------
# 🔷 STRATEGIE-MUSTER
# ------------------------------

def lade_und_berechne_daten(pfad: str) -> pd.DataFrame:
    """CSV-Datei laden und die Berechnungen durchführen."""
    df = pd.read_csv(pfad)

    # CO2-Emissionen, Temperatur und Extreme Wetterereignisse in einem Pivot
    pivot_data = df.pivot_table(
        index='Year',
        values=['CO2_Emissions_tons_per_capita', 'Avg_Temperature_degC', 'Extreme_Weather_Events'],
        aggfunc='mean'
    )
    return pivot_data


# 2. Grafik erstellen
def erstelle_finale_grafik(pivot_data: pd.DataFrame) -> None:
    """Erstellt und zeigt das Diagramm."""
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Linke Achse: CO2 und Temperatur
    ax1.plot(pivot_data.index, pivot_data['CO2_Emissions_tons_per_capita'], label='CO2 Emissionen (t/Kopf)',
             color='red', marker='o')
    ax1.plot(pivot_data.index, pivot_data['Avg_Temperature_degC'], label='Durchschn. Temperatur (°C)', color='orange',
             marker='s')
    ax1.set_xlabel('Jahr')
    ax1.set_ylabel('CO2 / Temperatur')
    ax1.legend(loc='upper left')
    ax1.grid(True)

    # Rechte Achse: Extreme Wetterereignisse
    ax2 = ax1.twinx()
    ax2.plot(pivot_data.index, pivot_data['Extreme_Weather_Events'], label='Extreme Wetterereignisse', color='purple',
             linestyle='--', marker='^')
    ax2.set_ylabel('Extreme Wetterereignisse')
    ax2.legend(loc='upper right')

    # Titel und Layout anpassen
    plt.title("Klimawandel – CO2, Temperatur und Extreme Wetterereignisse im Vergleich")
    plt.tight_layout()

    # Grafik speichern
    plt.savefig("derking_finale_klimatrends.png", dpi=300)
    plt.show()


# 3. Hauptfunktion
def main():
    # Daten laden
    pfad = "temperature.csv"
    pivot_data = lade_und_berechne_daten(pfad)

    # Grafik erstellen
    erstelle_finale_grafik(pivot_data)


if __name__ == "__main__":
    main()
