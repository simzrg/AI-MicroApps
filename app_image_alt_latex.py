import streamlit as st
import openai
import requests

# Constants for App Configuration
APP_URL = ""  # TODO: Add URL for the app
APP_IMAGE = ""  # TODO: Add default image for the app
PUBLISHED = False  # Status of the app

APP_TITLE = "LaTeX Generator"
APP_INTRO = "This app accepts images via upload or URL and returns LaTeX code."
APP_HOW_IT_WORKS = """
This app creates LaTeX code from images. 
For most images, it provides properly formatted LaTeX code.
"""

SYSTEM_PROMPT = (
    "You accept images in URL and file format containing mathematical equations, "
    "symbols, and text. Convert the images into properly formatted LaTeX code. "
    "Output: Provide the final LaTeX code in a format that can be easily copied or exported."
)

PHASES = {
    "phase1": {
        "name": "Image Input and LaTeX Generation",
        "fields": {
            "http_img_urls": {
                "type": "text_area",
                "label": "Enter image URLs",
            },
            "uploaded_files": {
                "type": "file_uploader",
                "label": "Choose files",
                "allowed_files": ['png', 'jpeg', 'gif', 'webp'],
                "multiple_files": True,
            },
        },
        "phase_instructions": "Generate LaTeX for the image URLs and uploads",
        "user_prompt": [
            {
                "prompt": """I am sending you one or more app_images. Please provide separate LaTeX code for each image I send. The LaTeX code should:
                - Convert the images into properly formatted LaTeX code."""
            }
        ],
        "show_prompt": True,
        "allow_skip": False,
    }
}

# OpenAI API Key
openai.api_key = "your_openai_api_key_here"  # Replace with your OpenAI API key

# Helper Function to Validate URLs
def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Generate Dynamic Prompt
def generate_system_prompt(base_prompt, urls, files, generate_latex):
    prompt = base_prompt + "\n\n"
    if urls:
        prompt += f"I have provided the following image URLs: {urls}\n"
    if files:
        prompt += f"I have uploaded the following image files: {', '.join(files)}\n"
    if generate_latex:
        prompt += "- Please generate properly formatted LaTeX code for these images.\n"
    return prompt.strip()

# Function to Call OpenAI API
def call_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# App Setup
st.set_page_config(
    page_title="LaTeX Generator",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Sidebar for Advanced Settings
with st.sidebar:
    st.title("Advanced Settings")
    system_prompt = st.text_area(
        label="Edit System Prompt",
        value=SYSTEM_PROMPT,
        height=150,
    )

# Main Application
st.title(APP_TITLE)
st.markdown(APP_INTRO)
st.markdown(APP_HOW_IT_WORKS)

# Input Phase
st.subheader("Input Images")
image_url = st.text_area("Enter Image URLs (one per line)")
uploaded_files = st.file_uploader(
    "Upload Image Files",
    type=["png", "jpeg", "jpg", "gif", "webp"],
    accept_multiple_files=True,
)

# Options
generate_latex = st.checkbox("Generate LaTeX Code", value=True)

# Submit Button
if st.button("Submit"):
    urls = [url.strip() for url in image_url.split("\n") if url.strip()]
    file_names = [uploaded_file.name for uploaded_file in uploaded_files]

    # Validate Input
    if not urls and not uploaded_files:
        st.error("Please provide at least one image URL or upload an image.")
    else:
        # Generate Prompt
        dynamic_prompt = generate_system_prompt(
            system_prompt,
            urls,
            file_names,
            generate_latex,
        )

        st.write("### Finalized Prompt Sent to OpenAI:")
        st.code(dynamic_prompt)

        # Process with OpenAI
        result = call_openai_api(dynamic_prompt)

        st.write("### Results:")
        st.text(result)

        # Display Uploaded Files (Optional)
        if uploaded_files:
            st.write("### Uploaded Images:")
            for uploaded_file in uploaded_files:
                st.image(uploaded_file, caption=uploaded_file.name)
