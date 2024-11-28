APP_URL = ""  # TODO: Add URL for the app
APP_IMAGE = ""  # TODO: Add default image for the app
PUBLISHED = False  # Status of the app

APP_TITLE = "LaTeX Generator"
APP_INTRO = "This app accepts images via upload or URL and returns LaTeX code."

APP_HOW_IT_WORKS = """
This app creates LaTeX code from images. 
For most images, it provides properly formatted LaTeX code.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = (
    "You accept app_images in url and file format to generate description or alt text according to WCAG 2.2 AA accessibility standards.  "
)

PHASES = {
    "phase1": {
        "name": "Image Input and LaTeX Generation",
        "fields": {
            "http_img_urls": {
                "type": "text_area",
                "label": "Enter image URLs"
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

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thanks for using the LaTeX Generator service"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "LaTeX Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

# Import necessary libraries
import streamlit as st

# Placeholder for LLM Functionality
def call_llm(prompt, model):
    """
    Simulate a call to the LLM (e.g., gpt-4o).
    Replace this with the real API call or backend logic.
    """
    return f"Simulated response for the prompt:\n\n{prompt}"

# Main Application Function
def main(config):
    st.set_page_config(**config["PAGE_CONFIG"])

    # Title and Introduction
    st.title(config["APP_TITLE"])
    st.markdown(config["APP_INTRO"])
    st.markdown(config["APP_HOW_IT_WORKS"])

    # Sidebar for Advanced Settings
    with st.sidebar:
        st.title("Advanced Settings")
        system_prompt = st.text_area("Edit System Prompt", value=config["SYSTEM_PROMPT"], height=150)

    # Phase 1: Image Input
    st.subheader(config["PHASES"]["phase1"]["name"])
    st.write(config["PHASES"]["phase1"]["phase_instructions"])

    # Collect URLs and uploaded files
    urls = st.text_area(config["PHASES"]["phase1"]["fields"]["http_img_urls"]["label"]).splitlines()
    uploaded_files = st.file_uploader(
        config["PHASES"]["phase1"]["fields"]["uploaded_files"]["label"],
        type=config["PHASES"]["phase1"]["fields"]["uploaded_files"]["allowed_files"],
        accept_multiple_files=config["PHASES"]["phase1"]["fields"]["uploaded_files"]["multiple_files"],
    )

    # Output Options
    st.subheader("Output Options")
    generate_latex = st.checkbox("Generate LaTeX Code", value=True)
    generate_alt_text = st.checkbox("Generate Alt Text", value=False)
    generate_transcript = st.checkbox("Generate Visual Transcript", value=False)

    # Submit Button
    if st.button("Submit"):
        if not urls and not uploaded_files:
            st.error("Please provide at least one URL or upload an image.")
        else:
            # Prepare inputs for prompt
            urls = [url.strip() for url in urls if url.strip()]
            file_names = [file.name for file in uploaded_files]

            # Build dynamic prompt
            prompt = system_prompt + "\n\n"
            if urls:
                prompt += f"Image URLs provided: {', '.join(urls)}\n"
            if file_names:
                prompt += f"Uploaded file names: {', '.join(file_names)}\n"
            if generate_latex:
                prompt += "- Generate LaTeX code.\n"
            if generate_alt_text:
                prompt += "- Create alt text.\n"
            if generate_transcript:
                prompt += "- Generate visual transcripts.\n"

            # Display Finalized Prompt
            st.write("### Finalized Prompt")
            st.code(prompt)

            # Simulate LLM Call (Replace with real API call to gpt-4o)
            result = call_llm(prompt, model=config["PREFERRED_LLM"])

            # Display Results
            st.write("### Results")
            st.text(result)

            # Optionally Display Uploaded Files
            if uploaded_files:
                st.write("### Uploaded Images")
                for uploaded_file in uploaded_files:
                    st.image(uploaded_file, caption=uploaded_file.name)

# Run the App
if __name__ == "__main__":
    main(config=globals())