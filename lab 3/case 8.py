import bpy
import math
import os

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Подготовка сцены для экспорта: куб + материал + анимация (кейсы 1, 2, 7)
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.object
cube.name = "VR_Cube"

mat = bpy.data.materials.new(name="VR_Material")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (0.03, 0.18, 0.8, 1)
bsdf.inputs["Roughness"].default_value = 0.3
cube.data.materials.append(mat)

scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 60
cube.rotation_euler.z = 0
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=1)
cube.rotation_euler.z = 2 * math.pi
cube.keyframe_insert(data_path="rotation_euler", index=2, frame=60)

# КЕЙС 8. Экспорт сцены в glTF (GLB) для VR-движка
export_path = os.path.join(os.path.expanduser("~"), "vr_scene.glb")

try:
    bpy.ops.export_scene.gltf(
        filepath=export_path,
        export_format='GLB',
        export_animations=True
    )
    print("\nКЕЙС 8")
    print("Экспортировано в:", export_path)

except Exception as e:
    print("\nОшибка экспорта:", e)