import streamlit as st
import requests
import time

# Replace this with your actual API key from https://studio.d-id.com/
API_KEY = "YWtzaGF5YW12MjAwNUBnbWFpbC5jb20:M6q4wDFsBR5eTDmHlbPXC"

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Default avatar image (public D-ID-supported URL)
AVATAR_IMAGE_URL = "https://create-images-results.d-id.com/DefaultMale/DefaultMale.jpg"

st.title("🗣️ Text to Talking Avatar Video")

# Input field for text
text_input = st.text_area("Enter the text you want the avatar to speak:", height=100)

# Button to trigger video generation
if st.button("🎬 Generate Video"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Generating video, please wait..."):
            payload = {
                "script": {
                    "type": "text",
                    "input": text_input,
                    "provider": {
                        "type": "microsoft",
                        "voice_id": "en-US-JennyNeural"
                    },
                    "ssml": False
                },
                "source_url": AVATAR_IMAGE_URL
            }

            # Step 1: Start the video generation
            response = requests.post("https://api.d-id.com/talks", json=payload, headers=HEADERS)

            if response.status_code == 200:
                talk_id = response.json().get("id")

                # Step 2: Poll until the video is ready
                status_url = f"https://api.d-id.com/talks/{talk_id}"
                for _ in range(30):
                    status_response = requests.get(status_url, headers=HEADERS)
                    status_data = status_response.json()
                    if "result_url" in status_data:
                        st.success("✅ Video is ready!")
                        st.video(status_data["result_url"])
                        break
                    time.sleep(2)
                else:
                    st.error("⚠️ Video generation timed out.")
            else:
                st.error(f"❌ Video generation failed. Error: {response.text}")
