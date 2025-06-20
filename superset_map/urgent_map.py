import pandas as pd
import folium

region_coords = {
    "г. Астана": [51.1605, 71.4704],
    "г. Алматы": [43.2389, 76.8897],
    "Акмолинская": [51.7, 69.5],
    "Актюбинская": [48.0, 57.0],
    "Алматинская": [45.0, 79.0],
    "Карагандинская": [49.8, 73.1],
    "Мангистауская": [44.0, 52.9],
    "Туркестанская": [42.5, 68.5],
    "Западно-Казахстанская": [50.1, 51.2],
    "Северо-Казахстанская": [54.0, 69.0],
}

# Загрузка CSV-файла
df = pd.read_csv("e_otinish_dummy.csv")

# Привязка координат по регионам
df["lat"] = df["Регион"].map(lambda r: region_coords.get(r, [None, None])[0])
df["lon"] = df["Регион"].map(lambda r: region_coords.get(r, [None, None])[1])
df = df.dropna(subset=["lat", "lon"])

# Цветовая схема по срочности
def get_color(urgency):
    if urgency == "Высокая":
        return "red"
    elif urgency == "Средняя":
        return "orange"
    else:
        return "green"

# Создание карты
m = folium.Map(location=[48.5, 66.5], zoom_start=5)

# Добавление точек на карту
for _, row in df.iterrows():
    popup_text = f"""
    <b>Регион:</b> {row['Регион']}<br>
    <b>Дата:</b> {row['Дата обращения']}<br>
    <b>Категория:</b> {row['Категория']} / {row['Подкатегория']}<br>
    <b>Статус:</b> {row['Статус']}<br>
    <b>Срочность:</b> {row['Категория срочности']}<br>
    <b>Пол:</b> {row['Пол']} | Возраст: {row['Возраст заявителя']}
    """
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=7,
        color=get_color(row["Категория срочности"]),
        fill=True,
        fill_opacity=0.7,
        popup=popup_text
    ).add_to(m)

# Сохранение карты
m.save("urgent_map.html")
print("✅ Карта сохранена как urgent_map.html")