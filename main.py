import osm_query as query
import osm_client as osm
import bb_query as bb
import bb_results as boundary
import selenium_monument_screenshots as sel
import convert as CV
import HFendpoint as HF
import blender_import as blender
import center_model as center
import trim_model as trim

monument = "Colosseum"

folder_path = f'C:\\Users\\evanl\\OneDrive\\Desktop\\Edukai\\edukai'
zip_file_name = '3Dmodel.zip'
glb_file_path = f"C:\\Users\\evanl\\OneDrive\\Desktop\\Edukai\\edukai\\model.glb"
blender_file_path = f"C:\\Users\\evanl\\OneDrive\\Desktop\\Edukai\\edukai\\Blender Model\\imported_model.blend"
centered_path = f"C:\\Users\\evanl\\OneDrive\\Desktop\\Edukai\\edukai\\Blender Model\\centered_model.blend"

# Take queries from file
query1, query2, query3, query4 = query.osm_query(monument)

# Long and Lat, ID from OSM; input queries
latitude, longitude, monument_id, message = osm.query_monument(monument, query1, query2, query3, query4)

# Bounding box query for OSM
geo_query = bb.bb_query(monument_id)

# Results from bounding box query
min_lat, min_lon, max_lat, max_lon, width, height = boundary.get_bounding_box(geo_query)

# Enter camera settings
altitude = 35
heading = 255
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