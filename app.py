import streamlit as st
from pathlib import Path

# ----------------------------
# Streamlit Page Configuration
# ----------------------------
st.set_page_config(
    page_title="🎵 Music Player",
    page_icon="🎧",
    layout="centered"
)

# ----------------------------
# App Title and Description
# ----------------------------
st.title("🎶 Simple Music Player App")
st.markdown("Upload and play your favorite **MP3** songs right here!")

# ----------------------------
# File Upload Section
# ----------------------------
uploaded_file = st.file_uploader("🎵 Upload an MP3 file", type=["mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    music_path = Path("uploaded_music.mp3")
    with open(music_path, "wb") as f:
        f.write(uploaded_file.read())

    # Show success message
    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    # Display the audio player
    st.audio(str(music_path))

else:
    st.info("Please upload an MP3 file to start playing music 🎧")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("🎧 Created with ❤️ using Streamlit and Python")
