import bpy

def delete_non_lod1_objects():
    # Create a dictionary to store objects with their LOD suffixes
    lod_objects = {}

    # Get a list of all objects in the scene
    all_objects = bpy.context.scene.objects

    # Loop through each object
    for obj in all_objects:
        # Get the base name of the object without the LOD suffix
        base_name = obj.name.split("_LOD")[0]

        # Check if the object's name contains "_LOD1", "_LOD2", or "_LOD3"
        if "_LOD" in obj.name:
            # Store the object in the dictionary under its base name
            lod_objects.setdefault(base_name, []).append(obj)

    # Loop through the dictionary entries
    for base_name, objects in lod_objects.items():
        # Check if there is an LOD1 object for the current base name
        if any("_LOD1" in obj.name for obj in objects):
            # Loop through the objects and delete those that don't contain "_LOD1" in their name
            for obj in objects:
                if "_LOD1" not in obj.name:
                    obj.select_set(True)
        else:
            # If there is no LOD1 object, keep all objects except for the first one (remove duplicates)
            for obj in objects[1:]:
                obj.select_set(True)

    # Delete all selected objects that don't contain "_LOD1" in their name
    bpy.ops.object.delete()

# Call the function to delete non-LOD1 objects
delete_non_lod1_objects()
