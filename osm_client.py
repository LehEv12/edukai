import requests


def query_monument(monument):
    # URL you are posting to
    url = "https://overpass-api.de/api/interpreter"

    # Initial query to be sent to the API
    query1 = f"""
    [out:json];

    // Define the search area as Rome
    area["name"="Italia"]->.searchArea;

    // Search for the Colosseum by its name in English as a monument and an archaeological site
    (
    node(area.searchArea)["historic"="monument"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="monument"]["name:en"="{monument}"];
    relation(area.searchArea)["historic"="monument"]["name:en"="{monument}"];

    node(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];
    relation(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];

    node(area.searchArea)["historic"="monument"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="monument"]["name:it"="{monument}"];
    relation(area.searchArea)["historic"="monument"]["name:it"="{monument}"];

    node(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];
    relation(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];
    );

    out center;
    """

    # Fallback query to be sent to the API; if certain structures or monuments are not labeled as historic monuments of sites in OSM, search for it as a tourist attraction
    query2 = f"""
    [out:json];

    // Define the search area as Rome
    area["name"="Roma"]->.searchArea;

    // Search for the monument by its name as a tourist attraction
    (
    node(area.searchArea)["tourism"]["name:en"="{monument}"];
    way(area.searchArea)["tourism"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"]["name:en"="{monument}"];

    node(area.searchArea)["tourism"]["name:it"="{monument}"];
    way(area.searchArea)["tourism"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"]["name:it"="{monument}"];
    );
    (._;>;);
    out center;
    """

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
                print(f"JSON response saved successfully as {monument}.json")
                
                return json_response
            except requests.exceptions.JSONDecodeError as e:
                print("Failed to decode JSON response:", e)
                return None
        else:
            print("Error occurred:", response.status_code)
            return None

    # Try the first query
    print("Trying first query...")
    json_response = send_query(query1)
    
    # Initialize variables to store coordinates and id
    longitude = None
    latitude = None
    monument_id = None

    # Check if the first query succeeded in getting coordinates
    if json_response and 'elements' in json_response and json_response['elements']:
        for element in json_response['elements']:
            monument_id = element.get('id')
            if 'center' in element:
                coordinates = element['center']
                longitude = coordinates.get('lon')
                latitude = coordinates.get('lat')
                break
    
    # If the first query did not succeed, try the second query
    if not longitude or not latitude:
        print("First query failed, trying second query...")
        json_response = send_query(query2)
        if json_response and 'elements' in json_response:
            for element in json_response['elements']:
                if element['type'] == 'node' and 'lat' in element and 'lon' in element:
                    latitude = element['lat']
                    longitude = element['lon']
                    monument_id = element.get('id')
                    break
    
    if longitude and latitude:
        message = f"{monument} found! ID: {monument_id}, Latitude: {latitude}, Longitude: {longitude}"
    else:
        message = f"{monument} not found. Try another monument or structure."
    
    print(message)
    return latitude, longitude, monument_id, message