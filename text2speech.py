from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import streamlit as st
import os

st.title("🗣️ Text to Video Generator (gTTS + Image)")

text_input = st.text_input("Enter text to convert into video:")

if st.button("🎬 Generate Video"):
    if text_input.strip():
        # Step 1: Convert text to speech
        tts = gTTS(text_input)
        tts.save("output.mp3")
        
        # Step 2: Prepare background image
        image_path = "avatar.jpg"  # Make sure this file exists in your working directory
        if not os.path.exists(image_path):
            st.error("Missing 'avatar.jpg' image file in your directory.")
        else:
            # Step 3: Create video with MoviePy
            audio_clip = AudioFileClip("output.mp3")
            image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
            image_clip = image_clip.set_audio(audio_clip).resize(height=480)

            video_path = "output.mp4"
            image_clip.write_videofile(video_path, fps=24)

            # Step 4: Display video in Streamlit
            st.success("✅ Video generated successfully!")
            st.video(video_path)
    else:
        st.warning("Please enter some text.")
