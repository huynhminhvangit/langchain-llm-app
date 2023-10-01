import langchain_youtube_helper as lch
import streamlit as st
import textwrap

# st.title("Pets name generator")

# animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))

# if animal_type == "Cat":
#     pet_color = st.sidebar.text_area(label= "What color is you cat?", max_chars = 15)
# if animal_type == "Dog":
#     pet_color = st.sidebar.text_area(label= "What color is you dog?", max_chars = 15)
# if animal_type == "Cow":
#     pet_color = st.sidebar.text_area(label= "What color is you cow?", max_chars = 15)
# if animal_type == "Hamster":
#     pet_color = st.sidebar.text_area(label= "What color is you hamster?", max_chars = 15)

# if pet_color:
#     response = lch.generate_pet_name(animal_type = animal_type, pet_color = pet_color)
#     st.text(response['pet_name'])

# Project 2
st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label="What is the Youtube video URL?",
            max_chars=50
        )

        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=50,
            key="query"
        )

        openai_api_key = st.sidebar.text_input(
            label="OpenAI API key",
            key="langchain_search_api_key_openai",
            max_chars=100,
            type="password"
        )

        submit_button = st.form_submit_button(label="Submit")

    if query and youtube_url:
        if not openai_api_key:
            st.info("Please add you OpenAI API key to continue.")
            st.stop()
        else:
            db = lch.create_db_from_youtube_video_url(youtube_url)
            response, docs = lch.get_response_from_query(db, query=query)

            st.subheader("Answer:")
            st.text(textwrap.fill(response, width=85))