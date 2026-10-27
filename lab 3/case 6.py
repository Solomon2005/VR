import bpy

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# КЕЙС 6. Освещение VR-сцены (источник Sun)
bpy.ops.object.light_add(type='SUN', location=(0, 0, 8))
sun = bpy.context.object
sun.name = "VR_Sun"
sun.data.energy = 4

print("\nКЕЙС 6")
print("Источник света:", sun.name)
print("Тип:", sun.data.type)
print("Мощность:", sun.data.energy)