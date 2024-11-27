APP_URL = "" # TODO: Add URL for the app
APP_IMAGE = "" # TODO: Add default image for the app
PUBLISHED = False # Status of the app

APP_TITLE = "LaTex Generator"
APP_INTRO = "This app accepts images via upload or URL and returns LaTeX code."

APP_HOW_IT_WORKS = """
This app creates LaTeX code from images. 
                For most images, it provides properly formated LaTeX code.
 """

SHARED_ASSET = {
}

HTML_BUTTON = {

}

SYSTEM_PROMPT = "You accept images in url and file format containing mathematical equations, symbols, and text into accurate and you convert the images into properly formatted LaTeX code. Output: Provide the final LaTeX code in a format that can be easily copied or exported."

PHASES = {
    "phase1": {
        "name": "Image Input and LaTeX Generation",
        "fields": {
            "http_img_urls": {
                "type": "text_area",
                "label": "Enter image urls"
            },
            "uploaded_files": {
                "type": "file_uploader",
                "label": "Choose files",
                "allowed_files": ['png', 'jpeg', 'gif', 'webp'],
                "multiple_files": True,
            },
        },
       "phase_instructions": "Generate LaTeX for the image urls and uploads",

        "user_prompt": [
            {
                "prompt": """I am sending you one or more app_images. Please provide separate LaTeX code for each image I send. The LaTeX code should:
                - convert the images into properly formatted LaTeX code"""
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

from core_logic.main import main
if __name__ == "__main__":
    main(config=globals())
