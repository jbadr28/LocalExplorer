import json 
import streamlit as st

def format(response):
    """
    Params : repsonse : ChatCompletion Object
    Returns  : message String 
    takes ChatCompletion from chatgpt API and return formated reponse to be desplayed on the web page
    
    """
    unporcessed = response.choices[0].message.content
    json_info = json.loads(unporcessed)
    info = response.choices[0].message.content.split(',')
    name,latitude,longitude,paragraph = json_info['name'],json_info['latitude'],json_info['longitude'],json_info['suggestion']
    return name,latitude,longitude,paragraph

def get_ggl_maps_embed_code(start_lat,start_lon,dest_lat,dest_lon):
    """"
    takes start and destination location, and return embed url for google maps highlighting the route

    """
    url = f"https://www.google.com/maps/embed/v1/directions?origin={start_lat}%20{start_lon}%20&destination={dest_lat}%20{dest_lon}%20&key={st.secrets['GOOGLE_MAPS_API_KEY']}"
    return url