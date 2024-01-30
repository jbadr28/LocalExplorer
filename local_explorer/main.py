import streamlit as st
import streamlit.components.v1 as components
from streamlit_geolocation import streamlit_geolocation
from api.openweatherapi import get_weather
from utilities import format, get_ggl_maps_embed_code
from openai import OpenAI

st.title("Local Explorer")

st.write('please press the button and grant the app permission to access to your location')

location = streamlit_geolocation()
if location['latitude']!=None:
    print('weather')
    weather = get_weather(location['latitude'],location['longitude']).json()
    print(weather)

    

    # Set OpenAI API key from Streamlit secrets
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message['role'] == 'user':
                st.markdown(message["content"])
            else :
                #full_response += (message["content"])
                st.markdown(message["content"][3])
                st.markdown(message['role'])
                st.components.v1.iframe(src=get_ggl_maps_embed_code(location['latitude'],location['longitude'],message["content"][1],message["content"][2]))

            
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            response  =  client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {
                    "role": "system",
                    "content": "you are an assistant that takes the weather data and longitude and the latitude of a location and and you suggest to the user activities or  places to visit based on the given location and weather. the suggestion should be as close to the given location as possible.the user message will be structured as the following\nweather = dictionary from openweather api\nand user_prompt = string\n\n\nand your response should be structured as a json where the first element is the name for the place, the second element is the latitude ,the third element is the longitude,  the forth element of the json is a small paragraph in which you suggest an activity or a place to visit and you explain what interesting about your suggestion,the json keys should be 'name','latitude','longitude','suggestion'"
                },
                {
                    "role": "user",
                    "content": f"message = {prompt}\n weather={weather}"
                }
                ],
                temperature=1,
                max_tokens=400,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
            full_response += (str(response))
            name,latitude,longitude,paragraph = format(response)
            st.session_state.messages.append({"role": "assistant", "content": [name,latitude,longitude,paragraph]})
            st.markdown(paragraph)
            print(get_ggl_maps_embed_code(34,-7.3,latitude,longitude))
            st.components.v1.iframe(src=get_ggl_maps_embed_code(location['latitude'],location['longitude'],latitude,longitude))#,width=400, height=100, scrolling=False)