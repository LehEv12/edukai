import subprocess
import os

def centered_model(blend_file_path):
    # Ensure the Blender file exists
    if os.path.exists(blend_file_path):
        # Path to Blender executable
        blender_executable = "C:\\Program Files\\Blender Foundation\\Blender 4.1\\blender.exe"  # Update this path

        # Blender script to center the largest object, scale it, and save the file
        blender_script = f"""
import bpy
import os
import mathutils

# Load the specified Blender file
bpy.ops.wm.open_mainfile(filepath=r"{blend_file_path}")

# Deselect all objects first
bpy.ops.object.select_all(action='DESELECT')

# Get all visible objects in the current view layer
visible_objects = bpy.context.visible_objects

# Find the object with the largest bounding box volume
largest_object = None
max_volume = 0.0

for obj in visible_objects:
    # Calculate bounding box volume (approximation using dimensions)
    bounding_volume = obj.dimensions.x * obj.dimensions.y * obj.dimensions.z
    
    # Check if current object has larger volume
    if bounding_volume > max_volume:
        max_volume = bounding_volume
        largest_object = obj

# Select only the largest object
if largest_object:
    bpy.context.view_layer.objects.active = largest_object
    largest_object.select_set(True)
    bpy.ops.object.select_all(action='DESELECT')
    largest_object.select_set(True)

    # Delete all other objects except the largest one
    objects_to_delete = [obj for obj in visible_objects if obj != largest_object]
    for obj in objects_to_delete:
        bpy.data.objects.remove(obj, do_unlink=True)

    # Move the largest object to the origin
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    bpy.ops.object.location_clear(clear_delta=False)
    
    # Scale the largest object by 25 times
    largest_object.scale = (25, 25, 25)

# Function to get the visual center of the object
def get_visual_center(obj):
    # Get the evaluated object to consider modifiers
    depsgraph = bpy.context.evaluated_depsgraph_get()
    evaluated_object = obj.evaluated_get(depsgraph)
    
    # Get the mesh data
    mesh = evaluated_object.data
    
    # Calculate the visual center based on the vertices
    vertices = [evaluated_object.matrix_world @ v.co for v in mesh.vertices]
    if vertices:
        bbox_center = sum(vertices, mathutils.Vector()) / len(vertices)
    else:
        bbox_center = mathutils.Vector()
    
    return bbox_center

# Clear selection
bpy.ops.object.select_all(action='DESELECT')

# Get the active object (selected object in 3D Viewport)
selected_obj = bpy.context.active_object

# Check if there is a selected object
if selected_obj:
    # Select the object
    selected_obj.select_set(True)
    bpy.context.view_layer.objects.active = selected_obj
    
    # Get the visual center of the object
    visual_center = get_visual_center(selected_obj)
    
    # Calculate the offset to move the object to the scene's origin
    offset = mathutils.Vector((0, 0, 0)) - visual_center
    
    # Move the object to center its solid display in the viewport
    selected_obj.location += offset
    
    print("Object centered in the viewport based on its visual display.")

# Iterate through all selected objects in the current view layer
for obj in bpy.context.selected_objects:
    # Set the object as the active object
    bpy.context.view_layer.objects.active = obj
    
    # Set the rotation mode to Euler
    obj.rotation_mode = 'XYZ'  # Set to whatever Euler rotation mode is desired
    
    # Set the desired rotation
    obj.rotation_euler = (-0.5348469, -3.1277516, -0.008628798)

# Save the modified Blender file as centered_model.blend
save_path = os.path.join(os.path.dirname(r"{blend_file_path}"), "centered_model.blend")
bpy.ops.wm.save_as_mainfile(filepath=save_path)
"""

        # Save the Blender script to a temporary file
        blender_script_path = "./centered_model.py"
        with open(blender_script_path, 'w') as script_file:
            script_file.write(blender_script)

        # Call Blender with the script
        try:
            subprocess.run([blender_executable, "--background", "--python", blender_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Blender script execution failed: {e}")
            return

        # Remove the temporary Blender script
        os.remove(blender_script_path)

        print(f"Blender file edited, scaled, and saved as centered_model.blend")

    else:
        print(f"Blender file not found: {blend_file_path}")