import streamlit as st
import os

# Use relative path or point to the uploaded file
wiki_file_path = 'assets/2019-12-11_MachineVision%2Bcpjobqueue.wikitext'  # Adjusted path

# Function to load the file content
def load_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return None

# Function to parse the sections
def parse_sections(content):
    sections = {}
    current_section = None
    current_content = []

    for line in content.splitlines():
        line = line.strip()
        if line.startswith("==") and line.endswith("=="):
            if current_section:
                sections[current_section] = "\n".join(current_content).strip()
            current_section = line.strip("=").strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = "\n".join(current_content).strip()

    return sections

# Load file content
file_content = load_file(wiki_file_path)

# Streamlit App
st.title("Intelligent Document Analysis Tool")

if file_content:
    sections = parse_sections(file_content)

    # Sidebar navigation with a collapsible section
    with st.sidebar.expander("Choose a Section", expanded=True):
        selected_section = st.selectbox("Sections", list(sections.keys()))

    # Display selected section content
    if selected_section:
        st.header(selected_section)
        st.write(sections[selected_section])
else:
    st.error(f"File not found at {wiki_file_path}. Please check the path.")
