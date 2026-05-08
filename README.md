# NCR Heat Index Dashboard

**Course:** DSA4154 - Information Presentation and Visualization <br>
**Program:** BS Data Science and Analytics <br>
**University:** University of Santo Tomas <br>
**2DSA2 - Group 4**

Aira Beatrice A. Donato | Atasha Samantha T. Geronimo | Zarinah Lindsay C. Gianan | 
Cherelle Valkyrie R. Oyales | John Dennis V. Vergara | Alecsandra Z. Villanueva

---

## About the Project

This project is a live, automated heat index dashboard for the 17 cities and municipalities of Metro Manila (NCR). It aims to inform the public about heat conditions and trends to help them make safer decisions during extreme heat events.

---

## Data Source

**API:** OpenMeteo Weather Forecast API

**URL:** https://openmeteo.com/en/docshourly=temperature_2m,relative_humidity_2m,apparent_temperature&past_days=7&forecast_days=14&timezone=Asia%2FSingapore&latitude=14.6184&longitude=120.9651 

**Variables:**
- `temperature_2m` — Actual air temperature (°C) at 2 meters above ground
- `relative_humidity_2m` — Relative humidity (%) at 2 meters above ground
- `apparent_temperature` — Heat index; how hot it actually feels by combining temperature, humidity, and wind

**Coverage:** 18 NCR locations with Caloocan split into North and South districts <br>
**Time Range:** 14-day forecast, updated daily at 8:00 AM Manila Time.

---

## Repository Structure

ncr-heat-index/ <br>
├── .github/ <br>
│   └── workflows/ <br>
│       └── daily_update.yml   # GitHub Actions scheduler <br>
├── main.py                    # Main Python extraction script <br>
├── requirements.txt           # Python dependencies <br>
├── service-account.json       # Private credentials (excluded from public repository) <br>
└── README.md                  # Project documentation <br>

---

## Technologies Used

- **Python** — Data extraction, transformation, and automation
- **OpenMeteo Weather Forecast API** — Weather and heat index data source
- **Google Sheets API** — Cloud-based dataset storage
- **GitHub Actions** — Automated daily pipeline execution
- **Tableau Public** — Interactive dashboard and data visualization
- **Google Cloud Service Account** — Authentication for Google Sheets integration

---

## How It Works

1. **Data Extraction** — main.py fetches hourly temperature, humidity, and apparent temperature for 18 NCR locations from the OpenMeteo API.
2. **Data Transformation** — Data is cleaned, timestamps are set to Philippine Standard Time (GMT+8), and heat index values are classified using PAGASA risk levels.
3. **Data Storage** — The processed data is automatically appended to Google Sheets using the Google Sheets API.
4. **Automation** — GitHub Actions runs the pipeline every day at 8:00 AM Manila Time.
5. **Visualization** — Tableau Public connects to Google Sheets with a daily dashboard refresh to display the live dashboard.

---

## PAGASA Heat Index Risk Levels

| Heat Index (°C) | Risk Level |
|---|---|
| 27 – 32 | Caution |
| 33 – 41 | Extreme Caution |
| 42 – 51 | Danger |
| 52+ | Extreme Danger |

---

## Dashboard Features

- Daily updated heat index monitoring for all NCR cities and municipalities
- Daily automated dataset updates through GitHub Actions
- Interactive dashboard visualization using Tableau Public
- PAGASA-based heat risk classifications through color-coded indicators
- Interactive filters by location and date for easier data exploration
- Heat maps and charts for clearer visualization of high-risk areas
- Centralized and accessible public heat index information

---

## Live Dashboard



**URL:** 
https://public.tableau.com/views/NCRHeatIndexMonitoringDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## License

This project is open-source and developed for educational and public awareness purposes related to heat risk monitoring, in line with the theme of helping Filipinos.
