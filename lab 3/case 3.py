import bpy
from mathutils import Vector

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# КЕЙС 3. Настройка стереокамеры для VR (multiview)
bpy.ops.object.camera_add(location=(7, -10, 6))
camera = bpy.context.object
camera.name = "VR_Camera"

# Направляем камеру на точку (0, 0, 1)
direction = Vector((0, 0, 1)) - camera.location
camera.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()

scene = bpy.context.scene
scene.camera = camera
scene.render.use_multiview = True
scene.render.views_format = 'STEREO_3D'

print("\nКЕЙС 3")
print("Стерео включено:", scene.render.use_multiview)

try:
    camera.data.stereo.interocular_distance = 0.065
    print("Межзрачковое расстояние:", camera.data.stereo.interocular_distance)
except (AttributeError, TypeError):
    print("Настройка межзрачкового расстояния недоступна")