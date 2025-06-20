# Data Platform Project

A project for building a data platform based on Apache Airflow, ClickHouse, Superset, and Jupyter.  
The goal is to automate the generation, loading, and visualization of synthetic data with geospatial references.

---

## Platform Components

- **Airflow** – orchestration of ETL/ELT pipelines  
- **ClickHouse** – analytical database  
- **Superset** – BI system for data visualization  
- **Jupyter Notebooks** – data generation and loading  
- **Leaflet.js** – custom map-based data visualization  

---

## Project Structure

```bash
├── data/                          # CSV files and Jupyter notebooks
│   ├── *_dummy_generator.ipynb     # synthetic data generators
│   ├── *_to_clickhouse.ipynb       # loaders to ClickHouse
│   └── *.csv                       # resulting datasets
│
├── superset_map/                  # geospatial data visualization
│   ├── e_otinsh_dummy.csv
│   ├── urgent_map.html             # interactive map with tooltips
│   └── urgent_map.py               # map generator script
│
├── docker-compose.yml             # platform launcher
├── Dockerfile                     # for Airflow
├── Dockerfile.superset            # for Superset
├── requirements.txt               # Python dependencies
└── .gitignore
```

---

## How to Run

```bash
git clone https://github.com/sobebaa/data-platform.git
cd data-platform
docker-compose up --build
```

---

## Geospatial Map

`urgent_map.html` is a Leaflet.js-based generated map that visualizes synthetic data.  
Each point includes tooltip information: region, age, category, gender, urgency, and status.

![map preview](./superset_map/urgent_map.html)

---

## Sample Data

The notebooks generate datasets related to:

- school students (`kezekte_school_dummy.csv`)
- eOtinish public requests (`e_otinish_dummy.csv`)
- family data cards (`synthetic_family_cards.csv`)

Loader notebooks allow seamless data import into ClickHouse and Superset.

---

[GitHub: @sobebaa](https://github.com/sobebaa)
