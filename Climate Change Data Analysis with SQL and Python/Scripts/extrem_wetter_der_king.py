import pandas as pd
import matplotlib.pyplot as plt

# Hol ma des Klima-Daten nei – muaß im gleiche Ordner sei
df = pd.read_csv("temperature.csv")

# Basteln mia a Pivot-Tabelle: Jahr → Durchschnitt von extreme Wetter
pivot_extreme_weather = df.pivot_table(
    index='Year',
    values='Extreme_Weather_Events',
    aggfunc='mean'
)

# Zeichnen mia a sauberes Liniendiagramm – dramatisch und ehrlich!
pivot_extreme_weather.plot(
    marker='o',
    linestyle='-',
    figsize=(10, 6),
    color='purple',
    legend=False
)

# Beschriftung für den DER KING Wetterbericht
plt.title("Durchschnittliche Anzahl extremer Wetterereignisse pro Jahr")
plt.xlabel("Jahr")
plt.ylabel("Extreme Wetterereignisse (Anzahl)")
plt.grid(True)
plt.tight_layout()

# Speichern mia des Bild in da Schatzkammer
plt.savefig("extrem_wetter_der_king.png", dpi=300)

# Zeign mia’s zur Lagebesprechung
plt.show()
