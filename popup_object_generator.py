import bpy
from mathutils import Euler
from utils.files import append_collection, load_image
from utils.fonts import default_font
from utils.materials import cream, yellow_glass
from utils.geometry import cuboid_mesh, plane_mesh

DEFAULT_FONT_NAME = 'Montserrat-Regular'

def label(text = 'Example', location = (0, -2, 0)):

    # Create text
    font_curve_data = bpy.data.curves.new(type='FONT',name='font_curve')
    font_curve_object = bpy.data.objects.new('font_curve', font_curve_data)
    font_curve_data.body = text
    font_curve_data.size = 0.4
    font_curve_data.font = default_font()
    font_curve_data.align_x = 'CENTER'
    font_curve_data.align_y = 'CENTER'
    font_curve_object.location = (location[0], location[1] - 0.155, location[2])
    font_curve_object.rotation_euler = Euler((1.5708, 0, 0), 'XYZ')
    font_curve_object.data.materials.append(cream())
    [text_size_x, text_size_y, text_size_z] = font_curve_object.dimensions

    padding = 0.4

    # mesh = cuboid_mesh(location = location, size_x = text_size_x + padding*2, size_z = text_size_y + padding*2)
    # cube_object = bpy.data.objects.new('label', mesh)
    # cube_object.data.materials.append(yellow_glass())

    mesh = plane_mesh(location = location, size_x = text_size_x + padding*2, size_z = text_size_y + padding*1)
    plane_object = bpy.data.objects.new('plane', mesh)

    print('bpy.data.materials 1', len(bpy.data.materials))

    image_material = bpy.data.materials.new('material_with_image')
    image_material.use_nodes = True
    material_nodes = image_material.node_tree.nodes
    material_links = image_material.node_tree.links
    principled_bsdf_node = material_nodes['Principled BSDF']
    material_output_node = material_nodes['Material Output']
    tex_image_node = material_nodes.new(type = 'ShaderNodeTexImage')
    material_links.new(tex_image_node.outputs['Color'], principled_bsdf_node.inputs['Emission'])

    print('bpy.data.materials 2', len(bpy.data.materials))

    #image = load_image('004/image')
    #tex_image_node.image = image
    
    image = load_image('./004/image.png')
    tex_image_node.image = image
    print('bpy.data.materials 3', len(bpy.data.materials))



    #bpy.ops.object.modifier_add(type='BEVEL')
    #cube_object.modifiers["Bevel"].offset_type = 'PERCENT'
    #cube_object.modifiers["Bevel"].segments = 5
    #ube_object.modifiers["Bevel"].width_pct = 3



    font_curve_object.parent = plane_object

    return [font_curve_object, plane_object]


def demo_popup_object():
    append_collection('common/demo_popup_object/demo_popup_object.blend', 'demo_popup_object')
    return bpy.data.collections['demo_popup_object']
