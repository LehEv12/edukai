import subprocess
import os
import shutil

def import_glb_to_blender(glb_file_path):
    # Ensure the GLB file exists
    if os.path.exists(glb_file_path):
        # Path to Blender executable
        blender_executable = "C:\\Program Files\\Blender Foundation\\Blender 4.1\\blender.exe"  # Update this path

        # Blender script to import the GLB file and save as Blender file
        blender_script = f"""
import bpy

# Delete default scene objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Import GLB file (escape backslashes in file path)
bpy.ops.import_scene.gltf(filepath="{glb_file_path.replace('\\', '\\\\')}")

# Save as Blender file
bpy.ops.wm.save_as_mainfile(filepath="./imported_model.blend")
"""

        # Save the Blender script to a temporary file
        blender_script_path = "./import_glb_to_blender.py"
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

        # Move the saved Blender file to a specific location if desired
        saved_blend_file_path = "./imported_model.blend"
        destination_path = "C:\\Users\\evanl\\Blender\\imported_model.blend"  # Update this path
        if os.path.exists(saved_blend_file_path):
            shutil.move(saved_blend_file_path, destination_path)
            print(f"Blender file saved to: {destination_path}")
        else:
            print(f"Blender file not found: {saved_blend_file_path}")

    else:
        print(f"GLB file not found: {glb_file_path}")