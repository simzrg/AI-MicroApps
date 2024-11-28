import streamlit as st

# Ensure page configuration is applied once and first
st.set_page_config(
    page_title="LaTeX Generator",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

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

SIDEBAR_HIDDEN = True

# Render Functions
def render_text_area(config):
    return st.text_area(
        label=config.get("label", "Enter text"),
        value=config.get("default", ""),
        height=config.get("height", 150),
    )

def render_file_uploader(config):
    return st.file_uploader(
        label=config.get("label", "Upload file(s)"),
        type=config.get("allowed_files", None),
        accept_multiple_files=config.get("multiple_files", False),
    )

def render_button(config):
    return st.button(
        label=config.get("label", "Submit"),
    )

def render_select(config):
    return st.selectbox(
        label=config.get("label", "Select an option"),
        options=config.get("options", []),
        index=config.get("default_index", 0),
    )

# Map field types to render functions
function_map = {
    "text_area": render_text_area,
    "file_uploader": render_file_uploader,
    "button": render_button,
    "select": render_select,
}

# Evaluate conditions for prompt filtering
def evaluate_conditions(user_input, condition):
    """
    Evaluates whether the 'user_input' meets the specified 'condition'.
    Supports logical operators like $and, $or, $not, and comparison operators.
    """
    if isinstance(condition, bool):  # Handle simple boolean conditions
        return condition

    if isinstance(condition, dict):  # Handle logical operators
        if "$and" in condition:
            return all(evaluate_conditions(user_input, sub_condition) for sub_condition in condition["$and"])
        elif "$or" in condition:
            return any(evaluate_conditions(user_input, sub_condition) for sub_condition in condition["$or"])
        elif "$not" in condition:
            return not evaluate_conditions(user_input, condition["$not"])

    # If condition is not recognized, raise an error
    raise ValueError(f"Unknown condition type: {condition}")

def prompt_conditionals(user_input, phase_name, phases):
    """
    Returns prompts based on the conditions defined in the phase configuration.
    """
    phase = phases.get(phase_name, {})
    additional_prompts = []

    for item in phase.get("user_prompt", []):
        condition_clause = item.get("condition", True)  # Default to True if condition is missing
        if evaluate_conditions(user_input, condition_clause):
            additional_prompts.append(item["prompt"])

    # Join all prompts into a single string
    return "\n".join(additional_prompts)

def format_user_prompt(prompt, user_input):
    """
    Formats the prompt with user input. Handles list-to-string conversion.
    """
    try:
        if isinstance(prompt, list):  # Convert list to a single string
            prompt = "\n".join(prompt)

        formatted_user_prompt = prompt.format(**user_input)
        return formatted_user_prompt
    except Exception as e:
        st.error(f"Error occurred in format_user_prompt: {e}")
        return prompt  # Return the raw prompt as a fallback

from core_logic.main import main

if __name__ == "__main__":
    main(config=globals())
