bl_info = {
    "name": "Lock camera to view shortcut",
    "author": "Stephan Nijman",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "View3D",
    "description": "Lock camera to view shortcut",
    "category": "Camera",
}

import bpy

# Keep track of added shortcut.
addon_keymaps = []

# ------------------------------------------------------------
# Operator: VIEW_3D_lock_camera_to_view
# -----------------------------------------------------------
class VIEW_3D_lock_camera_to_view(bpy.types.Operator):
    """Add shortcut to lock camera to view"""
    bl_idname = "view.lock_camera"
    bl_label = "Lock camera to view shortcut"
    bl_options = {'REGISTER'}

    def execute(self, context):
        if bpy.context.space_data.lock_camera:
            # Unlock camera from view,
            bpy.context.space_data.lock_camera = False
        else:
            # Move the view into the camera perspective.
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.spaces[0].region_3d.view_perspective = 'CAMERA'
                    break
            # Lock camera to view,
            bpy.context.space_data.lock_camera = True
        
        return {'FINISHED'}


# ------------------------------------------------------------
# Register class and keyboard shortcut
# -----------------------------------------------------------
def register():
    bpy.utils.register_class(VIEW_3D_lock_camera_to_view)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(VIEW_3D_lock_camera_to_view.bl_idname, type='E', value='PRESS', ctrl=True)
        addon_keymaps.append((km, kmi))


# ------------------------------------------------------------
# Unregister class and keyboard shortcut
# -----------------------------------------------------------
def unregister():
    bpy.utils.unregister_class(VIEW_3D_lock_camera_to_view)
    
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
