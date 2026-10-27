import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# КЕЙС 1. Создание примитива для VR-сцены
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.object
cube.name = "VR_Cube"

print("\nКЕЙС 1")
print("Создан объект:", cube.name)
print("Вершин:", len(cube.data.vertices))
print("Граней:", len(cube.data.polygons))