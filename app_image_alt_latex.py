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
APP_INTRO = "This app accepts images via URL or upload and generates LaTeX code, alt text, and visual transcripts."
SYSTEM_PROMPT = (
    "You accept images in URL and file format containing mathematical equations, "
    "symbols, and text, converting them into properly formatted LaTeX code. "
    "Output: Provide the final LaTeX code in a format that can be easily copied or exported."
)

# Sidebar
with st.sidebar:
    st.title("Advanced Settings")
    advanced_prompt = st.text_area(
        label="Edit System Prompt (Optional)",
        value=SYSTEM_PROMPT,
        height=150
    )

# App Header
st.title(APP_TITLE)
st.markdown(APP_INTRO)

# Input Section
st.subheader("Input Image")
image_url = st.text_input("Enter Image URL")
uploaded_files = st.file_uploader(
    "Upload Images",
    type=['png', 'jpeg', 'jpg', 'gif', 'webp'],
    accept_multiple_files=True
)

# Options Section
st.subheader("Options")
generate_latex = st.checkbox("Generate LaTeX Code", value=True)
generate_alt_text = st.checkbox("Generate Alt Text", value=True)
generate_visual_transcript = st.checkbox("Generate Visual Transcript", value=False)

# Submit Button
if st.button("Submit"):
    # Check inputs and display results
    if not image_url and not uploaded_files:
        st.error("Please provide at least one image URL or upload an image.")
    else:
        st.success("Processing your request...")
        st.write("### Selected Options:")
        st.write(f"- Generate LaTeX: {generate_latex}")
        st.write(f"- Generate Alt Text: {generate_alt_text}")
        st.write(f"- Generate Visual Transcript: {generate_visual_transcript}")
        st.write("### Advanced Prompt:")
        st.code(advanced_prompt)
        # Here you would process the inputs and generate outputs
        # Placeholder for the actual LaTeX, alt text, and transcript generation logic
        st.write("### Results (Placeholder):")
        st.write("LaTeX code and other outputs will be displayed here.")

