import bpy

def delete_zero_vertex_meshes():
    # Get a list of all mesh objects in the scene
    mesh_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'MESH' and len(obj.data.vertices) == 0]

    # Delete all selected objects (meshes with zero vertices)
    bpy.ops.object.delete({"selected_objects": mesh_objects})
    print("Deleted zero vertex meshes.")

def delete_objects_with_prefix(prefix):
    # Get a list of all objects in the scene with the specified prefix
    objects_to_delete = [obj for obj in bpy.context.scene.objects if obj.name.startswith(prefix)]

    # Delete all selected objects
    bpy.ops.object.delete({"selected_objects": objects_to_delete})
    print("Deleted objects with prefix:", prefix)

def delete_non_lod1_objects():
    # Create a set to store base names of LOD objects
    lod_base_names = set()

    # Get a list of all objects in the scene
    all_objects = bpy.context.scene.objects

    # Collect LOD base names from objects
    for obj in all_objects:
        if "_LOD" in obj.name:
            base_name = obj.name.split("_LOD")[0]
            lod_base_names.add(base_name)

    # Loop through the LOD base names and keep only LOD1 objects or the first object if no LOD1 is present
    for base_name in lod_base_names:
        lod_objects = [obj for obj in all_objects if obj.name.startswith(base_name + "_LOD")]
        lod1_object = next((obj for obj in lod_objects if "_LOD1" in obj.name), None)

        for obj in lod_objects:
            if obj != lod1_object:
                obj.select_set(True)

    # Delete all selected objects that don't contain "_LOD1" in their name
    bpy.ops.object.delete()
    print("Deleted non-LOD1 objects.")

def delete_empty_objects_with_prefix(prefix):
    # Get a list of all empty objects in the scene with the specified prefix
    empty_objects = [obj for obj in bpy.context.scene.objects if obj.type == 'EMPTY' and obj.name.startswith(prefix)]

    # Loop through each empty object and delete its children
    for empty_obj in empty_objects:
        for child in empty_obj.children:
            child.select_set(True)

    # Delete all selected child objects (sub-objects of the empties)
    bpy.ops.object.delete()

    # Now, delete the empty objects themselves
    for empty_obj in empty_objects:
        empty_obj.select_set(True)

    # Delete all selected empty objects
    bpy.ops.object.delete()
    print("Deleted empty objects with prefix:", prefix)

def delete_empty_empties():
    all_objects = bpy.context.scene.objects

    for obj in all_objects:
        if obj.type == 'EMPTY' and not obj.children:
            print('Removing ' + obj.name)
            bpy.data.objects.remove(obj, do_unlink=True)

# Call the functions to delete objects based on their properties
delete_zero_vertex_meshes()
delete_empty_objects_with_prefix("Colliders.")
delete_empty_objects_with_prefix("KillZone.")
delete_empty_objects_with_prefix("PHYS.")
delete_non_lod1_objects()
delete_objects_with_prefix("Model_1")
delete_empty_empties()