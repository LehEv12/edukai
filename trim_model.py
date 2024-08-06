import subprocess
import os

def trim_model(centered_path):
    if os.path.exists(centered_path):
        # Path to Blender executable
        blender_executable = "C:\\Program Files\\Blender Foundation\\Blender 4.1\\blender.exe"  # Update this path

        # Blender script to center the largest object, scale it, and save the file
        blender_script = f"""
import bpy
import os
import bmesh
import math

# Load the specified Blender file
bpy.ops.wm.open_mainfile(filepath=r"{centered_path}")

# Get the selected object
selected_obj = bpy.context.object

# Ensure we have an object selected
if selected_obj:
    # Set the Z location to 0
    selected_obj.location.z = 0.0


# Define the size of the region around the origin (adjust as needed)
region_size = 4  # This will create a region of +/- 4 units around the origin

# Calculate region boundaries
region_min = (-region_size, -region_size, -region_size)
region_max = (region_size, region_size, region_size)

# Delete vertices outside the specified region
def delete_vertices_outside_region(region_min, region_max):
    # Iterate through all mesh objects in the scene
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            # Ensure the object is in edit mode to modify mesh data
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            
            # Get the mesh data
            mesh = bmesh.from_edit_mesh(obj.data)
            
            # List to store vertices that need to be removed
            vertices_to_remove = []
            
            # Iterate through vertices and mark those outside the region for removal
            for vert in mesh.verts:
                vert_co = obj.matrix_world @ vert.co  # Global coordinates of the vertex
                
                # Check if the vertex is outside the defined region
                if not (region_min[0] <= vert_co.x <= region_max[0] and
                        region_min[1] <= vert_co.y <= region_max[1] and
                        region_min[2] <= vert_co.z <= region_max[2]):
                    vertices_to_remove.append(vert)
            
            # Remove vertices that are outside the region
            for vert in vertices_to_remove:
                mesh.verts.remove(vert)
            
            # Update and free the mesh
            bmesh.update_edit_mesh(obj.data)
            bpy.ops.object.mode_set(mode='OBJECT')

# Call the function to delete vertices outside the specified region
delete_vertices_outside_region(region_min, region_max)

# Save the modified Blender file as centered_model.blend
save_path = os.path.join(os.path.dirname(r"{centered_path}"), "trimmed_model.blend")
bpy.ops.wm.save_as_mainfile(filepath=save_path)
"""

        # Save the Blender script to a temporary file
        blender_trim_script_path = "./trim_model.py"
        with open(blender_trim_script_path, 'w') as script_file:
            script_file.write(blender_script)

        # Call Blender with the script
        try:
            subprocess.run([blender_executable, "--background", "--python", blender_trim_script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Blender script execution failed: {e}")
            return

        # Remove the temporary Blender script
        os.remove(blender_trim_script_path)

        print(f"Blender file trimmed and saved as trimmed_model.blend")

    else:
        print(f"Blender file not found: {centered_path}")