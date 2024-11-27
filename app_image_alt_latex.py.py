import streamlit as st

APP_URL = "https://example.com/app"  # Example URL
APP_IMAGE = "https://example.com/default_image.png"  # Example default image
PREFERRED_LLM = "gpt-4o"  # Matching preferred LLM

# Updated System Prompt to include both LaTeX and alt text generation
SYSTEM_PROMPT = (
    "You accept images in URL and file formats containing mathematical equations, symbols, "
    "and text. You can generate three outputs for each image: "
    "- (1) Accurate and properly formatted LaTeX code. "
    "- (2) Alt text describing the image content (for simple images). "
    "- (3) An accessible visual transcript for complex images. "
    "Output: Provide these outputs in a user-friendly format, depending on the image type."
)

# LLM configuration overrides
LLM_CONFIG_OVERRIDE = {
    "temperature": 0.2,  # Ensures deterministic output for accurate results
    "top_p": 0.9        # Balances diversity and relevance
}

PAGE_CONFIG = {
    "page_title": "LaTeX and Accessible Transcript Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

# Main App Logic
def main():
    st.set_page_config(**PAGE_CONFIG)

    # Display System Prompt Section
    st.header("System Prompt")
    st.text_area("View/Edit System Prompt:", value=SYSTEM_PROMPT, height=200)

    # Section for URL Input
    st.header("Image Input via URLs")
    http_img_urls = st.text_area("Enter image URLs (one per line):", height=150)

    if http_img_urls:
        url_list = http_img_urls.strip().split("\n")
        for idx, url in enumerate(url_list):
            st.image(url, caption=f"Preview of URL Image {idx + 1}")
            is_complex_url = st.checkbox(f"Is URL Image {idx + 1} complex?", key=f"url_{idx}")

            if is_complex_url:
                st.text_area(f"Accessible Transcript for URL Image {idx + 1}:", value="Generating detailed transcript...")
            else:
                st.text_area(f"LaTeX and Alt Text for URL Image {idx + 1}:", value="Generating concise outputs...")

    # Section for File Upload
    st.header("Image Input via File Upload")
    uploaded_files = st.file_uploader("Upload images", type=["png", "jpeg", "gif", "webp"], accept_multiple_files=True)

    if uploaded_files:
        for idx, file in enumerate(uploaded_files):
            st.image(file, caption=f"Preview of Uploaded Image {idx + 1}")
            is_complex_file = st.checkbox(f"Is Uploaded Image {idx + 1} complex?", key=f"file_{idx}")

            if is_complex_file:
                st.text_area(f"Accessible Transcript for Uploaded Image {idx + 1}:", value="Generating detailed transcript...")
            else:
                st.text_area(f"LaTeX and Alt Text for Uploaded Image {idx + 1}:", value="Generating concise outputs...")

    # Restart Button
    if st.button("Restart"):
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    main()
