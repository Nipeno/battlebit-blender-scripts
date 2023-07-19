import bpy

def delete_objects_with_prefix(prefix):
    # Get a list of all objects in the scene
    all_objects = bpy.context.scene.objects

    # Loop through each object
    for obj in all_objects:
        # Check if the object's name starts with the specified prefix
        if obj.name.startswith(prefix):
            # Check if the object is an empty
            if obj.type == 'EMPTY':
                # Select the empty
                obj.select_set(True)

                # Check if the empty has any children (underlying objects)
                if obj.children:
                    # Loop through the children and select them
                    for child in obj.children:
                        child.select_set(True)

    # Delete all selected objects (empties and their underlying objects)
    bpy.ops.object.delete()

# Call the function to delete objects with the prefix "Colliders."
delete_objects_with_prefix("Colliders.")

# Call the function to delete objects with the prefix "KillZone."
delete_objects_with_prefix("KillZone.")
