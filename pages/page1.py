import streamlit as st

# Page title
st.title("YouTube Video Viewer")

# Input for YouTube video URL
url = st.text_input("Enter the YouTube video URL:", 'https://www.youtube.com/watch?v=YvIZzziXK4c')

if url:
    # Extract the video ID from the URL
    video_id = url.split("v=")[-1].split("&")[0]
    video_embed_url = f"https://www.youtube.com/embed/{video_id}"

    # Display the video in an iframe
    st.markdown(
        f"""
        <iframe width="100%" height="600" src="{video_embed_url}" frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("Please enter a YouTube video URL to display the video.")

