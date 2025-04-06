-- 🌍 Joahr für Joahr – wie wird’s denn wärmer im Durchschnit?
SELECT year, ROUND(AVG(avg_temperature_degC), 2) AS avg_global_temp
FROM climate_data
GROUP BY year
ORDER BY year;

-- 🌪️ Wer hod’s kracha lassen? De Top 5 mit de meisten Unwetter
SELECT country, SUM(extreme_weather_events) AS total_extreme_events
FROM climate_data
GROUP BY country
ORDER BY total_extreme_events DESC
LIMIT 5;

-- 📈 Gibt’s an Zusammenhang zwischen Schmaddl und Hitze?
SELECT year,
       ROUND(AVG(co2_emissions_tons_per_capita), 2) AS avg_co2,
       ROUND(AVG(avg_temperature_degC), 2) AS avg_temp
FROM climate_data
GROUP BY year
ORDER BY year;

-- 🔥 Wer hod am meista zuaheizt? De 10 heißesten Länder im Vergleich
SELECT country,
       MAX(avg_temperature_degC) - MIN(avg_temperature_degC) AS temp_increase
FROM climate_data
GROUP BY country
ORDER BY temp_increase DESC
LIMIT 10;

-- 🌳 Wo is da Woid hi? Länder mit’m größten Verlust an Bäum
SELECT country,
       MAX(forest_area_pct) - MIN(forest_area_pct) AS forest_loss
FROM climate_data
GROUP BY country
ORDER BY forest_loss ASC
LIMIT 10;
