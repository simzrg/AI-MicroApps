import streamlit as st
import openai
import requests

# Constants for App Configuration
APP_TITLE = "LaTeX Generator"
APP_INTRO = "This app accepts images via upload or URL and returns LaTeX code."
APP_HOW_IT_WORKS = """
This app creates LaTeX code from images. 
For most images, it provides properly formatted LaTeX code.
"""

DEFAULT_PROMPT = (
    "You accept images in URL and file format containing mathematical equations, "
    "symbols, and text. Convert the images into properly formatted LaTeX code. "
    "Output: Provide the final LaTeX code in a format that can be easily copied or exported."
)

# OpenAI API Key (replace with your key)
openai.api_key = "your_openai_api_key_here"

# Helper Function: Validate URLs
def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Helper Function: Generate Dynamic Prompt
def generate_system_prompt(base_prompt, urls, files, latex, alt_text, transcript):
    prompt = base_prompt + "\n\n"
    if urls:
        prompt += f"I have provided the following image URLs: {', '.join(urls)}.\n"
    if files:
        prompt += f"I have uploaded the following image files: {', '.join(files)}.\n"
    prompt += "Please perform the following actions:\n"
    if latex:
        prompt += "- Generate properly formatted LaTeX code from the images.\n"
    if alt_text:
        prompt += "- Create descriptive alt text for the images.\n"
    if transcript:
        prompt += "- Generate a visual transcript for the images.\n"
    return prompt.strip()

# Helper Function: Call OpenAI API with GPT-4
def call_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# App Header
st.title(APP_TITLE)
st.markdown(APP_INTRO)
st.markdown(APP_HOW_IT_WORKS)

# Sidebar for Advanced Settings
with st.sidebar:
    st.title("Advanced Settings")
    system_prompt = st.text_area("Edit System Prompt", value=DEFAULT_PROMPT, height=150)

# Image Input Section
st.subheader("Input Images")
image_urls = st.text_area("Enter Image URLs (one per line)")
uploaded_files = st.file_uploader(
    "Upload Image Files",
    type=["png", "jpeg", "jpg", "gif", "webp"],
    accept_multiple_files=True,
)

# Output Options
st.subheader("Output Options")
generate_latex = st.checkbox("Generate LaTeX Code", value=True)
generate_alt_text = st.checkbox("Generate Alt Text", value=False)
generate_transcript = st.checkbox("Generate Visual Transcript", value=False)

# Submit Button
if st.button("Submit"):
    # Collect Input Data
    urls = [url.strip() for url in image_urls.split("\n") if url.strip()]
    file_names = [uploaded_file.name for uploaded_file in uploaded_files]

    # Validate Inputs
    if not urls and not uploaded_files:
        st.error("Please provide at least one image URL or upload an image.")
    else:
        # Generate Dynamic Prompt
        finalized_prompt = generate_system_prompt(
            system_prompt,
            urls,
            file_names,
            generate_latex,
            generate_alt_text,
            generate_transcript,
        )

        # Display Finalized Prompt
        st.write("### Finalized Prompt Sent to OpenAI:")
        st.code(finalized_prompt)

        # Call OpenAI GPT-4 API
        st.write("### Results:")
        result = call_openai_api(finalized_prompt)
        st.text(result)

        # Optionally Display Uploaded Files
        if uploaded_files:
            st.write("### Uploaded Images:")
            for uploaded_file in uploaded_files:
                st.image(uploaded_file, caption=uploaded_file.name)
