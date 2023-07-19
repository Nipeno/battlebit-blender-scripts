import bpy

def delete_objects_with_prefix(prefix):
    # Get a list of all objects in the scene
    all_objects = bpy.context.scene.objects

    # Loop through each object
    for obj in all_objects:
        # Check if the object's name starts with the specified prefix
        if obj.name.startswith(prefix):
            # Select the object
            obj.select_set(True)

    # Delete all selected objects
    bpy.ops.object.delete()

# Call the function to delete objects with the prefix "Model_1."
delete_objects_with_prefix("Model_1.")