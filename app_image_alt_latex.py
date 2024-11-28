# App Configuration
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

SYSTEM_PROMPT = """
You accept images in URL and file format containing mathematical equations, symbols, and text 
into accurate and you convert the images into properly formatted LaTeX code. 
Output: Provide the final LaTeX code in a format that can be easily copied or exported.
"""

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
                - convert the images into properly formatted LaTeX code exactly as it appears (verbatim)""",
                "condition": True  # Default condition for execution
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

# Core Logic Fixes
def evaluate_conditions(user_input, condition):
    """
    Evaluate the given condition based on user_input.
    Returns True or False based on the logic of the condition.
    """
    return condition  # Simplified for this context; customize as needed.

def prompt_conditionals(user_input, phase_name, phases):
    """
    Generate a prompt based on conditionals within the given phase.
    """
    phase = phases.get(phase_name, {})
    additional_prompts = []

    for item in phase.get("user_prompt", []):
        condition_clause = item.get("condition", True)  # Default to True if 'condition' is missing
        if evaluate_conditions(user_input, condition_clause):
            additional_prompts.append(item["prompt"])

    return "\n".join(additional_prompts)

def format_user_prompt(user_input, phase_name, phases):
    """
    Format the user prompt by substituting variables in the base prompt.
    """
    try:
        prompt = prompt_conditionals(user_input, phase_name, phases)

        if isinstance(prompt, str):
            return prompt.format(**user_input)  # Format string
        elif isinstance(prompt, list):
            return "\n".join([p.format(**user_input) for p in prompt])  # Handle list of strings
        else:
            raise ValueError("Unexpected prompt type")

    except Exception as e:
        print(f"Error occurred in format_user_prompt: {e}")
        return ""

# Streamlit App Logic
from core_logic.main import main

if __name__ == "__main__":
    main(config=globals())
