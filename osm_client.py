import requests

def query_monument(monument, query1, query2, query3, query4):
    # Function to replace ' with ’ in the monument name
    def replace_apostrophe(monument):
        return monument.replace("'", "’")

    # URL you are posting to
    url = "https://overpass-api.de/api/interpreter"

    # Send query to OSM
    def send_query(query):
        print("Sending query...")
        data = {'data': query}
        response = requests.post(url, data=data)
        print("Status code:", response.status_code)
        
        if response.status_code == 200:
            try:
                json_response = response.json()
                with open(f'{monument}.json', 'w', encoding='utf-8') as f:
                    f.write(response.text)
                                
                return json_response
            except requests.exceptions.JSONDecodeError as e:
                print("Failed to decode JSON response:", e)
                return None
        else:
            print("Error occurred:", response.status_code)
            return None

    # Function to extract coordinates from response
    def extract_coordinates(json_response):
        if json_response and 'elements' in json_response and json_response['elements']:
            for element in json_response['elements']:
                if element['type'] == 'relation' and 'center' in element:
                    coordinates = element['center']
                    return coordinates.get('lat'), coordinates.get('lon'), element.get('id')
            
            for element in json_response['elements']:
                if element['type'] == 'way' and 'center' in element:
                    coordinates = element['center']
                    return coordinates.get('lat'), coordinates.get('lon'), element.get('id')
            
            for element in json_response['elements']:
                if element['type'] == 'node' and 'lat' in element and 'lon' in element:
                    return element['lat'], element['lon'], element.get('id')
        return None, None, None

    # Try the first query
    print("Trying first query...")
    json_response = send_query(query1)
    
    # Extract coordinates from the first query response
    latitude, longitude, monument_id = extract_coordinates(json_response)

    # If the first query did not succeed, try the second query
    if not longitude or not latitude:
        print("First query failed, trying second query...")
        json_response = send_query(query2)
        latitude, longitude, monument_id = extract_coordinates(json_response)

    # If the second query did not succeed, try the third query
    if not longitude or not latitude:
        print("Second query failed, trying third query...")
        json_response = send_query(query3)
        latitude, longitude, monument_id = extract_coordinates(json_response)

    # If the third query did not succeed, try the fourth query
    if not longitude or not latitude:
        print("Third query failed, trying fourth query...")
        json_response = send_query(query4)
        latitude, longitude, monument_id = extract_coordinates(json_response)
    
    # Retry with replaced apostrophe if all queries fail and there is an apostrophe in the monument name
    if not longitude or not latitude:
        if "'" in monument:
            print("Queries failed due to an apostrophe, retrying with replaced apostrophe...")
            modified_monument = replace_apostrophe(monument)
            
            # Retry with modified monument name
            query1_modified = query1.replace(monument, modified_monument)
            query2_modified = query2.replace(monument, modified_monument)
            query3_modified = query3.replace(monument, modified_monument)
            query4_modified = query4.replace(monument, modified_monument)
            
            json_response = send_query(query1_modified)
            latitude, longitude, monument_id = extract_coordinates(json_response)
            
            if not longitude or not latitude:
                print("First query failed, trying second query...")
                json_response = send_query(query2_modified)
                latitude, longitude, monument_id = extract_coordinates(json_response)

            if not longitude or not latitude:
                print("First query failed, trying second query...")
                json_response = send_query(query3_modified)
                latitude, longitude, monument_id = extract_coordinates(json_response)

            if not longitude or not latitude:
                print("First query failed, trying second query...")
                json_response = send_query(query4_modified)
                latitude, longitude, monument_id = extract_coordinates(json_response)
        
    if longitude and latitude:
        message = f"{monument} found! ID: {monument_id}, Latitude: {latitude}, Longitude: {longitude}"
    else:
        message = f"{monument} not found. Try another monument or structure."
    
    print(message)
    return latitude, longitude, monument_id, message