import requests

def bb_query(monument_id):

    geo_query = f"""
    [out:json];
    (
    relation({monument_id});
    way({monument_id});
    node({monument_id});
    );
    out bb;
    out center;
    """

    return geo_query