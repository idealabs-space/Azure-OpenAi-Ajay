import streamlit as st
import requests

# Streamlit app title
st.title("Azure OpenAI Chatbot")

# Correctly access secrets
endpoint_url = st.secrets["AZURE_OPENAI_ENDPOINT"]
api_key = st.secrets["AZURE_OPENAI_API_KEY"]

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Create two main layout sections
response_container = st.container()
input_container = st.container()

# Function to display chat history in the response container
def display_chat():
    with response_container:
        st.markdown("### Chat History")
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**You:** {message['content']}")
            else:
                st.markdown(f"**Bot:** {message['content']}")

# Handle user input and API interaction within a form
with input_container:
    # Use st.form to capture user input and allow Enter to submit
    with st.form(key="chat_form"):
        user_message = st.text_input("Enter your message:", key="user_input", label_visibility="collapsed")
        submit_button = st.form_submit_button("Send")

        if submit_button and user_message.strip():
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_message})

            # Prepare request headers and payload
            headers = {
                "Content-Type": "application/json",
            }
            data = {
                "model": "<deployment-name>",  # Replace with your model's deployment name
                "messages": [
                    {"role": "system", "content": "You are a detailed and helpful assistant. Provide complete and elaborate answers."}
                ] + st.session_state.chat_history,
                "max_tokens": 1000,
                "temperature": 0.7,
                "top_p": 1.0,
                "frequency_penalty": 0.5,
                "presence_penalty": 0.6
            }
            params = {
                "api-key": api_key
            }

            # Make the API request
            response = requests.post(endpoint_url, headers=headers, json=data, params=params)

            # Handle the response
            if response.status_code == 200:
                response_json = response.json()
                bot_message = response_json['choices'][0]['message']['content'].strip()
                st.session_state.chat_history.append({"role": "assistant", "content": bot_message})
            else:
                st.error(f"Error: {response.status_code}")
                st.error(response.text)

# Always display the chat history
display_chat()
