import selenium_monument_screenshots as sel
import convert as CV
import HFendpoint as HF
import osm_client as osm
import blender_import as blender
import center_model as center
import trim_model as trim

monument = "Colosseum"
folder_path = '.'
zip_file_name = '3Dmodel.zip'
glb_file_path = f"C:\\Users\\evanl\\model.glb"
blender_file_path = f"C:\\Users\\evanl\\Blender\\imported_model.blend"
centered_path = f"C:\\Users\\evanl\\Blender\\centered_model.blend"

# Long and Lat from OSM
latitude, longitude, monument_id, message = osm.query_monument(monument)

# Enter camera settings
altitude = 30.5
heading = 250.5
pitch = 35
tilt = 60
roll = 0

sel.take_pictures(latitude, longitude, altitude, heading, pitch, tilt, roll)

CV.convert_png_to_jpg(folder_path)
CV.add_jpgs_to_zip(folder_path, zip_file_name)

HF.send_request(zip_file_name)

blender.import_glb_to_blender(glb_file_path)

center.centered_model(blender_file_path)

trim.trim_model(centered_path)