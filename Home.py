import streamlit as st
from pathlib import Path

st.set_page_config(page_title="World Cities App", page_icon="🌎")

st.title("🌎 World Cities Explorer")
st.write(
    """
    Welcome to the World Cities Explorer!  
    Discover information about cities around the world.
    """
)

# Button to navigate to the main app (app.py in the "pages" directory)
pages_dir = Path("pages")
app_file = pages_dir / "app.py"

if st.button("Go to App"):
    # Streamlit multipage navigation: set query params or instruct user
    st.experimental_set_query_params(page="app")
    st.info("If you're not redirected automatically, please select 'app' from the sidebar pages!")
