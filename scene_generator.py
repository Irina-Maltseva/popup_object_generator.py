import bpy

from utils.files import load_blend_from_art, append_material, load_font

def new_scene():
    load_blend_from_art('common/startup_file/startup_file_python.blend')
    append_material('common/shaders/shaders.blend', 'brown')
    append_material('common/shaders/shaders.blend', 'cream')
    append_material('common/shaders/shaders.blend', 'grey')
    append_material('common/shaders/shaders.blend', 'yellow_glass')
    append_material('common/shaders/shaders.blend', 'white_glass')
    append_material('common/shaders/shaders.blend', 'transparent_glass')
    print('Materials loaded.', len(bpy.data.materials))


    load_font('common/startup_file/Montserrat/Montserrat-Black.ttf')
    load_font('common/startup_file/Montserrat/Montserrat-Regular.ttf')
    load_font('common/startup_file/Montserrat/Montserrat-Light.ttf')



    return bpy.context.scene
