import pandas as pd
import matplotlib.pyplot as plt

# Des is da CSV-Datei – der muaß im Projekt-Ordner drin sei
df = pd.read_csv("temperature.csv")

# Bauen ma a Pivot-Tabelle: Jahr -> Land -> Temperatur
pivot_temp = df.pivot_table(index='Year', columns='Country', values='Avg_Temperature_degC')

# Nimm ma a paar Lända zum Zeichnen
example_countries = ['USA', 'Germany', 'France']

# Zeichnen ma de Temperatur-Verläufe
pivot_temp[example_countries].plot(figsize=(12, 6), marker='o')

# Beschriftung damit ma net den Durchblick verlier'n
plt.title("Durchschnitts-Temperatur im Jahr – USA, Deutschland, Frankreich")
plt.xlabel("Jahr")
plt.ylabel("Temperatur in °C")
plt.grid(True)
plt.tight_layout()

# Speichern mia des G'schichtl ins Projekt
plt.savefig("temperatur_trend_der_king.png", dpi=300)

# No azeigen zur Kontrolle
plt.show()
