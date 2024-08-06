import requests

def get_bounding_box(geo_query):
    # Define the Overpass API endpoint
    overpass_url = "http://overpass-api.de/api/interpreter"

    # Send the query to the Overpass API
    response = requests.post(overpass_url, data={'data': geo_query})

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Initialize variables
        min_lat = min_lon = max_lat = max_lon = None
        latitude = longitude = None

        # Iterate over elements to find bounding box and center
        for element in data.get('elements', []):            
            # Process bounding box if available
            if 'bounds' in element:
                bounds = element['bounds']
                min_lat = bounds['minlat']
                min_lon = bounds['minlon']
                max_lat = bounds['maxlat']
                max_lon = bounds['maxlon']

        # If no bounding box was found, raise an error
        if min_lat is None or min_lon is None or max_lat is None or max_lon is None:
            print("No bounding box found in the response elements.")  # Debug: print no bounding box found in elements
            raise ValueError("Error: No bounding box found in the response.")

        # Calculate the width and height of the bounding box
        width = max_lon - min_lon
        height = max_lat - min_lat

        # Print the bounding box coordinates and dimensions
        print(f"Bounding Box Coordinates:\n"
              f"Min Latitude: {min_lat}\n"
              f"Min Longitude: {min_lon}\n"
              f"Max Latitude: {max_lat}\n"
              f"Max Longitude: {max_lon}\n"
              f"Width: {width}\n"
              f"Height: {height}\n")
        
        return min_lat, min_lon, max_lat, max_lon, width, height

    else:
        print(f"Error: Unable to fetch data. HTTP Status code: {response.status_code}")  # Debug: print error status code
        raise ConnectionError(f"Error: Unable to fetch data. HTTP Status code: {response.status_code}")