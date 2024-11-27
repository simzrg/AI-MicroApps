import streamlit as st

APP_URL = "https://example.com/app"  # Example URL
APP_IMAGE = "https://example.com/default_image.png"  # Example default image
PREFERRED_LLM = "gpt-4o"  # Matching preferred LLM

# Updated System Prompt to include both LaTeX and alt text generation
SYSTEM_PROMPT = (
    "You accept images in URL and file formats containing mathematical equations, symbols, "
    "and text. You can generate three outputs for each image: "
    "- (1) Accurate and properly formatted LaTeX code. "
    "- (2) Alt text describing the image content (for simple images). "
    "- (3) An accessible visual transcript for complex images. "
    "Output: Provide these outputs in a user-friendly format, depending on the image type."
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
        "phase_instructions": (
            "Provide the necessary outputs for each image. "
            "- For simple images, generate LaTeX code and alt text. "
            "- For complex images, generate LaTeX code and an accessible visual transcript."
        ),
        "user_prompts": [
            {
                "condition": {"is_complex": False},
                "prompt": (
                    "I am sending you one or more images. Please provide both: "
                    "- Properly formatted LaTeX code for mathematical elements. "
                    "- Alt text describing the image content."
                )
            },
            {
                "condition": {"is_complex": True},
                "prompt": (
                    "I am sending you one or more complex images. Please provide: "
                    "- Properly formatted LaTeX code for the image content. "
                    "- An accessible visual transcript describing the image in detail."
                )
            }
        ],
        "show_prompt": True,
        "allow_skip": False,
    }
}

# Adding temperature hyperparameter and other LLM overrides
LLM_CONFIG_OVERRIDE = {
    "temperature": 0.2,  # Ensures deterministic output for accurate results
    "top_p": 0.9        # Balances diversity and relevance
}

PAGE_CONFIG = {
    "page_title": "LaTeX and Accessible Transcript Generator",
    "page_icon": "🖼️",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
}

# Main App Logic
def main():
    st.set_page_config(**PAGE_CONFIG)

    # Display System Prompt Section
    st.header("System Prompt")
    st.text_area("View/Edit System Prompt:", value=SYSTEM_PROMPT, height=200)

    # Image Input and Complexity Check
    st.header("Image Input and Output Generation")
    uploaded_files = st.file_uploader("Upload images", type=["png", "jpeg", "gif", "webp"], accept_multiple_files=True)

    # Checkbox for Complex Image
    is_complex = st.checkbox("Check if these images are complex")

    if uploaded_files:
        for file in uploaded_files:
            st.image(file, caption=f"Preview of {file.name}")
            if is_complex:
                st.info(f"Processing {file.name} as a complex image...")
                st.text_area(f"Accessible Transcript for {file.name}:", value="Generating detailed transcript...")
            else:
                st.info(f"Processing {file.name} as a simple image...")
                st.text_area(f"LaTeX and Alt Text for {file.name}:", value="Generating concise outputs...")

    # Restart Button
    if st.button("Restart"):
        st.experimental_rerun()

# Run the app
if __name__ == "__main__":
    main()
