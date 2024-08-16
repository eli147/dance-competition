import streamlit as st
import random

# Function to compare videos automatically
def video_comparison():
    st.title("Video Comparison")

    # Upload two video files
    uploaded_video1 = st.file_uploader("Upload the first video clip:", type=["mp4", "mov", "avi"])
    uploaded_video2 = st.file_uploader("Upload the second video clip:", type=["mp4", "mov", "avi"])

    if uploaded_video1 and uploaded_video2:
        st.write("**Comparing the two video clips:**")

        # Display both videos side by side
        col1, col2 = st.columns(2)

        with col1:
            st.video(uploaded_video1, start_time=0)
            st.write("**Video 1**")

        with col2:
            st.video(uploaded_video2, start_time=0)
            st.write("**Video 2**")

        # Decide which video is better using a random choice
        # Note: You might want to implement actual comparison logic instead of random choice
        better_video = random.choice([uploaded_video1, uploaded_video2])

        st.write("**Automatic Decision:**")
        st.write("**The chosen better video is displayed below:**")
        st.video(better_video, start_time=0)

    else:
        st.write("Please upload both video clips to compare.")

video_comparison()
