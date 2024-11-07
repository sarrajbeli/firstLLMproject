import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key

# Configure OpenAI API
genai.configure(api_key=google_gemini_api_key)

# Generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Set app to wide mode
st.set_page_config(layout="wide")

# Title for the app
st.title('My first LLM Project, BlogBuddy: Your AI Writing Companion')

# Create a subheader
st.subheader('Now you can craft perfect blogs with the help of AI - BlogBuddy is your new AI Blog Companion')

# SideBar for the user input
with st.sidebar:
    st.title('Input your blog details')
    st.header('Enter details for the blog you want to generate')

    # Blog title from the user
    blog_title = st.text_input('Blog Title')

    # Keywords input
    keywords = st.text_area("Keywords (comma separated)")

    # Number of words
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=100)

    # Number of images
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)

    # Submit button
    submit_button = st.button("Generate Blog")

# If submit button is pressed
if submit_button:
    # Build prompt parts based on user inputs
    prompt_text = (
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keywords}\"."
        f" Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length,"
        " suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout."
    )

    # Start chat session and send message with prompt_text
    chat_session = model.start_chat(history=[{"role": "user", "parts": [prompt_text]}])

    response = chat_session.send_message(prompt_text)  # Pass prompt_text as content

    # Display the response in Streamlit
    if response and response.text:
        st.write(response.text)
    else:
        st.write("An error occurred. Please try again.")
