import math
import numpy as np

# КЕЙС 9.
head = np.array([0.0, -2.0, 1.6])
ipd = 0.065

left_eye = head - np.array([ipd / 2, 0, 0])
right_eye = head + np.array([ipd / 2, 0, 0])

distance_eyes = np.linalg.norm(right_eye - left_eye)

print("\nКЕЙС 9. Стереокамеры")
print("Левый глаз:", left_eye)
print("Правый глаз:", right_eye)
print(f"Расстояние между камерами: {distance_eyes:.3f} м")


# КЕЙС 10.
fov = 100
distance = 5
object_width = 2

visible_width = 2 * distance * math.tan(math.radians(fov / 2))
fraction = object_width / visible_width * 100

print("\nКЕЙС 10. Поле зрения")
print(f"FOV: {fov} град")
print(f"Ширина видимой области: {visible_width:.2f} м")
print(f"Объект занимает {fraction:.1f}% ширины кадра")


# КЕЙС 11.
angle = math.radians(90)

q = [
    math.cos(angle / 2),
    0,
    0,
    math.sin(angle / 2)
]

# Поворачиваем вектор (0, 1, 0) вокруг оси Z
x = -math.sin(angle)
y = math.cos(angle)
z = 0

print("\nКЕЙС 11. Кватернион")
print("Кватернион:", np.round(q, 3))
print("Вектор до поворота: [0, 1, 0]")
print("Вектор после поворота:", np.round([x, y, z], 3))


# КЕЙС 12.
render_time = 9.5

print("\nКЕЙС 12. Бюджет кадра")

for hz in [72, 90, 120]:
    budget = 1000 / hz
    print(f"{hz} Гц -> {budget:.2f} мс")

budget = 1000 / 90

print("Рендер при 90 Гц:",
      "успеваем" if render_time <= budget else "НЕ успеваем")


# КЕЙС 13.
print("\nКЕЙС 13. Выбор LOD")

for d in [2, 10, 35, 80]:
    if d <= 5:
        lod = "LOD0 (высокая детализация)"
    elif d <= 20:
        lod = "LOD1 (средняя)"
    elif d <= 50:
        lod = "LOD2 (низкая)"
    else:
        lod = "culled (не рендерится)"

    print(f"{d} м -> {lod}")


# КЕЙС 14.
budget = 1_000_000
triangles = 8_000
objects = 150

max_objects = budget // triangles
total = objects * triangles

print("\nКЕЙС 14. Полигональный бюджет")
print("Максимум объектов:", max_objects)
print("Всего треугольников:", total)
print("Результат:",
      "в бюджете" if total <= budget else "ПРЕВЫШЕН бюджет")


#  КЕЙС 15.
latencies = [2, 3, 11, 4]
total_latency = sum(latencies)

print("\nКЕЙС 15. Motion-to-photon")
print("Суммарная задержка:", total_latency, "мс")
print("Комфортно (< 20 мс)?", total_latency < 20)