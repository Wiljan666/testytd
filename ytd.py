import streamlit as st
from pytube import YouTube
import os
import shutil
from pathlib import Path

def download_audio(url):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        st.text("Downloading audio...")
        output_path = Path.home() / "Music" / yt.title  # Het pad naar de "Muziek" map met de naam van de YouTube-video
        output_path.mkdir(parents=True, exist_ok=True)
        audio.download(output_path=output_path)
        st.text("Audio downloaded successfully.")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

def main():
    st.title("YouTube Audio Downloader")
    url = st.text_input("Enter YouTube video URL:")
    if st.button("Download Audio"):
        if url:
            download_audio(url)

if __name__ == "__main__":
    main()
