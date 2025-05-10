# restaurant_generator.py
import streamlit as st
import cohere

# Set your Cohere API key
COHERE_API_KEY = "39R6tqfDIiW73u01tcIlFzE0QRnI9Of4DZu26ZNm"

# Initialize Cohere
co = cohere.Client(COHERE_API_KEY)

st.title("🍽️ Restaurant Name & Menu Generator")

# Cuisine selector
cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

def generate_restaurant_name_and_items(cuisine_type):
    prompt = f"""
    You are a creative assistant. Generate a unique restaurant name and a list of 5 popular menu items based on the cuisine: {cuisine_type}.

    Return the response in this format:
    Restaurant Name: <name>
    Menu: <item1>, <item2>, <item3>, <item4>, <item5>
    """

    response = co.chat(
        model="command-r",
        message=prompt,
        temperature=0.8,
        max_tokens=200
    )

    return response.text.strip()

if cuisine:
    output = generate_restaurant_name_and_items(cuisine)

    # Split the output
    if "Restaurant Name:" in output and "Menu:" in output:
        name_part = output.split("Menu:")[0].replace("Restaurant Name:", "").strip()
        menu_part = output.split("Menu:")[1].strip().split(",")
        
        st.header(name_part)
        st.write("**Menu Items**")
        for item in menu_part:
            st.write("-", item.strip())
    else:
        st.error("Unexpected response format from Cohere.")
