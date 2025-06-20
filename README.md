# Data Platform Project

Проект по созданию дата-платформы на базе Apache Airflow, ClickHouse, Superset и Jupyter.  
Цель — автоматизация генерации, загрузки и визуализации синтетических данных с привязкой к географическим координатам.

---

## Компоненты платформы

- **Airflow** – оркестрация ETL/ELT процессов
- **ClickHouse** – аналитическая база данных
- **Superset** – BI-система для визуализации данных
- **Jupyter Notebooks** – генерация и загрузка данных
- **Leaflet.js** – кастомная карта с визуализацией данных

---

## Структура проекта

```bash
├── data/                      # CSV-файлы и Jupyter ноутбуки
│   ├── *_dummy_generator.ipynb     # генераторы синтетических данных
│   ├── *_to_clickhouse.ipynb       # загрузка данных в ClickHouse
│   └── *.csv                       # итоговые таблицы
│
├── superset_map/              # Геокарта с визуализацией данных
│   ├── e_otinsh_dummy.csv
│   ├── urgent_map.html             # карта с точками и всплывающей аналитикой
│   └── urgent_map.py               # генератор HTML-карты
│
├── docker-compose.yml         # Запуск платформы
├── Dockerfile                 # Airflow
├── Dockerfile.superset        # Superset
├── requirements.txt           # Python-зависимости
└── .gitignore
```

---

## Как запустить

```bash
git clone https://github.com/sobebaa/data-platform.git
cd data-platform
docker-compose up --build
```

---

## Геокарта

`urgent_map.html` — это сгенерированная карта на Leaflet.js, визуализирующая синтетические данные.  
Каждая точка содержит всплывающее описание: регион, возраст, категория, пол, срочность и статус.

![map preview](./superset_map/urgent_map.html)

---

## Примеры данных

Генераторы создают данные о:

- учениках школ (`kezekte_school_dummy.csv`)
- eOtinish обращениях (`e_otinish_dummy.csv`)
- семейных картах (`synthetic_family_cards.csv`)

Сценарии загрузки позволяют сразу перенести данные в ClickHouse и Superset.


---

[GitHub: @sobebaa](https://github.com/sobebaa)
