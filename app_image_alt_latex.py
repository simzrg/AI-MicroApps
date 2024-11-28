import streamlit as st

APP_URL = ""  # TODO: Add URL for the app
APP_IMAGE = ""  # TODO: Add default image for the app
PUBLISHED = False  # Status of the app

APP_TITLE = "LaTeX Generator"
APP_INTRO = "This app accepts images via upload or URL and returns LaTeX code."

APP_HOW_IT_WORKS = """
This app creates LaTeX code from images. 
For most images, it provides properly formatted LaTeX code, along with options for alt text and visual transcripts.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = "You accept images in URL and file format containing mathematical equations, symbols, and text into accurate and you convert the images into properly formatted LaTeX code. Output: Provide the final LaTeX code in a format that can be easily copied or exported."

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
                "label": "Upload images",
                "allowed_files": ['png', 'jpeg', 'gif', 'webp'],
                "multiple_files": True,
            },
            "latex_choice": {
                "type": "checkbox",
                "label": "Generate LaTeX",
                "default": True
            },
            "alt_text_choice": {
                "type": "checkbox",
                "label": "Generate Alt Text",
                "default": True
            },
            "visual_transcript_choice": {
                "type": "checkbox",
                "label": "Generate Visual Transcript",
                "default": False
            },
            "advanced_settings": {
                "type": "text_area",
                "label": "Edit System Prompt (Optional)",
                "default": SYSTEM_PROMPT,
                "hidden": False
            },
        },
        "phase_instructions": "Provide the images through URL or upload and configure your options below.",
        "user_prompt": [
            {
                "condition": True,  # Default condition
                "prompt": """I am sending you one or more app_images. Please provide separate LaTeX code, alt text, and/or visual transcript for each image I send based on the selected options. The LaTeX code should:
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

COMPLETION_MESSAGE = "Thank you for using the LaTeX Generator service!"
COMPLETION_CELEBRATION = False

PAGE_CONFIG = {
    "page_title": "LaTeX Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_HIDDEN = True

# Render Functions
def render_text_area(config):
    """Renders a text area in Streamlit."""
    return st.text_area(
        label=config.get("label", "Enter text"),
        value=config.get("default", ""),
        height=config.get("height", 150),
    )

def render_file_uploader(config):
    """Renders a file uploader in Streamlit."""
    return st.file_uploader(
        label=config.get("label", "Upload file(s)"),
        type=config.get("allowed_files", None),
        accept_multiple_files=config.get("multiple_files", False),
    )

def render_button(config):
    """Renders a button in Streamlit."""
    return st.button(
        label=config.get("label", "Submit"),
    )

def render_select(config):
    """Renders a dropdown menu in Streamlit."""
    return st.selectbox(
        label=config.get("label", "Select an option"),
        options=config.get("options", []),
        index=config.get("default_index", 0),
    )

# Mapping for field types to rendering functions
function_map = {
    "text_area": render_text_area,
    "file_uploader": render_file_uploader,
    "button": render_button,
    "select": render_select,
}

def prompt_conditionals(user_input, phase_name, phases):
    phase = phases.get(phase_name, {})
    additional_prompts = []
    for item in phase.get("user_prompt", []):
        condition_clause = item.get("condition", True)  # Default to True if condition is missing
        if condition_clause:  # Evaluate or use default True
            additional_prompts.append(item["prompt"])
    return "\n".join(additional_prompts)

def format_user_prompt(prompt, user_input):
    try:
        if isinstance(prompt, list):
            prompt = "\n".join(prompt)  # Convert list to string
        formatted_user_prompt = prompt.format(**user_input)
        return formatted_user_prompt
    except Exception as e:
        print(f"Error occurred in format_user_prompt: {e}")
        return prompt  # Fallback to raw prompt

from core_logic.main import main
if __name__ == "__main__":
    st.set_page_config(
        page_title=PAGE_CONFIG["page_title"],
        page_icon=PAGE_CONFIG["page_icon"],
        layout=PAGE_CONFIG["layout"],
        initial_sidebar_state=PAGE_CONFIG["initial_sidebar_state"],
    )
    main(config=globals())
