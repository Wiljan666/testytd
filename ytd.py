import streamlit as st
from pytube import YouTube
import os

def main():
    path = st.text_input('Enter URL of any YouTube video')
    option = st.selectbox(
        'Select type of download',
        ('audio', 'highest_resolution', 'lowest_resolution'))

    if st.button("Download"):
        video_object = YouTube(path)
        st.write("Title of Video: " + str(video_object.title))
        st.write("Number of Views: " + str(video_object.views))

        download_dir = os.path.expanduser("~") + "\\Downloads"  # Het pad naar de "Downloads" map in Windows

        if option == 'audio':
            audio = video_object.streams.get_audio_only()
            audio.download(output_path=download_dir)
        elif option == 'highest_resolution':
            video = video_object.streams.get_highest_resolution()
            video.download(output_path=download_dir)
        elif option == 'lowest_resolution':
            video = video_object.streams.get_lowest_resolution()
            video.download(output_path=download_dir)

    if st.button("View"):
        st.video(path)

if __name__ == '__main__':
    main()
