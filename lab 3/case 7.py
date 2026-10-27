import bpy
import math

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Куб из кейса 1 (нужен для анимации)
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.object
cube.name = "VR_Cube"

# КЕЙС 7. Анимация вращения (ключевые кадры)
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 60

cube.rotation_euler.z = 0
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=1)

cube.rotation_euler.z = 2 * math.pi
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=60)

print("\nКЕЙС 7")
print("Кадры:", scene.frame_start, "-", scene.frame_end)
print("Ключевых кадров: 2")