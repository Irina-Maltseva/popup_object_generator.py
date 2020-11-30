# DEPRECATED! All materials are loaded with scenes now (see scene_generator)

import bpy

def glass():
    # 1. Создание материала
    material = bpy.data.materials.new(name='glass')
    #material.diffuse_color = (0, 0, 1, 1)
    # TODO add refraction

    # 2. Подготовка/настройка материала
    mod.nodes["Principled BSDF"].inputs[4].default_value = 0.7

    # 3. Возвращаем материал
    return material
