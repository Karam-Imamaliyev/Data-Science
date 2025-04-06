import pandas as pd
import matplotlib.pyplot as plt

# Les ma des CSV ein – sog i, der Datei muaß im gleiche Ordner sein
df = pd.read_csv("temperature.csv")

# Mach ma a Pivot – Durchschnitt pro Jahr für Temperatur und Meeresspiegel
pivot_sea_temp = df.pivot_table(index='Year', values=['Avg_Temperature_degC', 'Sea_Level_Rise_mm'], aggfunc='mean')

# Bauen mia zwoa Achsen auf – links is warm, rechts is naß 
fig, ax1 = plt.subplots(figsize=(12, 6))

# Linke Achse: Temperatur in Rot
ax1.plot(pivot_sea_temp.index, pivot_sea_temp['Avg_Temperature_degC'],
         color='red', marker='o', label='Temperatur (°C)')
ax1.set_xlabel('Jahr')
ax1.set_ylabel('Temperatur (°C)', color='red')
ax1.tick_params(axis='y', labelcolor='red')

# Rechte Achse: Meeresspiegel in Blau
ax2 = ax1.twinx()
ax2.plot(pivot_sea_temp.index, pivot_sea_temp['Sea_Level_Rise_mm'],
         color='blue', marker='s', label='Meeresspiegelanstieg (mm)')
ax2.set_ylabel('Meeresspiegel (mm)', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# Titel und Feintuning
plt.title('Temperatur vs. Meeresspiegelanstieg pro Jahr')
plt.grid(True)
fig.tight_layout()

# Speichern mia des Meisterwerk
plt.savefig("meer_temp_der_king.png", dpi=300)

# No herzeign – für den General!
plt.show()
