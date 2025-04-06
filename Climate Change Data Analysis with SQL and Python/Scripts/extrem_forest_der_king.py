import pandas as pd
import matplotlib.pyplot as plt

# Hol ma de Daten nei – muaß im Projekt-Ordner drin sei
df = pd.read_csv("temperature.csv")

# Basteln mia Kategorien für extreme Wetterereignisse – vo wenig bis brutal
df['Extreme_Weather_Category'] = pd.cut(
    df['Extreme_Weather_Events'],
    bins=[0, 5, 10, 15, 20, 25, 30],
    labels=['0–5', '6–10', '11–15', '16–20', '21–25', '26–30']
)

# Rechnen mia, wie vü Wald in jeder Katastrophen-Kategorie übrig bleibt
pivot_extreme_forest = df.pivot_table(
    index='Extreme_Weather_Category',
    values='Forest_Area_pct',
    aggfunc='mean',
    observed=False  # Damit’s koane Zukunfts-Schimpf gibt
)

# Zeichnen mia des Ganze – grün wie da tiefste Bayerwald
pivot_extreme_forest.plot(kind='bar', figsize=(10, 6), legend=False, color='darkgreen')

# Beschriftung für Förster, Feuerwehr und DER KING
plt.title("Waldanteil nach Häufigkeit extremer Wetterereignisse")
plt.xlabel("Anzahl extremer Wetterereignisse (Kategorie)")
plt.ylabel("Waldfläche (%)")
plt.grid(True, axis='y')
plt.xticks(rotation=0)
plt.tight_layout()

# Speichern mia des Beweisstück fürs DER KING Archiv
plt.savefig("extrem_forest_der_king.png", dpi=300)

# Zeign mia’s no für Freigabe durch Oberkommando
plt.show()
