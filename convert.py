import os
from PIL import Image
import zipfile

def convert_png_to_jpg(folder_path):
    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    for png_file in png_files:
        # Full path of the PNG file
        png_path = os.path.join(folder_path, png_file)
        # Full path of the JPG file
        jpg_path = os.path.join(folder_path, png_file.replace('.png', '.jpg'))
        
        # Open the PNG image and convert it to JPG
        img = Image.open(png_path)
        img.convert('RGB').save(jpg_path, 'JPEG')
        
        # Print conversion message
        print(f"Converted {png_file} to {os.path.basename(jpg_path)}")
        
        # Delete the original PNG file
        os.remove(png_path)
        print(f"Deleted {png_file}")

def add_jpgs_to_zip(folder_path, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        # Get all JPG files in the folder
        jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
        
        for jpg_file in jpg_files:
            # Full path of the JPG file
            jpg_path = os.path.join(folder_path, jpg_file)
            # Add the JPG file to the ZIP archive
            zipf.write(jpg_path, jpg_file)
            
            # Print zip addition message
            print(f"Added {jpg_file} to {zip_file_name}")
        
    print("Completed.")