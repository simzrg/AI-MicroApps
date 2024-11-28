APP_URL = "https://alt-text.streamlit.app"
APP_IMAGE = "alt_text_flat.webp"
PUBLISHED = True

APP_TITLE = "Alt Text Generator"
APP_INTRO = """This app accepts images via upload or URL and returns alt text for accessibility."""

APP_HOW_IT_WORKS = """
This app creates alt text for accessibility from images. 
For most images, it provides brief alt text to describe the image, focusing on the most important information first. 

For complex images, like charts and graphs, the app creates a short description of the image and a longer detail that describes what the complex image is conveying. 

For more information, see <a href="https://www.w3.org/WAI/tutorials/images/" target="_blank">W3C Images Accessibility Guidelines</a>.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = (
    "You accept images in URL and file format to generate description or alt text according to W3C standards."
)

PHASES = {
    "phase1": {
        "name": "Image Input and Alt Text Generation",
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
            "important_text": {
                "type": "checkbox",
                "label": "The text in my image(s) is important",
                "value": False,
                "help": "If text is important, it should be included in the alt text. If it is irrelevant or covered in text elsewhere on the page, it should not be included.",
            },
            "complex_image": {
                "type": "checkbox",
                "label": "My image is a complex image (chart, infographic, etc...)",
                "value": False,
                "help": "Complex images get both a short and a long description of the image.",
            },
        },
        "phase_instructions": "Generate the alt text for the image URLs and uploads",
    },
}

PREFERRED_LLM = "gpt-4o"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thanks for using the Alt Text Generator service"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "Alt Text Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded",
}

SIDEBAR_HIDDEN = True

# Import necessary libraries
import streamlit as st

# Helper function to build the prompt
def build_prompt(system_prompt, urls, files, important_text, complex_image):
    """Constructs a dynamic prompt based on user input."""
    prompt = system_prompt + "\n\n"
    if urls:
        prompt += f"URLs provided: {', '.join(urls)}\n"
    if files:
        prompt += f"Uploaded files: {', '.join(files)}\n"

    if complex_image:
        prompt += (
            "I am sending you one or more complex images. Please provide a short description "
            "of the most important concept depicted in the image; and a long description to explain "
            "the relationship between components to provide a detailed and informative description of the image.\n"
        )
    else:
        prompt += (
            "I am sending you one or more images. Please provide separate appropriate alt text for each image I send. "
            "The alt text should describe the most important concept displayed in the image in less than 120 characters.\n"
        )

    if important_text:
        prompt += "Transcribe text verbatim to provide a detailed and informative description of the image.\n"

    return prompt.strip()


# Main application logic
def main(config):
    st.set_page_config(**config["PAGE_CONFIG"])

    # Title and Introduction
    st.title(config["APP_TITLE"])
    st.markdown(config["APP_INTRO"])
    st.markdown(config["APP_HOW_IT_WORKS"])

    # Sidebar for advanced settings
    with st.sidebar:
        st.title("Advanced Settings")
        system_prompt = st.text_area(
            "Edit System Prompt", value=config["SYSTEM_PROMPT"], height=150
        )

    # Phase 1: Image Input
    st.subheader(config["PHASES"]["phase1"]["name"])
    st.write(config["PHASES"]["phase1"]["phase_instructions"])

    # Collect input fields
    urls = st.text_area(
        config["PHASES"]["phase1"]["fields"]["http_img_urls"]["label"]
    ).splitlines()
    uploaded_files = st.file_uploader(
        config["PHASES"]["phase1"]["fields"]["uploaded_files"]["label"],
        type=config["PHASES"]["phase1"]["fields"]["uploaded_files"]["allowed_files"],
        accept_multiple_files=True,
    )
    important_text = st.checkbox(
        config["PHASES"]["phase1"]["fields"]["important_text"]["label"],
        value=config["PHASES"]["phase1"]["fields"]["important_text"]["value"],
        help=config["PHASES"]["phase1"]["fields"]["important_text"]["help"],
    )
    complex_image = st.checkbox(
        config["PHASES"]["phase1"]["fields"]["complex_image"]["label"],
        value=config["PHASES"]["phase1"]["fields"]["complex_image"]["value"],
        help=config["PHASES"]["phase1"]["fields"]["complex_image"]["help"],
    )


# Run the app
if __name__ == "__main__":
    main(config=globals())
