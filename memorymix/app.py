import streamlit as st
from components.recording import show_recording_interface
from components.document_processing import show_document_interface
from components.study_session import show_study_interface
from components.review import show_review_interface

def main():
    st.set_page_config(
        page_title="MemoryMix - Smart Study Assistant",
        page_icon="📚",
        layout="wide"
    )

    st.title("MemoryMix - Smart Study Assistant")

    # Sidebar navigation
    mode = st.sidebar.selectbox(
        "Select Mode",
        ["Lecture Recording", "Document Processing", "Study Session", "Review & Quiz"]
    )

    # Main content area based on selected mode
    if mode == "Lecture Recording":
        show_recording_interface()
    elif mode == "Document Processing":
        show_document_interface()
    elif mode == "Study Session":
        show_study_interface()
    else:
        show_review_interface()

if __name__ == "__main__":
    main()