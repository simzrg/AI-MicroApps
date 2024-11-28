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

SYSTEM_PROMPT = "You accept images in URL and file format containing mathematical equations, symbols, and text into accurate and you convert the images into properly formatted LaTeX code. Output: Provide the final LaTeX code in a format that can be easily copied or exported."

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
            "latex_input": {
                "type": "text_area",
                "label": "Enter custom LaTeX (optional)",
            },
            "alt_text": {
                "type": "text_area",
                "label": "Enter alt text for the image (optional)",
            },
            "visual_transcript": {
                "type": "select",
                "label": "Include visual transcript?",
                "options": ["Yes", "No"],
            },
        },
        "phase_instructions": "Provide image URLs or upload files, and optionally add custom LaTeX, alt text, or select visual transcript options.",
        "user_prompt": [
            {
                "prompt": """I am sending you one or more images. Please provide separate LaTeX code for each image I send. The LaTeX code should:
                - Convert the images into properly formatted LaTeX code.
                - Include any custom LaTeX provided by the user.
                - Attach alt text and/or visual transcripts if specified."""
            }
        ],
        "show_prompt": True,
        "allow_skip": False,
    }
}

ADVANCED_SETTINGS = {
    "type": "accordion",
    "label": "Advanced Settings",
    "content": {
        "system_prompt": {
            "type": "text_area",
            "label": "View/Edit System Prompt",
            "default": SYSTEM_PROMPT,
        }
    }
}

BUTTONS = {
    "submit": {
        "type": "button",
        "label": "Submit",
        "action": "submit_form",
    },
    "restart": {
        "type": "button",
        "label": "Restart",
        "action": "restart_app",
    },
    "exit": {
        "type": "button",
        "label": "Exit",
        "action": "exit_app",
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
    "initial_sidebar_state": "expanded",
}

SIDEBAR_HIDDEN = True

from core_logic.main import main

if __name__ == "__main__":
    main(config=globals())
