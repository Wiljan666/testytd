import streamlit as st
from pytube import YouTube
import os

def download_audio(url, output_path):
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        st.text("Downloading audio...")
        audio.download(output_path=output_path)
        st.text("Audio downloaded successfully.")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

def main():
    st.title("YouTube Audio Downloader")
    url = st.text_input("Enter YouTube video URL:")
    if st.button("Download Audio"):
        if url:
            download_dir = "muziek"  # Hier wordt de map "muziek" gebruikt om de audiobestanden op te slaan
            os.makedirs(download_dir, exist_ok=True)
            download_audio(url, download_dir)

if __name__ == "__main__":
    main()
