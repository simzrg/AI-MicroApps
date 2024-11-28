import streamlit as st

# Constants
APP_TITLE = "LaTeX Generator"
APP_DESCRIPTION = (
    "This app accepts images via upload or URL and generates LaTeX code for the content."
)
APP_HOW_IT_WORKS = """
This app processes images containing mathematical equations, symbols, and text, and returns the equivalent properly formatted LaTeX code.
"""

# Streamlit Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# App Header
st.title(APP_TITLE)
st.write(APP_DESCRIPTION)
st.markdown(APP_HOW_IT_WORKS)

# Input Section
st.subheader("Upload Image Files or Provide URLs")

uploaded_files = st.file_uploader(
    label="Choose files",
    type=["png", "jpeg", "gif", "webp"],
    accept_multiple_files=True,
)

http_img_urls = st.text_area(
    label="Enter image URLs (one per line)", 
    placeholder="https://example.com/image1.png\nhttps://example.com/image2.png"
)

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {
    "max_tokens": 8000,
    "temperature": 1.0
}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

# Footer
st.info("Thanks for using the LaTeX Generator service!")
