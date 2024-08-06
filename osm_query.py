import requests

def osm_query(monument):
    # Initial query to be sent to the API
    query1 = f"""
    [out:json];

    // Define the search area as Italy
    area["name"="Italia"]->.searchArea;

    // Search for the monument/place by its name in English and Italian under historic tags
    (
    relation(area.searchArea)["historic"="monument"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="monument"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="monument"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="monument"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="monument"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="monument"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="monument"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="monument"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="monument"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="archaeological_site"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="archaeological_site"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="archaeological_site"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="archaeological_site"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="archaeological_site"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="castle"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="castle"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="castle"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="castle"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="castle"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="castle"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="castle"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="castle"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="castle"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="building"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="building"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="building"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="building"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="building"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="building"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="building"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="building"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="building"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="church"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="church"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="church"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="church"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="church"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="church"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="church"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="church"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="church"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="fort"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="fort"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="fort"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="fort"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="fort"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="fort"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="fort"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="fort"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="fort"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="house"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="house"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="house"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="house"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="house"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="house"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="house"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="house"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="house"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="aqueduct"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="aqueduct"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="aqueduct"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="aqueduct"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="aqueduct"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="aqueduct"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="aqueduct"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="aqueduct"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="aqueduct"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="battlefield"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="battlefield"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="battlefield"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="battlefield"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="battlefield"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="battlefield"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="battlefield"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="battlefield"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="battlefield"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="district"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="district"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="district"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="district"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="district"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="district"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="district"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="district"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="district"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="farm"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="farm"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="farm"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="farm"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="farm"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="farm"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="farm"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="farm"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="farm"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="manor"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="manor"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="manor"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="manor"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="manor"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="manor"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="manor"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="manor"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="manor"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="memorial"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="memorial"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="memorial"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="memorial"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="memorial"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="memorial"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="memorial"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="memorial"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="memorial"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="monastery"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="monastery"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="monastery"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="monastery"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="monastery"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="monastery"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="monastery"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="monastery"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="monastery"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="mosque"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="mosque"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="mosque"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="mosque"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="mosque"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="mosque"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="mosque"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="mosque"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="mosque"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="pillory"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="pillory"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="pillory"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="pillory"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="pillory"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="pillory"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="pillory"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="pillory"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="pillory"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="ruins"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="ruins"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="ruins"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="ruins"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="ruins"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="ruins"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="ruins"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="ruins"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="ruins"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="temple"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="temple"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="temple"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="temple"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="temple"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="temple"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="temple"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="temple"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="temple"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="tower"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="tower"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="tower"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="tower"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="tower"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="tower"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="tower"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="tower"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="tower"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="high_cross"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="high_cross"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="high_cross"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="high_cross"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="high_cross"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="high_cross"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="high_cross"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="high_cross"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="high_cross"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="stone"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="stone"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="stone"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="stone"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="stone"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="stone"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="stone"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="stone"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="stone"]["alt_name"="{monument}"];

    relation(area.searchArea)["historic"="yes"]["name:en"="{monument}"];
    way(area.searchArea)["historic"="yes"]["name:en"="{monument}"];
    node(area.searchArea)["historic"="yes"]["name:en"="{monument}"];

    relation(area.searchArea)["historic"="yes"]["name:it"="{monument}"];
    way(area.searchArea)["historic"="yes"]["name:it"="{monument}"];
    node(area.searchArea)["historic"="yes"]["name:it"="{monument}"];

    relation(area.searchArea)["historic"="yes"]["alt_name"="{monument}"];
    way(area.searchArea)["historic"="yes"]["alt_name"="{monument}"];
    node(area.searchArea)["historic"="yes"]["alt_name"="{monument}"];
    );
    (._;>;);
    out center;
    """

    #Fallback to first query; searches globally
    query2 = f"""
    [out:json];

    (
    way["historic"="monument"]["name:en"="{monument}"];
    relation["historic"="monument"]["name:en"="{monument}"];
    node["historic"="monument"]["name:en"="{monument}"];

    way["historic"="monument"]["name:it"="{monument}"];
    relation["historic"="monument"]["name:it"="{monument}"];
    node["historic"="monument"]["name:it"="{monument}"];

    way["historic"="monument"]["alt_name"="{monument}"];
    relation["historic"="monument"]["alt_name"="{monument}"];
    node["historic"="monument"]["alt_name"="{monument}"];

    way["historic"="archaeological_site"]["name:en"="{monument}"];
    relation["historic"="archaeological_site"]["name:en"="{monument}"];
    node["historic"="archaeological_site"]["name:en"="{monument}"];

    way["historic"="archaeological_site"]["name:it"="{monument}"];
    relation["historic"="archaeological_site"]["name:it"="{monument}"];
    node["historic"="archaeological_site"]["name:it"="{monument}"];

    way["historic"="archaeological_site"]["alt_name"="{monument}"];
    relation["historic"="archaeological_site"]["alt_name"="{monument}"];
    node["historic"="archaeological_site"]["alt_name"="{monument}"];

    way["historic"="castle"]["name:en"="{monument}"];
    relation["historic"="castle"]["name:en"="{monument}"];
    node["historic"="castle"]["name:en"="{monument}"];

    way["historic"="castle"]["name:it"="{monument}"];
    relation["historic"="castle"]["name:it"="{monument}"];
    node["historic"="castle"]["name:it"="{monument}"];

    way["historic"="castle"]["alt_name"="{monument}"];
    relation["historic"="castle"]["alt_name"="{monument}"];
    node["historic"="castle"]["alt_name"="{monument}"];

    way["historic"="building"]["name:en"="{monument}"];
    relation["historic"="building"]["name:en"="{monument}"];
    node["historic"="building"]["name:en"="{monument}"];

    way["historic"="building"]["name:it"="{monument}"];
    relation["historic"="building"]["name:it"="{monument}"];
    node["historic"="building"]["name:it"="{monument}"];

    way["historic"="building"]["alt_name"="{monument}"];
    relation["historic"="building"]["alt_name"="{monument}"];
    node["historic"="building"]["alt_name"="{monument}"];

    way["historic"="church"]["name:en"="{monument}"];
    relation["historic"="church"]["name:en"="{monument}"];
    node["historic"="church"]["name:en"="{monument}"];

    way["historic"="church"]["name:it"="{monument}"];
    relation["historic"="church"]["name:it"="{monument}"];
    node["historic"="church"]["name:it"="{monument}"];

    way["historic"="church"]["alt_name"="{monument}"];
    relation["historic"="church"]["alt_name"="{monument}"];
    node["historic"="church"]["alt_name"="{monument}"];

    way["historic"="fort"]["name:en"="{monument}"];
    relation["historic"="fort"]["name:en"="{monument}"];
    node["historic"="fort"]["name:en"="{monument}"];

    way["historic"="fort"]["name:it"="{monument}"];
    relation["historic"="fort"]["name:it"="{monument}"];
    node["historic"="fort"]["name:it"="{monument}"];

    way["historic"="fort"]["alt_name"="{monument}"];
    relation["historic"="fort"]["alt_name"="{monument}"];
    node["historic"="fort"]["alt_name"="{monument}"];

    way["historic"="house"]["name:en"="{monument}"];
    relation["historic"="house"]["name:en"="{monument}"];
    node["historic"="house"]["name:en"="{monument}"];

    way["historic"="house"]["name:it"="{monument}"];
    relation["historic"="house"]["name:it"="{monument}"];
    node["historic"="house"]["name:it"="{monument}"];

    way["historic"="house"]["alt_name"="{monument}"];
    relation["historic"="house"]["alt_name"="{monument}"];
    node["historic"="house"]["alt_name"="{monument}"];

    way["historic"="aqueduct"]["name:en"="{monument}"];
    relation["historic"="aqueduct"]["name:en"="{monument}"];
    node["historic"="aqueduct"]["name:en"="{monument}"];

    way["historic"="aqueduct"]["name:it"="{monument}"];
    relation["historic"="aqueduct"]["name:it"="{monument}"];
    node["historic"="aqueduct"]["name:it"="{monument}"];

    way["historic"="aqueduct"]["alt_name"="{monument}"];
    relation["historic"="aqueduct"]["alt_name"="{monument}"];
    node["historic"="aqueduct"]["alt_name"="{monument}"];

    way["historic"="battlefield"]["name:en"="{monument}"];
    relation["historic"="battlefield"]["name:en"="{monument}"];
    node["historic"="battlefield"]["name:en"="{monument}"];

    way["historic"="battlefield"]["name:it"="{monument}"];
    relation["historic"="battlefield"]["name:it"="{monument}"];
    node["historic"="battlefield"]["name:it"="{monument}"];

    way["historic"="battlefield"]["alt_name"="{monument}"];
    relation["historic"="battlefield"]["alt_name"="{monument}"];
    node["historic"="battlefield"]["alt_name"="{monument}"];

    way["historic"="district"]["name:en"="{monument}"];
    relation["historic"="district"]["name:en"="{monument}"];
    node["historic"="district"]["name:en"="{monument}"];

    way["historic"="district"]["name:it"="{monument}"];
    relation["historic"="district"]["name:it"="{monument}"];
    node["historic"="district"]["name:it"="{monument}"];

    way["historic"="district"]["alt_name"="{monument}"];
    relation["historic"="district"]["alt_name"="{monument}"];
    node["historic"="district"]["alt_name"="{monument}"];

    way["historic"="farm"]["name:en"="{monument}"];
    relation["historic"="farm"]["name:en"="{monument}"];
    node["historic"="farm"]["name:en"="{monument}"];

    way["historic"="farm"]["name:it"="{monument}"];
    relation["historic"="farm"]["name:it"="{monument}"];
    node["historic"="farm"]["name:it"="{monument}"];

    way["historic"="farm"]["alt_name"="{monument}"];
    relation["historic"="farm"]["alt_name"="{monument}"];
    node["historic"="farm"]["alt_name"="{monument}"];

    way["historic"="manor"]["name:en"="{monument}"];
    relation["historic"="manor"]["name:en"="{monument}"];
    node["historic"="manor"]["name:en"="{monument}"];

    way["historic"="manor"]["name:it"="{monument}"];
    relation["historic"="manor"]["name:it"="{monument}"];
    node["historic"="manor"]["name:it"="{monument}"];

    way["historic"="manor"]["alt_name"="{monument}"];
    relation["historic"="manor"]["alt_name"="{monument}"];
    node["historic"="manor"]["alt_name"="{monument}"];

    way["historic"="memorial"]["name:en"="{monument}"];
    relation["historic"="memorial"]["name:en"="{monument}"];
    node["historic"="memorial"]["name:en"="{monument}"];

    way["historic"="memorial"]["name:it"="{monument}"];
    relation["historic"="memorial"]["name:it"="{monument}"];
    node["historic"="memorial"]["name:it"="{monument}"];

    way["historic"="memorial"]["alt_name"="{monument}"];
    relation["historic"="memorial"]["alt_name"="{monument}"];
    node["historic"="memorial"]["alt_name"="{monument}"];

    way["historic"="monastery"]["name:en"="{monument}"];
    relation["historic"="monastery"]["name:en"="{monument}"];
    node["historic"="monastery"]["name:en"="{monument}"];

    way["historic"="monastery"]["name:it"="{monument}"];
    relation["historic"="monastery"]["name:it"="{monument}"];
    node["historic"="monastery"]["name:it"="{monument}"];

    way["historic"="monastery"]["alt_name"="{monument}"];
    relation["historic"="monastery"]["alt_name"="{monument}"];
    node["historic"="monastery"]["alt_name"="{monument}"];

    way["historic"="mosque"]["name:en"="{monument}"];
    relation["historic"="mosque"]["name:en"="{monument}"];
    node["historic"="mosque"]["name:en"="{monument}"];

    way["historic"="mosque"]["name:it"="{monument}"];
    relation["historic"="mosque"]["name:it"="{monument}"];
    node["historic"="mosque"]["name:it"="{monument}"];

    way["historic"="mosque"]["alt_name"="{monument}"];
    relation["historic"="mosque"]["alt_name"="{monument}"];
    node["historic"="mosque"]["alt_name"="{monument}"];

    way["historic"="pillory"]["name:en"="{monument}"];
    relation["historic"="pillory"]["name:en"="{monument}"];
    node["historic"="pillory"]["name:en"="{monument}"];

    way["historic"="pillory"]["name:it"="{monument}"];
    relation["historic"="pillory"]["name:it"="{monument}"];
    node["historic"="pillory"]["name:it"="{monument}"];

    way["historic"="pillory"]["alt_name"="{monument}"];
    relation["historic"="pillory"]["alt_name"="{monument}"];
    node["historic"="pillory"]["alt_name"="{monument}"];

    way["historic"="ruins"]["name:en"="{monument}"];
    relation["historic"="ruins"]["name:en"="{monument}"];
    node["historic"="ruins"]["name:en"="{monument}"];

    way["historic"="ruins"]["name:it"="{monument}"];
    relation["historic"="ruins"]["name:it"="{monument}"];
    node["historic"="ruins"]["name:it"="{monument}"];

    way["historic"="ruins"]["alt_name"="{monument}"];
    relation["historic"="ruins"]["alt_name"="{monument}"];
    node["historic"="ruins"]["alt_name"="{monument}"];

    way["historic"="temple"]["name:en"="{monument}"];
    relation["historic"="temple"]["name:en"="{monument}"];
    node["historic"="temple"]["name:en"="{monument}"];

    way["historic"="temple"]["name:it"="{monument}"];
    relation["historic"="temple"]["name:it"="{monument}"];
    node["historic"="temple"]["name:it"="{monument}"];

    way["historic"="temple"]["alt_name"="{monument}"];
    relation["historic"="temple"]["alt_name"="{monument}"];
    node["historic"="temple"]["alt_name"="{monument}"];

    way["historic"="tower"]["name:en"="{monument}"];
    relation["historic"="tower"]["name:en"="{monument}"];
    node["historic"="tower"]["name:en"="{monument}"];

    way["historic"="tower"]["name:it"="{monument}"];
    relation["historic"="tower"]["name:it"="{monument}"];
    node["historic"="tower"]["name:it"="{monument}"];

    way["historic"="tower"]["alt_name"="{monument}"];
    relation["historic"="tower"]["alt_name"="{monument}"];
    node["historic"="tower"]["alt_name"="{monument}"];

    way["historic"="high_cross"]["name:en"="{monument}"];
    relation["historic"="high_cross"]["name:en"="{monument}"];
    node["historic"="high_cross"]["name:en"="{monument}"];

    way["historic"="high_cross"]["name:it"="{monument}"];
    relation["historic"="high_cross"]["name:it"="{monument}"];
    node["historic"="high_cross"]["name:it"="{monument}"];

    way["historic"="high_cross"]["alt_name"="{monument}"];
    relation["historic"="high_cross"]["alt_name"="{monument}"];
    node["historic"="high_cross"]["alt_name"="{monument}"];

    way["historic"="stone"]["name:en"="{monument}"];
    relation["historic"="stone"]["name:en"="{monument}"];
    node["historic"="stone"]["name:en"="{monument}"];

    way["historic"="stone"]["name:it"="{monument}"];
    relation["historic"="stone"]["name:it"="{monument}"];
    node["historic"="stone"]["name:it"="{monument}"];

    way["historic"="stone"]["alt_name"="{monument}"];
    relation["historic"="stone"]["alt_name"="{monument}"];
    node["historic"="stone"]["alt_name"="{monument}"];

    way["historic"="yes"]["name:en"="{monument}"];
    relation["historic"="yes"]["name:en"="{monument}"];
    node["historic"="yes"]["name:en"="{monument}"];

    way["historic"="yes"]["name:it"="{monument}"];
    relation["historic"="yes"]["name:it"="{monument}"];
    node["historic"="yes"]["name:it"="{monument}"];

    way["historic"="yes"]["alt_name"="{monument}"];
    relation["historic"="yes"]["alt_name"="{monument}"];
    node["historic"="yes"]["alt_name"="{monument}"];
    );
    (._;>;);
    out center;
    """

    # Fallback to both first and second queries; searches under tourism tags in Italy
    query3 = f"""
    [out:json];

    // Define the search area as Rome
    area["name"="Italia"]->.searchArea;

    // Search for the monument by its name as a tourist attraction
    (
    way(area.searchArea)["tourism"="alpine_hut"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="alpine_hut"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="alpine_hut"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="alpine_hut"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="alpine_hut"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="alpine_hut"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="alpine_hut"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="alpine_hut"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="alpine_hut"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="aquarium"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="aquarium"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="aquarium"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="aquarium"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="aquarium"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="aquarium"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="aquarium"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="aquarium"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="aquarium"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="artwork"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="artwork"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="artwork"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="artwork"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="artwork"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="artwork"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="artwork"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="artwork"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="artwork"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="attraction"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="attraction"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="attraction"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="attraction"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="attraction"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="attraction"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="attraction"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="attraction"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="attraction"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="camp_site"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="camp_site"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="camp_site"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="camp_site"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="camp_site"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="camp_site"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="camp_site"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="camp_site"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="camp_site"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="chalet"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="chalet"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="chalet"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="chalet"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="chalet"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="chalet"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="chalet"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="chalet"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="chalet"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="gallery"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="gallery"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="gallery"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="gallery"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="gallery"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="gallery"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="gallery"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="gallery"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="gallery"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="hostel"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="hostel"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="hostel"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="hostel"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="hostel"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="hostel"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="hostel"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="hostel"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="hostel"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="hotel"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="hotel"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="hotel"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="hotel"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="hotel"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="hotel"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="hotel"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="hotel"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="hotel"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="information"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="information"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="information"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="information"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="information"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="information"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="information"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="information"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="information"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="motel"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="motel"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="motel"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="motel"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="motel"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="motel"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="motel"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="motel"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="motel"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="museum"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="museum"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="museum"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="museum"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="museum"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="museum"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="museum"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="museum"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="museum"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="theme_park"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="theme_park"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="theme_park"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="theme_park"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="theme_park"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="theme_park"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="theme_park"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="theme_park"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="theme_park"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="viewpoint"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="viewpoint"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="viewpoint"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="viewpoint"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="viewpoint"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="viewpoint"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="viewpoint"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="viewpoint"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="viewpoint"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="zoo"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="zoo"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="zoo"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="zoo"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="zoo"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="zoo"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="zoo"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="zoo"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="zoo"]["alt_name"="{monument}"];

    way(area.searchArea)["tourism"="yes"]["name:en"="{monument}"];
    relation(area.searchArea)["tourism"="yes"]["name:en"="{monument}"];
    node(area.searchArea)["tourism"="yes"]["name:en"="{monument}"];

    way(area.searchArea)["tourism"="yes"]["name:it"="{monument}"];
    relation(area.searchArea)["tourism"="yes"]["name:it"="{monument}"];
    node(area.searchArea)["tourism"="yes"]["name:it"="{monument}"];

    way(area.searchArea)["tourism"="yes"]["alt_name"="{monument}"];
    relation(area.searchArea)["tourism"="yes"]["alt_name"="{monument}"];
    node(area.searchArea)["tourism"="yes"]["alt_name"="{monument}"];
    );
    (._;>;);
    out center;
    """

    #Fallback to third query; searches globally
    query4 = f"""
    [out:json];

    // Define the search area as Rome
    area["name"="Italia"]->.searchArea;

    // Search for the monument by its name as a tourist attraction
    (
    way["tourism"="alpine_hut"]["name:en"="{monument}"];
    relation["tourism"="alpine_hut"]["name:en"="{monument}"];
    node["tourism"="alpine_hut"]["name:en"="{monument}"];

    way["tourism"="alpine_hut"]["name:it"="{monument}"];
    relation["tourism"="alpine_hut"]["name:it"="{monument}"];
    node["tourism"="alpine_hut"]["name:it"="{monument}"];

    way["tourism"="alpine_hut"]["alt_name"="{monument}"];
    relation["tourism"="alpine_hut"]["alt_name"="{monument}"];
    node["tourism"="alpine_hut"]["alt_name"="{monument}"];

    way["tourism"="aquarium"]["name:en"="{monument}"];
    relation["tourism"="aquarium"]["name:en"="{monument}"];
    node["tourism"="aquarium"]["name:en"="{monument}"];

    way["tourism"="aquarium"]["name:it"="{monument}"];
    relation["tourism"="aquarium"]["name:it"="{monument}"];
    node["tourism"="aquarium"]["name:it"="{monument}"];

    way["tourism"="aquarium"]["alt_name"="{monument}"];
    relation["tourism"="aquarium"]["alt_name"="{monument}"];
    node["tourism"="aquarium"]["alt_name"="{monument}"];

    way["tourism"="artwork"]["name:en"="{monument}"];
    relation["tourism"="artwork"]["name:en"="{monument}"];
    node["tourism"="artwork"]["name:en"="{monument}"];

    way["tourism"="artwork"]["name:it"="{monument}"];
    relation["tourism"="artwork"]["name:it"="{monument}"];
    node["tourism"="artwork"]["name:it"="{monument}"];

    way["tourism"="artwork"]["alt_name"="{monument}"];
    relation["tourism"="artwork"]["alt_name"="{monument}"];
    node["tourism"="artwork"]["alt_name"="{monument}"];

    way["tourism"="attraction"]["name:en"="{monument}"];
    relation["tourism"="attraction"]["name:en"="{monument}"];
    node["tourism"="attraction"]["name:en"="{monument}"];

    way["tourism"="attraction"]["name:it"="{monument}"];
    relation["tourism"="attraction"]["name:it"="{monument}"];
    node["tourism"="attraction"]["name:it"="{monument}"];

    way["tourism"="attraction"]["alt_name"="{monument}"];
    relation["tourism"="attraction"]["alt_name"="{monument}"];
    node["tourism"="attraction"]["alt_name"="{monument}"];

    way["tourism"="camp_site"]["name:en"="{monument}"];
    relation["tourism"="camp_site"]["name:en"="{monument}"];
    node["tourism"="camp_site"]["name:en"="{monument}"];

    way["tourism"="camp_site"]["name:it"="{monument}"];
    relation["tourism"="camp_site"]["name:it"="{monument}"];
    node["tourism"="camp_site"]["name:it"="{monument}"];

    way["tourism"="camp_site"]["alt_name"="{monument}"];
    relation["tourism"="camp_site"]["alt_name"="{monument}"];
    node["tourism"="camp_site"]["alt_name"="{monument}"];

    way["tourism"="chalet"]["name:en"="{monument}"];
    relation["tourism"="chalet"]["name:en"="{monument}"];
    node["tourism"="chalet"]["name:en"="{monument}"];

    way["tourism"="chalet"]["name:it"="{monument}"];
    relation["tourism"="chalet"]["name:it"="{monument}"];
    node["tourism"="chalet"]["name:it"="{monument}"];

    way["tourism"="chalet"]["alt_name"="{monument}"];
    relation["tourism"="chalet"]["alt_name"="{monument}"];
    node["tourism"="chalet"]["alt_name"="{monument}"];

    way["tourism"="gallery"]["name:en"="{monument}"];
    relation["tourism"="gallery"]["name:en"="{monument}"];
    node["tourism"="gallery"]["name:en"="{monument}"];

    way["tourism"="gallery"]["name:it"="{monument}"];
    relation["tourism"="gallery"]["name:it"="{monument}"];
    node["tourism"="gallery"]["name:it"="{monument}"];

    way["tourism"="gallery"]["alt_name"="{monument}"];
    relation["tourism"="gallery"]["alt_name"="{monument}"];
    node["tourism"="gallery"]["alt_name"="{monument}"];

    way["tourism"="hostel"]["name:en"="{monument}"];
    relation["tourism"="hostel"]["name:en"="{monument}"];
    node["tourism"="hostel"]["name:en"="{monument}"];

    way["tourism"="hostel"]["name:it"="{monument}"];
    relation["tourism"="hostel"]["name:it"="{monument}"];
    node["tourism"="hostel"]["name:it"="{monument}"];

    way["tourism"="hostel"]["alt_name"="{monument}"];
    relation["tourism"="hostel"]["alt_name"="{monument}"];
    node["tourism"="hostel"]["alt_name"="{monument}"];

    way["tourism"="hotel"]["name:en"="{monument}"];
    relation["tourism"="hotel"]["name:en"="{monument}"];
    node["tourism"="hotel"]["name:en"="{monument}"];

    way["tourism"="hotel"]["name:it"="{monument}"];
    relation["tourism"="hotel"]["name:it"="{monument}"];
    node["tourism"="hotel"]["name:it"="{monument}"];

    way["tourism"="hotel"]["alt_name"="{monument}"];
    relation["tourism"="hotel"]["alt_name"="{monument}"];
    node["tourism"="hotel"]["alt_name"="{monument}"];

    way["tourism"="information"]["name:en"="{monument}"];
    relation["tourism"="information"]["name:en"="{monument}"];
    node["tourism"="information"]["name:en"="{monument}"];

    way["tourism"="information"]["name:it"="{monument}"];
    relation["tourism"="information"]["name:it"="{monument}"];
    node["tourism"="information"]["name:it"="{monument}"];

    way["tourism"="information"]["alt_name"="{monument}"];
    relation["tourism"="information"]["alt_name"="{monument}"];
    node["tourism"="information"]["alt_name"="{monument}"];

    way["tourism"="motel"]["name:en"="{monument}"];
    relation["tourism"="motel"]["name:en"="{monument}"];
    node["tourism"="motel"]["name:en"="{monument}"];

    way["tourism"="motel"]["name:it"="{monument}"];
    relation["tourism"="motel"]["name:it"="{monument}"];
    node["tourism"="motel"]["name:it"="{monument}"];

    way["tourism"="motel"]["alt_name"="{monument}"];
    relation["tourism"="motel"]["alt_name"="{monument}"];
    node["tourism"="motel"]["alt_name"="{monument}"];

    way["tourism"="museum"]["name:en"="{monument}"];
    relation["tourism"="museum"]["name:en"="{monument}"];
    node["tourism"="museum"]["name:en"="{monument}"];

    way["tourism"="museum"]["name:it"="{monument}"];
    relation["tourism"="museum"]["name:it"="{monument}"];
    node["tourism"="museum"]["name:it"="{monument}"];

    way["tourism"="museum"]["alt_name"="{monument}"];
    relation["tourism"="museum"]["alt_name"="{monument}"];
    node["tourism"="museum"]["alt_name"="{monument}"];

    way["tourism"="theme_park"]["name:en"="{monument}"];
    relation["tourism"="theme_park"]["name:en"="{monument}"];
    node["tourism"="theme_park"]["name:en"="{monument}"];

    way["tourism"="theme_park"]["name:it"="{monument}"];
    relation["tourism"="theme_park"]["name:it"="{monument}"];
    node["tourism"="theme_park"]["name:it"="{monument}"];

    way["tourism"="theme_park"]["alt_name"="{monument}"];
    relation["tourism"="theme_park"]["alt_name"="{monument}"];
    node["tourism"="theme_park"]["alt_name"="{monument}"];

    way["tourism"="viewpoint"]["name:en"="{monument}"];
    relation["tourism"="viewpoint"]["name:en"="{monument}"];
    node["tourism"="viewpoint"]["name:en"="{monument}"];

    way["tourism"="viewpoint"]["name:it"="{monument}"];
    relation["tourism"="viewpoint"]["name:it"="{monument}"];
    node["tourism"="viewpoint"]["name:it"="{monument}"];

    way["tourism"="viewpoint"]["alt_name"="{monument}"];
    relation["tourism"="viewpoint"]["alt_name"="{monument}"];
    node["tourism"="viewpoint"]["alt_name"="{monument}"];

    way["tourism"="zoo"]["name:en"="{monument}"];
    relation["tourism"="zoo"]["name:en"="{monument}"];
    node["tourism"="zoo"]["name:en"="{monument}"];

    way["tourism"="zoo"]["name:it"="{monument}"];
    relation["tourism"="zoo"]["name:it"="{monument}"];
    node["tourism"="zoo"]["name:it"="{monument}"];

    way["tourism"="zoo"]["alt_name"="{monument}"];
    relation["tourism"="zoo"]["alt_name"="{monument}"];
    node["tourism"="zoo"]["alt_name"="{monument}"];

    way["tourism"="yes"]["name:en"="{monument}"];
    relation["tourism"="yes"]["name:en"="{monument}"];
    node["tourism"="yes"]["name:en"="{monument}"];

    way["tourism"="yes"]["name:it"="{monument}"];
    relation["tourism"="yes"]["name:it"="{monument}"];
    node["tourism"="yes"]["name:it"="{monument}"];

    way["tourism"="yes"]["alt_name"="{monument}"];
    relation["tourism"="yes"]["alt_name"="{monument}"];
    node["tourism"="yes"]["alt_name"="{monument}"];
    );
    (._;>;);
    out center;
    """

    return query1, query2, query3, query4