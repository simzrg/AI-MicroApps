import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="LaTeX Generator",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Constants
APP_TITLE = "LaTeX Generator"
APP_INTRO = (
    "This app accepts images via URL or upload and generates LaTeX code, "
    "alt text, and visual transcripts based on your selections."
)
DEFAULT_PROMPT = (
    "You accept images in URL and file format containing mathematical equations, "
    "symbols, and text, converting them into properly formatted LaTeX code. "
    "Output: Provide the final LaTeX code in a format that can be easily copied or exported."
)

# Sidebar for advanced settings
with st.sidebar:
    st.title("Advanced Settings")
    system_prompt = st.text_area(
        label="Edit System Prompt (Optional)",
        value=DEFAULT_PROMPT,
        height=150,
    )

# App header
st.title(APP_TITLE)
st.markdown(APP_INTRO)

# Input Section
st.subheader("Image Input")
image_url = st.text_input("Enter Image URL")
uploaded_files = st.file_uploader(
    "Upload Images",
    type=["png", "jpeg", "jpg", "gif", "webp"],
    accept_multiple_files=True,
)

# Options Section
st.subheader("Output Options")
generate_latex = st.checkbox("Generate LaTeX Code", value=True)
generate_alt_text = st.checkbox("Generate Alt Text", value=True)
generate_visual_transcript = st.checkbox("Generate Visual Transcript", value=False)

# Submit Button
if st.button("Submit"):
    # Validate inputs
    if not image_url and not uploaded_files:
        st.error("Please provide at least one image URL or upload an image.")
    else:
        st.success("Processing your request...")
        
        # Display the inputs for debugging or visualization
        st.write("### Input Details:")
        if image_url:
            st.write(f"Image URL: {image_url}")
        if uploaded_files:
            st.write(f"Uploaded Files: {[file.name for file in uploaded_files]}")

        # Display selected options
        st.write("### Selected Options:")
        st.write(f"- Generate LaTeX: {generate_latex}")
        st.write(f"- Generate Alt Text: {generate_alt_text}")
        st.write(f"- Generate Visual Transcript: {generate_visual_transcript}")

        # Display the system prompt
        st.write("### System Prompt:")
        st.code(system_prompt)

        # Placeholder for processing logic
        st.write("### Results:")
        if generate_latex:
            st.write("LaTeX code generation result (placeholder).")
        if generate_alt_text:
            st.write("Alt text generation result (placeholder).")
        if generate_visual_transcript:
            st.write("Visual transcript generation result (placeholder).")

        # Example for visualizing uploaded images (if any)
        if uploaded_files:
            st.write("### Uploaded Images:")
            for uploaded_file in uploaded_files:
                st.image(uploaded_file, caption=uploaded_file.name)

