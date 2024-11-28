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

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
