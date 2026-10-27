import bpy
import math
from mathutils import Vector
import os


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    for datablocks in (
        bpy.data.meshes,
        bpy.data.curves,
        bpy.data.materials,
        bpy.data.cameras,
        bpy.data.lights
    ):
        for item in list(datablocks):
            if item.users == 0:
                datablocks.remove(item)


def material(name, color, roughness=0.65, metallic=0.0, emission=None):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*color, 1)
    mat.use_nodes = True

    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1)
    bsdf.inputs["Roughness"].default_value = roughness
    bsdf.inputs["Metallic"].default_value = metallic

    if emission:
        bsdf.inputs["Emission Color"].default_value = (*emission, 1)
        bsdf.inputs["Emission Strength"].default_value = 2.0

    return mat


def sphere(name, loc, scale, mat, rotation=(0, 0, 0)):
    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=40,
        ring_count=24,
        location=loc
    )

    obj = bpy.context.object
    obj.name = name
    obj.scale = scale
    obj.rotation_euler = rotation
    obj.data.materials.append(mat)

    bpy.ops.object.shade_smooth()

    return obj


def look_at(obj, point):
    direction = Vector(point) - obj.location
    obj.rotation_euler = direction.to_track_quat(
        '-Z', 'Y'
    ).to_euler()


def make_scene():
    # Материалы
    white = material(
        "Мягкий белый мех",
        (0.92, 0.94, 0.97),
        0.82
    )

    pink = material(
        "Розовый",
        (0.95, 0.42, 0.55),
        0.55
    )

    black = material(
        "Глаза",
        (0.012, 0.018, 0.028),
        0.18
    )

    nose_mat = material(
        "Носик",
        (0.95, 0.58, 0.68),
        0.35
    )

    floor_mat = material(
        "Матовый пол",
        (0.68, 0.73, 0.75),
        0.9
    )

    # Тело и голова
    sphere(
        "Тело",
        (0, 0, 1.15),
        (0.67, 0.53, 0.88),
        white
    )

    sphere(
        "Голова",
        (0, -0.03, 2.25),
        (0.72, 0.61, 0.67),
        white
    )

    # Уши
    sphere(
        "Левое ухо",
        (-0.38, 0.02, 3.05),
        (0.19, 0.16, 0.62),
        white,
        (0, math.radians(-8), math.radians(-5))
    )

    sphere(
        "Правое ухо",
        (0.38, 0.02, 3.07),
        (0.19, 0.16, 0.62),
        white,
        (0, math.radians(8), math.radians(5))
    )

    # Розовая внутренняя часть ушей
    sphere(
        "Внутри левого уха",
        (-0.38, -0.125, 3.08),
        (0.105, 0.055, 0.46),
        pink,
        (0, math.radians(-8), math.radians(-5))
    )

    sphere(
        "Внутри правого уха",
        (0.38, -0.125, 3.10),
        (0.105, 0.055, 0.46),
        pink,
        (0, math.radians(8), math.radians(5))
    )

    # Глаза
    sphere(
        "Левый глаз",
        (-0.27, -0.585, 2.37),
        (0.095, 0.055, 0.13),
        black
    )

    sphere(
        "Правый глаз",
        (0.27, -0.585, 2.37),
        (0.095, 0.055, 0.13),
        black
    )

    # Блики в глазах
    sphere(
        "Блик левого глаза",
        (-0.295, -0.635, 2.415),
        (0.027, 0.018, 0.035),
        white
    )

    sphere(
        "Блик правого глаза",
        (0.245, -0.635, 2.415),
        (0.027, 0.018, 0.035),
        white
    )

    # Нос и щёки
    sphere(
        "Нос",
        (0, -0.665, 2.19),
        (0.085, 0.05, 0.055),
        nose_mat
    )

    sphere(
        "Левая щёчка",
        (-0.22, -0.57, 2.12),
        (0.15, 0.055, 0.105),
        white
    )

    sphere(
        "Правая щёчка",
        (0.22, -0.57, 2.12),
        (0.15, 0.055, 0.105),
        white
    )

    # Руки
    sphere(
        "Левая рука",
        (-0.58, -0.02, 1.27),
        (0.19, 0.20, 0.36),
        white,
        (0, 0, math.radians(-22))
    )

    sphere(
        "Правая рука",
        (0.58, -0.02, 1.27),
        (0.19, 0.20, 0.36),
        white,
        (0, 0, math.radians(22))
    )

    # Лапки
    sphere(
        "Левая лапка",
        (-0.34, -0.02, 0.38),
        (0.22, 0.25, 0.25),
        white
    )

    sphere(
        "Правая лапка",
        (0.34, -0.02, 0.38),
        (0.22, 0.25, 0.25),
        white
    )

    # Хвост
    sphere(
        "Пушистый хвост",
        (0, 0.52, 0.78),
        (0.22, 0.22, 0.22),
        white
    )

    # Пол
    bpy.ops.mesh.primitive_plane_add(
        size=200,
        location=(0, 0, 0.08)
    )

    bpy.context.object.name = "Пол"
    bpy.context.object.data.materials.append(floor_mat)

    # Основной источник света
    bpy.ops.object.light_add(
        type='AREA',
        location=(4, -4, 6)
    )

    key = bpy.context.object
    key.name = "Мягкий основной свет"
    key.data.energy = 650
    key.data.shape = 'DISK'
    key.data.size = 5

    look_at(key, (0, 0, 1.8))

    # Дополнительный свет
    bpy.ops.object.light_add(
        type='AREA',
        location=(-4, -1, 3.5)
    )

    fill = bpy.context.object
    fill.name = "Заполняющий свет"
    fill.data.energy = 300
    fill.data.size = 4

    look_at(fill, (0, 0, 1.8))

    # Камера
    bpy.ops.object.camera_add(
        location=(4.7, -8.5, 4.0)
    )

    cam = bpy.context.object
    cam.name = "Камера"
    cam.data.lens = 55

    look_at(cam, (0, 0, 1.75))

    bpy.context.scene.camera = cam

    # Настройки рендера
    scene = bpy.context.scene
    scene.render.engine = 'BLENDER_EEVEE_NEXT'

    scene.render.resolution_x = 900
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100

    scene.render.image_settings.file_format = 'PNG'

    scene.render.filepath = os.path.join(
        os.path.expanduser("~"),
        "bunny_render.png"
    )

    # Фон
    scene.world.color = (0.45, 0.48, 0.52)
    scene.view_settings.view_transform = 'AgX'
    scene.camera.data.dof.use_dof = False
    scene.render.film_transparent = False

    scene.world.use_nodes = True

    scene.world.node_tree.nodes["Background"].inputs[
        "Color"
    ].default_value = (0.32, 0.36, 0.42, 1)

    scene.world.node_tree.nodes["Background"].inputs[
        "Strength"
    ].default_value = 0.35


    # Выполнение рендера
    bpy.ops.render.render(write_still=True)

    print("Готово! Рендер сохранён:", scene.render.filepath)
    print(
        "Количество объектов в сцене:",
        len(bpy.context.scene.objects)
    )


clear_scene()
make_scene()