import pandas as pd
import folium

# Координаты регионов
region_coords = {
    "Нур-Султан": [51.1605, 71.4704],
    "Актобе": [50.2839, 57.1660],
    "Тараз": [42.9, 71.3667],
    # добавь другие регионы, если они есть
}

# Загрузка данных
df = pd.read_csv("synthetic_family_cards.csv")  # путь к твоему файлу

# Добавление координат
df["lat"] = df["region"].map(lambda r: region_coords.get(r, [None, None])[0])
df["lon"] = df["region"].map(lambda r: region_coords.get(r, [None, None])[1])
df = df.dropna(subset=["lat", "lon"])

# Цвет по категории
def get_color(category):
    if category == "многодетная":
        return "red"
    elif category == "малоимущая":
        return "orange"
    elif category == "пенсионеры":
        return "blue"
    elif category == "инвалиды":
        return "green"
    else:
        return "gray"

# Создание карты
m = folium.Map(location=[48.5, 66.5], zoom_start=5)

# Добавление точек
for _, row in df.iterrows():
    popup_text = f"""
    <b>Регион:</b> {row['region']}<br>
    <b>Город:</b> {row['city']}<br>
    <b>Категория семьи:</b> {row['family_category']}<br>
    <b>Дети:</b> {row['children_count']} | Пожилые: {'Да' if row['has_elderly_member'] else 'Нет'}<br>
    <b>Доход:</b> {row['average_income']} ₸<br>
    <b>Тип жилья:</b> {row['housing_type']}
    """
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=4 + row["children_count"],
        color=get_color(row["family_category"]),
        fill=True,
        fill_opacity=0.6,
        popup=popup_text
    ).add_to(m)

# Сохранение
m.save("family_map.html")
print("✅ Карта сохранена как family_map.html")