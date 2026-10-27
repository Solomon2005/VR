import bpy

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# КЕЙС 5. Инстансинг: расстановка объектов циклом
count = 0

for row in range(5):
    for col in range(5):
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(col * 2, row * 2 + 5, 0.5)
        )
        bpy.context.object.name = f"Tile_{row}_{col}"
        count += 1

print("\nКЕЙС 5")
print("Создано объектов:", count)