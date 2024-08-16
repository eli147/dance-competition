import streamlit as st

# Set up page configuration
st.set_page_config(page_title="My Dance Competition App", layout="wide")


def show_home():
    # Use an expander to create a full-width container
    st.title("Welcome to the Dance Competition App")
    st.write("Here you can find the latest dance competition updates and videos.")
    with st.container():
        # Display the background image
        st.image('images/image.jpeg', use_column_width=True, caption='Background Image')

    # Add a new container for the content
    st.markdown(
        """
        <style>
        .content-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
            z-index: 1;
            background: rgba(0, 0, 0, 0.5); /* Optional: Add a semi-transparent overlay */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


st.sidebar.title("Navigation")
pages = {
    "Home": "main.py",
    "YouTube Video": "page1.py",
    "Video Comparison": "page2.py"  # Adding the new page to the sidebar
}
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page
if selection == 'Home':
    show_home()
else:
    page = pages[selection]
    with open(f"pages/{page}") as f:
        exec(f.read())
