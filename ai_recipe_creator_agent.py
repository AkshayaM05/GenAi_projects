import cohere
import os

# Initialize Cohere client with your API key
co = cohere.Client('39R6tqfDIiW73u01tcIlFzE0QRnI9Of4DZu26ZNm')  # Replace with your actual API key

# Define your input ingredients
ingredients = "chicken, garlic, and tomatoes"

# Create a message prompt
message = f"Create a detailed cooking recipe using the following ingredients: {ingredients}"

# Use the chat API (correct for 'command-r')
response = co.chat(
    model='command-r',
    message=message
)

# Print the generated recipe
print("Recipe:\n")
print(response.text.strip())
