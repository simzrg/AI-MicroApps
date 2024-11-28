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

# Process LaTeX Generation
if st.button("Generate LaTeX Code"):
    if not uploaded_files and not http_img_urls.strip():
        st.error("Please upload files or enter image URLs.")
    else:
        with st.spinner("Processing..."):
            # Process uploaded files
            if uploaded_files:
                st.subheader("LaTeX Code from Uploaded Files")
                for file in uploaded_files:
                    # Streamlit AI interaction for file processing
                    response = st.experimental_connection("ai").run(file.read())
                    st.code(response, language="latex")

            # Process URLs
            if http_img_urls.strip():
                st.subheader("LaTeX Code from Image URLs")
                for url in http_img_urls.splitlines():
                    # Streamlit AI interaction for URL processing
                    response = st.experimental_connection("ai").run(url)
                    st.code(response, language="latex")

        st.success("LaTeX code generation completed.")

# Footer
st.info("Thanks for using the LaTeX Generator service!")
