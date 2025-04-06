import pandas as pd
import matplotlib.pyplot as plt

# Les ma des Klima-Daten nei – wichtig fürs DER KING Archiv
df = pd.read_csv("temperature.csv")

# Mach ma aus Waldfläche a schene Klass’n – von kloa bis riesig
df['Forest_Cover_Category'] = pd.cut(
    df['Forest_Area_pct'],
    bins=[0, 10, 20, 30, 40, 50, 60, 100],
    labels=['<10%', '10–20%', '20–30%', '30–40%', '40–50%', '50–60%', '>60%']
)

# Berechn ma, wie vü CO2 pro Kopf in jeder Wald-Klasse ausgstoß’n werd
pivot_forest_co2 = df.pivot_table(
    index='Forest_Cover_Category',
    values='CO2_Emissions_tons_per_capita',
    aggfunc='mean',
    observed=False  # keine Warnung wird kommen
)

# Zeichnen mia a barplot – mit da grün'n Kraft vo da Natur
pivot_forest_co2.plot(kind='bar', figsize=(10, 6), legend=False, color='green')

# Beschriftung wie beim Förster-Stammtisch
plt.title("CO2-Emissionen nach Waldanteil")
plt.xlabel("Waldanteil (%)")
plt.ylabel("CO2 Emissionen (Tonnen pro Kopf)")
plt.grid(True, axis='y')
plt.xticks(rotation=0)
plt.tight_layout()

# Speichern mia des Meisterwerk fürs DER KING GitHub-Museum
plt.savefig("wald_co2_der_king.png", dpi=300)

# Zeign mia's no dem General zur Freigabe
plt.show()
