APP_URL = "https://example.com/app"  # Example URL
APP_IMAGE = "https://example.com/default_image.png"  # Example default image
PREFERRED_LLM = "gpt-4o"  # Matching preferred LLM

# Updated System Prompt to include both LaTeX and alt text generation
SYSTEM_PROMPT = (
    "You accept images in URL and file formats containing mathematical equations, symbols, "
    "and text. You can generate two outputs for each image: "
    "- (1) Accurate and properly formatted LaTeX code. "
    "- (2) Alt text describing the image content. "
    "Output: Provide both outputs for each image in a user-friendly format."
)

# Updated PHASES to handle conditions and dynamic prompts
PHASES = {
    "phase1": {
        "name": "Image Input and Output Generation",
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
        "phase_instructions": "Generate LaTeX code and/or alt text for the image URLs and uploads.",
        "user_prompts": [
            {
                "condition": {"important_text": False, "complex_image": False},
                "prompt": (
                    "I am sending you one or more images. Please provide both: "
                    "- Properly formatted LaTeX code for mathematical elements."
                    "- Alt text describing the image."
                )
            },
            {
                "condition": {"complex_image": True},
                "prompt": (
                    "I am sending you one or more complex images. Please provide: "
                    "- Properly formatted LaTeX code for the image content."
                    "- A detailed alt text description of the image."
                )
            },
            {
                "condition": {"important_text": True, "complex_image": True},
                "prompt": (
                    "I am sending you one or more important and complex images. Please provide: "
                    "- Detailed LaTeX code for mathematical elements. "
                    "- A detailed alt text description, focusing on important textual information."
                )
            }
        ],
        "show_prompt": True,
        "allow_skip": False,
    }
}

# Adding temperature hyperparameter and other LLM overrides
LLM_CONFIG_OVERRIDE = {
    "temperature": 0.2,
    "top_p": 0.9
}

PAGE_CONFIG = {
    "page_title": "LaTeX and Alt Text Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

# Verify module import
try:
    from core_logic.main import main
except ImportError as e:
    raise ImportError("Ensure 'core_logic.main' is available.") from e

if __name__ == "__main__":
    config = {
        "APP_URL": APP_URL,
        "APP_IMAGE": APP_IMAGE,
        "PREFERRED_LLM": PREFERRED_LLM,
        "PHASES": PHASES,
        "SYSTEM_PROMPT": SYSTEM_PROMPT,
        "LLM_CONFIG_OVERRIDE": LLM_CONFIG_OVERRIDE,
        "PAGE_CONFIG": PAGE_CONFIG,
    }
    main(config=config)
