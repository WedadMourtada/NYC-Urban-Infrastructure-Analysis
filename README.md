Urban Infrastructure Data Analysis combines open NYC traffic, energy demand, and weather data to analyze cross‑system patterns and simulate resource‑use scenarios (e.g., +5 °C temperature, −10% traffic volume).

**Why this project?**
Right now, NYC traffic, energy, and weather data are stored separately and in different formats, making it hard to connect them. This project creates a clear, repeatable process (pipeline) to bring these datasets together, clean them, and align them on the same timeline. With interactive dashboards, we can test “what-if” scenarios—like hotter days or reduced traffic—and see how these changes might impact electricity demand in NYC.
It’s hard to answer: “How do weather and traffic changes affect energy demand?” because NYC has tons of open data and it’s scattered and inconsistent:
- Different sources (traffic, energy, weather) live in separate systems.
- Different formats & units (CSV vs API, °F vs °C, kW vs MW).
- Different time scales (5-min traffic, hourly energy, daily weather).
- Different locations (boroughs, sensors, zones) that don’t line up.

**Solution**
I'm building a single, clean pipeline that:
-Collects traffic, energy load, and weather data.
- Cleans & standardizes them (units, timestamps, locations).
- Aligns them to the same time grid and NYC geography.
- Analyzes patterns/relationships (e.g., hotter days → higher load; lower traffic → any effect?).
- Simulates “what-if” scenarios (e.g., +5 °C, −10% traffic) to see expected changes in demand.
- Visualizes results in interactive dashboards so non-coders can explore.

**Key features**
- Data ingestion & cleaning in Python (Pandas)
- Schema‑aligned datasets ready for analysis
- Scenario engine to apply counterfactuals (e.g., temp/traffic adjustments)
- Interactive dashboards (Tableau) for trends & scenarios
- Reproducible environment (requirements + make targets)

**Data Sources**

Data Plan
Type of data and scale:
Where and how do to get the data:
