**Azure OpenAI Chatbot**
________________________________________
Overview

This repository contains the implementation of a chatbot using Streamlit and Azure OpenAI services. The chatbot enables users to interact with an AI model by sending messages and receiving detailed, context-aware responses. The application leverages the Azure OpenAI API to process user inputs and generate responses.
Features
•	User-friendly Streamlit interface.
•	Persistent chat history within a session.
•	Integration with Azure OpenAI for intelligent responses.
•	Configurable parameters like temperature, top_p, and penalties for fine-tuning response generation.
________________________________________
Getting Started
Prerequisites
1.	Python: Ensure Python 3.7 or higher is installed.
2.	Azure OpenAI API Key and Endpoint: Obtain the API key and endpoint URL from your Azure OpenAI resource.
3.	Environment Variables: Install the python-dotenv library to securely manage sensitive credentials.
Installation
1.	Clone the repository:
2.	git clone https://github.com/your-username/azure-openai-chatbot.git
cd azure-openai-chatbot
3.	Create and activate a virtual environment:
4.	python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
5.	Install dependencies:
pip install -r requirements.txt
6.	Create a .env file for environment variables:
touch .env
Add your Azure credentials in the .env file:
AZURE_OPENAI_ENDPOINT=<Your Endpoint URL>
AZURE_OPENAI_API_KEY=<Your API Key>
7.	Add your deployment name in the code: Replace <deployment-name> in the data dictionary with the name of your Azure OpenAI model deployment.
________________________________________
Usage
Running the Application
1.	Start the Streamlit app:
streamlit run app.py
2.	Open the provided URL in your browser (typically http://localhost:8501).
3.	Interact with the chatbot by entering your messages in the input box and clicking "Send."
Application Structure
•	st.title: Sets the title of the app.
•	Chat History: Displays the ongoing conversation between the user and the chatbot.
•	Input Form: Accepts user input and sends it to the Azure OpenAI API.
________________________________________
Code Explanation
Key Components
1.	Environment Variable Management The dotenv library is used to load sensitive credentials from the .env file.
2.	from dotenv import load_dotenv
load_dotenv()
3.	Streamlit Session State Stores the chat history for persistence during the session.
4.	if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
5.	Azure OpenAI Integration Makes POST requests to the Azure OpenAI API with user input and configuration settings.
response = requests.post(endpoint_url, headers=headers, json=data, params=params)
6.	Chat History Display Displays the conversation in a user-friendly format using Markdown.
st.markdown(f"**You:** {message['content']}")
________________________________________
Configuration
The API request payload includes several tunable parameters:
•	model: Name of the Azure OpenAI deployment.
•	max_tokens: Maximum tokens in the response.
•	temperature: Controls randomness in responses (higher values = more creative).
•	top_p: Nucleus sampling for diverse responses.
•	Penalties: Adjusts response penalties for token frequency and presence.
________________________________________
Error Handling
•	Displays appropriate error messages for failed API calls.
•	Logs status codes and response text for debugging.
________________________________________
Example Interaction
1.	User enters: "What is the capital of France?"
2.	Bot responds: "The capital of France is Paris."
________________________________________
Future Enhancements
•	Add user authentication for secure access.
•	Integrate additional AI models for varied capabilities.
•	Store chat history in a database for long-term persistence.
________________________________________
License
This project is licensed under the MIT License. See the LICENSE file for details.
________________________________________
Acknowledgements
•	Streamlit Documentation
•	Azure OpenAI Service
