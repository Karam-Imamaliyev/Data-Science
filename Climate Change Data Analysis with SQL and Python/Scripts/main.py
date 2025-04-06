import pandas as pd

# 📦 1. Da holen ma uns des Wetterdings aus'm CSV
df = pd.read_csv("temperature.csv")

# 📄 2. Hier leg ma uns an Sackl zamm, wo ma de SQL-Befehle eini haun
insert_queries = []

# 🔁 3. Jetzt gemma jedes Zeile durch – wie in da Früh beim Semmeln holen
for _, row in df.iterrows():
    query = f"""
    INSERT INTO climate_data (
        year, country, avg_temperature_degC, co2_emissions_tons_per_capita,
        sea_level_rise_mm, rainfall_mm, population, renewable_energy_pct,
        extreme_weather_events, forest_area_pct
    ) VALUES (
        {int(row['Year'])},
        '{row['Country'].replace("'", "''")}',  -- Oiso wenn a Hochkomma drin is, dua ma doppelt
        {row['Avg_Temperature_degC']},
        {row['CO2_Emissions_tons_per_capita']},
        {row['Sea_Level_Rise_mm']},
        {row['Rainfall_mm']},
        {int(row['Population'])},
        {row['Renewable_Energy_pct']},
        {int(row['Extreme_Weather_Events'])},
        {row['Forest_Area_pct']}
    );
    """
    insert_queries.append(query.strip())

# 🧾 4. Und jetz pack ma des ois zamm in a SQL-Datei, fein säuberlich
with open("load_data.sql", "w", encoding="utf-8") as file:
    file.write("\n".join(insert_queries))

print("✅ Fertig! De INSERT-Befehle san jetzt in 'load_data.sql'. Auf geht’s!")
