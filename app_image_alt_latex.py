import streamlit as st
import openai
import requests

# OpenAI API Key
openai.api_key = "your_openai_api_key_here"  # Replace with your OpenAI API key

# Helper Function to Validate URLs
def is_valid_url(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Function to Call OpenAI API
def call_openai_api(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with "gpt-3.5-turbo" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating LaTeX, alt text, and visual transcripts."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Dynamic Prompt Generation
def generate_system_prompt(base_prompt, urls, files, generate_latex, generate_alt_text, generate_visual_transcript):
    # Start with the base prompt
    prompt = base_prompt + "\n\n"
    
    # Add context for input sources
    if urls:
        prompt += f"I have provided image URLs: {urls}.\n"
    if files:
        prompt += f"I have uploaded image files: {', '.join(files)}.\n"
    
    # Add user-selected options
    prompt += "Please perform the following actions based on my selections:\n"
    if generate_latex:
        prompt += "- Generate properly formatted LaTeX code from the images.\n"
    if generate_alt_text:
        prompt += "- Create descriptive alt text for the images.\n"
    if generate_visual_transcript:
        prompt += "- Generate visual transcripts for the images.\n"
    
    return prompt.strip()

# Page Configuration
st.set_page_config(
    page_title="LaTeX Generator",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Constants
APP_TITLE = "LaTeX Generator"
APP_INTRO = (
    "This app accepts images via URL or upload and generates LaTeX code, "
    "alt text, and visual transcripts based on your selections."
)
DEFAULT_PROMPT = (
    "You accept images in URL and file format containing mathematical equations, "
    "symbols, and text. Convert them into properly formatted LaTeX code. "
    "Output: Provide the final LaTeX code in a format that can be easily copied or exported."
)

# Sidebar for advanced settings
with st.sidebar:
    st.title("Advanced Settings")
    system_prompt = st.text_area(
        label="Edit System Prompt",
        value=DEFAULT_PROMPT,
        height=150,
    )

# App Header
st.title(APP_TITLE)
st.markdown(APP_INTRO)

# Image Input Section
st.subheader("Image Input")
image_url = st.text_area("Enter Image URLs (one per line)")
uploaded_files = st.file_uploader(
    "Upload Images",
    type=["png", "jpeg", "jpg", "gif", "webp"],
    accept_multiple_files=True,
)

# Options Section
st.subheader("Output Options")
generate_latex = st.checkbox("Generate LaTeX Code", value=True)
generate_alt_text = st.checkbox("Generate Alt Text", value=False)
generate_visual_transcript = st.checkbox("Generate Visual Transcript", value=False)

# Submit Button and Processing
if st.button("Submit"):
    # Validate input
    urls = [url.strip() for url in image_url.split("\n") if url.strip()]
    file_names = [uploaded_file.name for uploaded_file in uploaded_files]

    if not urls and not uploaded_files:
        st.error("Please provide at least one image URL or upload an image.")
    else:
        # Prepare the dynamic prompt
        dynamic_prompt = generate_system_prompt(
            system_prompt,
            urls,
            file_names,
            generate_latex,
            generate_alt_text,
            generate_visual_transcript,
        )

        # Display the finalized prompt
        st.write("### Finalized Prompt Sent to OpenAI:")
        st.code(dynamic_prompt)

        # Send request to OpenAI API
        st.write("### Results:")
        result = call_openai_api(dynamic_prompt)
        st.text(result)

        # Optionally, display uploaded files
        if uploaded_files:
            st.write("### Uploaded Images:")
            for uploaded_file in uploaded_files:
                st.image(uploaded_file, caption=uploaded_file.name)
