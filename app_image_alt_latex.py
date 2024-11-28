APP_URL = ""  # TODO: Add URL for the app
APP_IMAGE = ""  # TODO: Add default image for the app
PUBLISHED = False  # Status of the app

APP_TITLE = "Image Description Generator"
APP_INTRO = "This app accepts images via upload or URL and returns appropriate descriptions."

APP_HOW_IT_WORKS = """
This app creates descriptions for images. 
For most images, it provides concise alt text based on the most important concept displayed.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = (
    "You accept images in URL and file format and provide accurate descriptions. "
    "Output: Provide descriptions that are concise and contextually relevant."
)

PHASES = {
    "phase1": {
        "name": "Image Input and Description Generation",
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
        "phase_instructions": "Generate descriptions for the image URLs and uploads",
        "user_prompt": [
            {
                "prompt": """I am sending you one or more app_images. Please provide appropriate descriptions for each image I send. The descriptions should:
                - Describe the most important concept displayed in the image in less than 120 characters."""
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

COMPLETION_MESSAGE = "Thanks for using the Image Description Generator service"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "Image Description Generator",
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
    # Simulated response logic
    response = {
        "input_prompt": prompt,
        "results": [
            "Description 1: This is a simulated response for image 1.",
            "Description 2: This is a simulated response for image 2.",
        ],
    }
    return response

# Helper Function: Build Prompt Dynamically
def build_prompt(system_prompt, urls, files, options):
    """
    Build the dynamic system prompt based on user inputs and options.
    """
    prompt = system_prompt + "\n\n"
    
    if urls:
        prompt += f"I have provided the following image URLs: {', '.join(urls)}.\n"
    if files:
        prompt += f"I have uploaded the following image files: {', '.join(files)}.\n"

    # Handle complex image option
    if options.get("complex_image"):
        prompt += (
            "I am sending you one or more complex app_images. "
            "Please provide a short description of the most important concept depicted in the image; "
            "and a long description to explain the relationship between components to provide a detailed "
            "and informative description of the image.\n"
        )
    elif options.get("important_text"):
        # Handle important text option
        prompt += "Transcribe text verbatim to provide a detailed and informative description of the image.\n"
    else:
        # Default prompt if no options are selected
        prompt += (
            "I am sending you one or more app_images. Please provide separate appropriate alt text for each image I send. "
            "The alt text should describe the most important concept displayed in the image in less than 120 characters.\n"
        )
    
    return prompt.strip()

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

    # Options for Image Processing
    st.subheader("Image Processing Options")
    complex_image = st.checkbox("Complex Image")
    important_text = st.checkbox("Important Text")

    # Submit Button
    if st.button("Submit"):
        if not urls and not uploaded_files:
            st.error("Please provide at least one URL or upload an image.")
        else:
            # Prepare inputs for prompt
            urls = [url.strip() for url in urls if url.strip()]
            file_names = [file.name for file in uploaded_files]

            # Build dynamic prompt
            options = {
                "complex_image": complex_image,
                "important_text": important_text,
            }
            prompt = build_prompt(system_prompt, urls, file_names, options)

            # Display Finalized Prompt
            st.write("### Finalized Prompt")
            st.code(prompt)

            # Simulate LLM Call (Replace with real API call to gpt-4o)
            response = call_llm(prompt, model=config["PREFERRED_LLM"])

            # Display AI Results
            st.write("### Results")
            for result in response["results"]:
                st.text(result)

            # Optionally Display Uploaded Files
            if uploaded_files:
                st.write("### Uploaded Images")
                for uploaded_file in uploaded_files:
                    st.image(uploaded_file, caption=uploaded_file.name)

# Run the App
if __name__ == "__main__":
    main(config=globals())
