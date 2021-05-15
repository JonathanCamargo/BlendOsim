bl_info = {
    "name": "Osim",
    "category": "Import",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
}

import bpy
import osim
from osim.model import addModel
from osim.common import readNames,loadAnimation
from osim.markers import loadMarkers
from osim.forces import loadForces
import numpy as np

import os

rootpath=os.path.dirname(os.path.abspath(__file__))
stlFolder=os.path.join(rootpath,'osim','resources')



class MyProperties(bpy.types.PropertyGroup):
    markersfile : bpy.props.StringProperty(
        name='Markers file',
        subtype="FILE_PATH")
    
    forcesfile : bpy.props.StringProperty(
        name='Forces file',
        subtype="FILE_PATH")            
    modelfile : bpy.props.StringProperty(
        name='Model file',
        subtype="FILE_PATH")

    motionfile : bpy.props.StringProperty(
        name='Motion file',
        subtype="FILE_PATH")


    



class addCubeSample(bpy.types.Operator):
    bl_idname = 'mesh.add_cube_sample'
    bl_label = 'Add Cube'
    bl_options = {'REGISTER', 'UNDO'}
      
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}
    
class addModel(bpy.types.Operator):
    bl_idname = 'mesh.add_osim_model'
    bl_label = 'Add Model'
    bl_options = {'REGISTER', 'UNDO'}
      
    def execute(self, context):
        scene=context.scene
        mytool=scene.my_tool          
        osim.model.addModel(mytool.modelfile,stlRoot=stlFolder)
        return {'FINISHED'}
    
class addMotion(bpy.types.Operator):
    bl_idname = 'motion.add_osim_motion'
    bl_label = 'Add Motion'
    bl_options = {'REGISTER', 'UNDO'}
      
    def execute(self, context):
        scene=context.scene
        mytool=scene.my_tool  
        csvFile=mytool.motionfile
        data = np.genfromtxt(csvFile, dtype=float, delimiter=',', names=True,skip_header=0) 
        objectNames=readNames(data.dtype.names[1:])          
        collection=bpy.data.collections['osimModel']        
        osim.model.loadAnimation(collection,data,objectNames)
        #bpy.context.scene.update()
        return {'FINISHED'}
    
class addMarkers(bpy.types.Operator):
    bl_idname = 'mesh.add_osim_markers'
    bl_label = 'Add Markers'
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene=context.scene
        mytool=scene.my_tool  
        csvFile=mytool.markersfile
        osim.markers.loadMarkers(csvFile)
        #bpy.context.scene.update()        
        return {'FINISHED'}

class addForces(bpy.types.Operator):
    bl_idname = 'mesh.add_osim_forces'
    bl_label = 'Add Forces'
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        scene=context.scene
        mytool=scene.my_tool  
        csvFile=mytool.forcesfile
        osim.forces.loadForces(csvFile)
        #bpy.context.scene.update()        
        return {'FINISHED'}


class panel1(bpy.types.Panel):
    bl_idname = "panel.panel1"
    bl_label = "BlendOsim"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlendOsim"

    
    
    def draw(self, context):
        layout=self.layout
        layout.label(text='Add data from opensim') 
        scene=context.scene
        mytool=scene.my_tool  
        layout.prop(mytool,"modelfile")
        layout.operator("mesh.add_osim_model",icon='MESH_MONKEY', text="Add Model")      
        layout.prop(mytool,"motionfile")   
        layout.operator("motion.add_osim_motion",icon='CURVE_PATH', text="Add Motion")     
        layout.prop(mytool,"markersfile")            
        layout.operator("mesh.add_osim_markers",icon='MESH_UVSPHERE', text="Add Markers") 
        layout.prop(mytool,"forcesfile")            
        layout.operator("mesh.add_osim_forces",icon='EMPTY_SINGLE_ARROW', text="Add Forces") 
        
def register():
    print('Addon Registered')
    bpy.utils.register_class(addCubeSample)
    bpy.utils.register_class(addModel)
    bpy.utils.register_class(addMotion)            
    bpy.utils.register_class(addMarkers)
    bpy.utils.register_class(addForces)
    bpy.utils.register_class(panel1)
    bpy.utils.register_class(MyProperties)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=MyProperties)

def unregister():
    print('chao')
    bpy.utils.unregister_class(addCubeSample)
    bpy.utils.unregister_class(addModel)
    bpy.utils.unregister_class(addMotion)            
    bpy.utils.unregister_class(addMarkers)
    bpy.utils.unregister_class(addForces)
    bpy.utils.unregister_class(panel1)
    bpy.utils.unregister_class(MyProperties)

        
# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()
    print('test done')
    
    