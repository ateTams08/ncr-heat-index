# NCR Heat Index Dashboard

**Course:** DSA4154 - Information Presentation and Visualization <br>
**Program:** BS Data Science and Analytics <br>
**University:** University of Santo Tomas <br>
**Group 4**

Aira Beatrice A. Donato | Atasha Samantha T. Geronimo | Zarinah Lindsay C. Gianan
Cherelle Valkyrie R. Oyales | John Dennis V. Vergara | Alecsandra Z. Villanueva

---

## About the Project

This project is a live, automated heat index dashboard for the 17 cities and municipalities of Metro Manila (NCR). It aims to inform the public about current and upcoming heat conditions to help them make safer decisions during extreme heat events.

---

## Data Source

**API:** OpenMeteo Weather Forecast API

**URL:** [placeholder]

**Variables:**
- `temperature_2m` — Actual air temperature (°C) at 2 meters above ground
- `relative_humidity_2m` — Relative humidity (%) at 2 meters above ground
- `apparent_temperature` — Heat index; how hot it actually feels combining temperature, humidity, and wind

**Coverage:** 18 locations across Metro Manila (Caloocan is split into North and South)

**Time Range:** Past 7 days + 14-day forecast, updated daily

---

## Repository Structure

| File | Description |
|---|---|
| `main.py` | Main Python extraction script |
| `requirements.txt` | Python dependencies |
| `service-account.json` | Google Cloud credentials (private) |
| `.github/workflows/daily_update.yml` | GitHub Actions scheduler |
| `README.md` | Project documentation |

---

## How It Works

1. **Data Extraction** — main.py fetches hourly temperature, humidity, and apparent temperature for 18 NCR locations from the OpenMeteo API.
2. **Data Transformation** — Data is cleaned, timestamps are set to Philippine Standard Time (GMT+8), and heat index values are classified using PAGASA risk levels.
3. **Data Storage** — The processed data is automatically appended to a Google Sheets file via Google Cloud.
4. **Automation** — GitHub Actions runs the pipeline every day at 8:00 AM Manila Time.
5. **Visualization** — Tableau Public connects to Google Sheets with 24-hour sync to display the live dashboard.

---

## PAGASA Heat Index Risk Levels

| Heat Index (°C) | Risk Level |
|---|---|
| 27 – 32 | Caution |
| 33 – 41 | Extreme Caution |
| 42 – 51 | Danger |
| 52+ | Extreme Danger |

---

## Live Dashboard

[placeholder]

---

## License

This project is open-source and intended for public use in accordance with the theme of helping the Filipino people.
