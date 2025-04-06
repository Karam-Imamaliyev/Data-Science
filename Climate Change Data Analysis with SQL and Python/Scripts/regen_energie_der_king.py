import pandas as pd
import matplotlib.pyplot as plt

# Les ma des Klima-Daten nei – muaß im gleiche Ordner sei
df = pd.read_csv("temperature.csv")

# Kategorisiern mia de Niederschlagswerte – von "Az" bis "Sehr viel"
df['Rainfall_Category'] = pd.cut(
    df['Rainfall_mm'],
    bins=[0, 1000, 1500, 2000, 2500, 3000],
    labels=['Az Yağış', 'Orta Az', 'Orta', 'Orta Çok', 'Çok Yağış']
)

# Für jede Kategorie den Schnitt von erneuerbare Energie rechnen
pivot_rain_renew = df.pivot_table(
    index='Rainfall_Category',
    values='Renewable_Energy_pct',
    aggfunc='mean',
    observed=False  # keine error bekommen
)


# Zeichnen mia a Barplot
pivot_rain_renew.plot(kind='bar', figsize=(10, 6), legend=False, color='orange')

# Beschriftung, damit jeder Trottel des versteht
plt.title("Wie viel Regen bringt saubere Energie?")
plt.xlabel("Regen-Klasse")
plt.ylabel("Saubere Kraft in Prozent")

plt.grid(True, axis='y')
plt.xticks(rotation=0)
plt.tight_layout()

# Speichern mia des Werk ins Lager
plt.savefig("regen_energie_der_king.png", dpi=300)

# Zeign mia’s da Welt
plt.show()
