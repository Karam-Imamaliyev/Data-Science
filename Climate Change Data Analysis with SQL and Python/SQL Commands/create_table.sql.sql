DROP TABLE IF EXISTS climate_data;

CREATE TABLE climate_data (
    year INT,
    country VARCHAR(100),
    avg_temperature_degC FLOAT,
    co2_emissions_tons_per_capita FLOAT,
    sea_level_rise_mm FLOAT,
    rainfall_mm INT,
    population BIGINT,
    renewable_energy_pct FLOAT,
    extreme_weather_events INT,
    forest_area_pct FLOAT
);
