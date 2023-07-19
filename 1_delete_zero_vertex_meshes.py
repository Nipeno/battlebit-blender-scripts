import bpy

def delete_zero_vertex_meshes():
    # Get a list of all mesh objects in the scene
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH']

    # Loop through each mesh object
    for obj in mesh_objects:
        # Check if the object has zero vertices
        if len(obj.data.vertices) == 0:
            # Select the object
            obj.select_set(True)

    # Delete all selected objects (meshes with zero vertices)
    bpy.ops.object.delete()

# Call the function to delete zero vertex meshes
delete_zero_vertex_meshes()