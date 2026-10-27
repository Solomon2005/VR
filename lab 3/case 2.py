import bpy

# Очистка сцены
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Куб из кейса 1 (нужен для назначения материала)
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.object
cube.name = "VR_Cube"

# КЕЙС 2. PBR-материал для объекта (Principled BSDF)
mat = bpy.data.materials.new(name="VR_Material")
mat.use_nodes = True

bsdf = mat.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (0.03, 0.18, 0.8, 1)
bsdf.inputs["Roughness"].default_value = 0.3

cube.data.materials.append(mat)

print("\nКЕЙС 2")
print("Материал назначен:", mat.name)
print("Материалов на объекте:", len(cube.data.materials))