####################################################### IMPORTANT #####################################################################  
# Install Ollama in your local machine using sudo snap install ollama                                                                 #
# Create an account in Ollama and go to this page: https://ollama.com/library/llama3.1                                                #
# From a separate terminal, enter: ollama run llama3.1 ( choose any version you want ) [NOTE: 405b parameterized version is 231gb]    #
# After the latest model is fetched, run the python file using streamlit run chat_app.py and chat away with the best in the business  # 
# Author: Anubrata Bhowmick                                                                                                           #
#######################################################################################################################################

# Don't forget to create a new environment and install us!
import streamlit as st
import ollama 

def get_llm_response(option, message):
    if option == 'Mistral-Large':
        llm_model = 'mistral-large'
    elif option == 'Llama3.1':
        llm_model = 'llama3.1'
        
    try:
        response = ollama.chat(
            model = llm_model,
            messages = message
        )
        return response['message']['content']
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None
    
def main():
    st.title("Chat with Open Source LLMs")
    
    option = st.selectbox(
        'What model would you like to chat with?',
        ('Llama3.1', 'Mistral-Large')
    )
    
    # Initiate the Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat message history on app return
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
            
    # React to user input
    if prompt := st.chat_input("What is your message?"):
        # Add the message to chat history
        st.session_state.messages.append({
            'role': 'user',
            'content': prompt
        })
        
        # Display in the container
        with st.chat_message('user'):
            st.markdown(prompt)
            
        # Get the Llama response
        llama_resp = get_llm_response(option, st.session_state.messages)
        
        # Display the response
        with st.chat_message('assistant'):
            st.markdown(llama_resp)
            
        # Add the response to chat history
        st.session_state.messages.append({
            'role': 'assistant',
            'content': llama_resp
        })
        
if __name__ == "__main__":
    main()