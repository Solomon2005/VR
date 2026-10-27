import bpy

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# КЕЙС 4. Оптимизация меша под 90 FPS (модификатор Decimate)
bpy.ops.mesh.primitive_ico_sphere_add(
    subdivisions=3, radius=1, location=(4, 0, 1)
)
sphere = bpy.context.object
sphere.name = "VR_LOD_Sphere"

original = sum(len(p.vertices) - 2 for p in sphere.data.polygons)

modifier = sphere.modifiers.new("Decimate", 'DECIMATE')
modifier.ratio = 0.25

bpy.context.view_layer.objects.active = sphere
bpy.ops.object.modifier_apply(modifier="Decimate")

result = sum(len(p.vertices) - 2 for p in sphere.data.polygons)

print("\nКЕЙС 4")
print("Было треугольников:", original)
print("Целевое количество:", round(original * 0.25))
print("После упрощения:", result)