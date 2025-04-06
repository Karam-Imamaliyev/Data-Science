import pandas as pd
import matplotlib.pyplot as plt

# Les ma des CSV ein – muaß im gleiche Ordner sei
df = pd.read_csv("temperature.csv")

# Mach ma a Pivot – für jedes Land den Durchschnitt von CO2 pro Kopp
pivot_co2 = df.pivot_table(index='Country', values='CO2_Emissions_tons_per_capita', aggfunc='mean')

# Sortiern mia des gscheid – de, wo am meisten rauspusten, ganz oben
pivot_co2_sorted = pivot_co2.sort_values(by='CO2_Emissions_tons_per_capita', ascending=False)

# Zeichnen mia a Bar-Diagramm draus
pivot_co2_sorted.plot(kind='bar', figsize=(12, 6))


# A paar gschaide Beschriftungen, damit’s da Opa a versteh'd
plt.title("Durchschnittliche CO2-Emission pro Kopf – Länder")
plt.ylabel("CO2 Emission in Tonnen pro Mensch")
plt.xlabel("Land")
plt.grid(True, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()

# Und jetz: Speichern mia des Werk in PNG – fürs DER KING Archiv!
plt.savefig("co2_emission_der_king.png", dpi=300)

# Zeign mia’s no schnell her
plt.show()
