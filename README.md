# HeatBeat: NCR Heat Index Dashboard

**Course:** DSA4154 - Information Presentation and Visualization  
**Program:** BS Data Science and Analytics  
**University:** University of Santo Tomas  

## 2DSA2 - Group 4
- Atasha Samantha T. Geronimo  
- Zarinah Lindsay C. Gianan  
- Cherelle Valkyrie R. Oyales  
- John Dennis V. Vergara  
- Alecsandra Z. Villanueva  

---

# Project Overview

HeatBeat is a live, automated heat index monitoring dashboard for the National Capital Region (NCR), Philippines. The project tracks and visualizes hourly heat index conditions across Metro Manila using automated weather data pipelines and interactive visual analytics.

The dashboard aims to improve public awareness of heat-related risks by providing accessible, real-time, and forecasted heat index information based on PAGASA heat risk classifications.

---

# Project Objectives

- Monitor hourly heat index conditions across NCR
- Provide accessible and interactive public heat risk visualizations
- Automate the full data pipeline without manual uploads
- Support heat awareness and data-driven decision-making during extreme heat events

---

# Technologies Used

| Component | Technology |
|---|---|
| Data Extraction | Python |
| API Source | Open-Meteo Weather API |
| Automation | GitHub Actions |
| Cloud Storage | Google Sheets API |
| Visualization | Tableau Public |
| Authentication | Google Cloud Service Account |

---

# Data Source

## Open-Meteo Weather Forecast API

The project uses the Open-Meteo API to retrieve hourly weather forecast data for NCR locations.

**API Documentation:**  
https://open-meteo.com/en/docs

### Variables Collected

- `temperature_2m` — Actual air temperature (°C)
- `relative_humidity_2m` — Relative humidity (%)
- `apparent_temperature` — Heat index or perceived temperature

### Coverage

- 18 NCR locations
- Caloocan separated into North and South districts

### Forecast Range

- 14-day forecast
- Updated daily at 8:00 AM Philippine Standard Time

---

# PAGASA Heat Risk Classification

| Heat Index (°C) | Risk Level |
|---|---|
| Below 27 | Non-Hazardous |
| 27–32 | Caution |
| 33–41 | Extreme Caution |
| 42–51 | Danger |
| 52+ | Extreme Danger |

---

# Automation Workflow

## 1. Data Extraction

`main.py` retrieves hourly forecast data from the Open-Meteo API for all NCR locations.

## 2. Data Transformation

The pipeline:

- Cleans and standardizes records
- Converts timestamps to Philippine Standard Time (GMT+8)
- Classifies heat index values using PAGASA risk levels

## 3. Cloud Storage

Processed data is automatically uploaded to Google Sheets through the Google Sheets API.

## 4. Automated Scheduling

GitHub Actions executes the pipeline daily at 8:00 AM Manila Time without requiring manual intervention.

## 5. Dashboard Visualization

Tableau Public connects directly to Google Sheets using the Google Drive connector with scheduled refresh enabled.

---

# Cloud Storage Resources

| Resource | Purpose |
|---|---|
| Weather Dataset Sheet | Stores automated hourly NCR weather and heat index data |
| Heat Risk Reference Sheet | Stores static PAGASA heat risk classifications used in dashboard legends and interpretation |

---

# Repository Structure

```plaintext
ncr-heat-index/
├── .github/
│   └── workflows/
│       └── daily_update.yml      # GitHub Actions automation workflow
├── main.py                       # Main extraction and transformation script
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
└── .gitignore                    # Excludes private credentials
```

> Note: Private credentials such as `service-account.json` are excluded from the repository through `.gitignore` for security purposes.

---

# Dashboard Features

- Live and automated heat index monitoring across NCR
- Daily automated dataset updates through GitHub Actions
- Interactive dashboard visualization using Tableau Public
- PAGASA-based heat risk classifications through color-coded indicators
- Interactive filters by location and date for easier data exploration
- Heat maps and hourly heat index visualizations
- Dynamic 14-day forecast exploration
- Top hottest cities monitoring
- Automated “Last Updated” timestamp tracking
- Centralized and publicly accessible heat index information

---

# Data Cleaning & Calculated Fields

The dashboard applies several preprocessing and calculated logic steps to improve consistency, readability, and analytical interpretation.

## Data Cleaning
- Converted timestamps to Philippine Standard Time (GMT+8)
- Standardized hourly datetime formatting
- Structured data by city, date, and hourly forecast intervals

## Tableau Calculated Fields

### Heat Risk Level
Classifies heat index values according to PAGASA heat risk thresholds.

```tableau
IF FLOAT([Apparent Temp]) >= 52 THEN "Extreme Danger"
ELSEIF FLOAT([Apparent Temp]) >= 42 THEN "Danger"
ELSEIF FLOAT([Apparent Temp]) >= 33 THEN "Extreme Caution"
ELSEIF FLOAT([Apparent Temp]) >= 27 THEN "Caution"
ELSE "Non-Hazardous"
END
```

### Display Date
Creates dynamic dashboard date labels such as “Today” and forecast dates.

### Peak Heat Hour
Identifies the hour with the highest average NCR heat index for the current day.

### Top Hottest Cities
Ranks NCR cities based on maximum daily apparent temperature values.

---

# How to Read the Dashboard

The dashboard is divided into multiple sections to support both quick monitoring and deeper exploration of NCR heat conditions.

## Today's Overview
Displays today's key heat indicators in the NCR, including:
- Average Heat Index
- Maximum Heat Index
- Hottest NCR Location
- Peak Heat Hour

These KPIs provide a quick summary of current heat conditions across Metro Manila.

## Heat Risk Map
Shows the geographic distribution of heat index levels across NCR cities today using color-coded PAGASA heat risk classifications.

## Hourly Heat Index Grid
Visualizes hourly heat index forecasts per city to help identify:
- Peak heat periods
- High-risk locations
- Daily heat patterns

## Forecast Exploration
Interactive filters allow users to:
- View current and upcoming forecast dates
- Explore hourly heat conditions
- Compare NCR locations dynamically

## Heat Risk Legend
The dashboard uses PAGASA heat risk classifications:

- 🟦 Non-Hazardous (<27°C)
- 🟨 Caution (27°C–32°C)
- 🟧 Extreme Caution (33°C–41°C)
- 🟥 Danger (42°C–51°C)
- 🟥 Extreme Danger (52°C+)

---

# Live Dashboard

The HeatBeat Dashboard provides real-time and forecasted heat index insights across the National Capital Region through interactive visualizations and data-driven analytics. Published through Tableau Public, the dashboard is designed to help users monitor temperature trends, assess heat risk levels, and support informed decision-making for public safety and awareness.

## Tableau Public Dashboard

https://public.tableau.com/views/NCRHeatIndexMonitoringDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

# GitHub Repository

https://github.com/ateTams08/ncr-heat-index/

---

# License

This project is open-source and developed for educational and public awareness purposes related to heat risk monitoring and public safety in the Philippines.
