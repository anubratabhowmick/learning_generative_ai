import json
import traceback
import pandas as pd
import streamlit as st

from dotenv import load_dotenv

from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.mcq_generator import generate_evaluate_chain

from langchain_community.callbacks.manager import get_openai_callback

# Load the Response JSON file
with open("./data/response.json", "r") as file:
    RESPONSE_JSON = json.load(file) 
# Creating a title for the Streamlit App
st.title("MCQ Generation Application using LangChain")

# Create a form for the views
with st.form("user_inputs"):
    # File upload
    upload_file = st.file_uploader("Upload a PDF or a text file")
    # Input Fields
    mcq_counter = st.number_input("Number of MCQs to be generated", min_value=5, max_value=50)
    # Subject
    subject = st.text_input("Enter the subject", max_chars=20)
    # Quiz Tone
    tone = st.text_input("Complexity of the questions", max_chars=20, placeholder='Simple')
    # Button for Generation
    button = st.form_submit_button("Generate MCQs")
    # Check if the button has been clicked and all fields have values
    if button and upload_file is not None and mcq_counter and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(upload_file)
                # Count the tokens and the cost of the API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain({
                        "text": text,
                        "number": mcq_counter,
                        "subject": subject,
                        "tone": tone,
                        "response_json": RESPONSE_JSON
                    })
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('Error!')
            else:
                print(f'Total Tokens: {cb.total_tokens}')
                print(f'Prompt Tokens: {cb.prompt_tokens}')
                print(f'Completion Tokens: {cb.completion_tokens}')
                print(f'Total cost: {cb.total_cost}')
                
                if isinstance(response, dict):
                    # Extract the quiz data from the response
                    cleaned_quiz = response.get('quiz').strip('### RESPONSE_JSON\n```json\n')
                    
                    if cleaned_quiz is not None:
                        table_data = get_table_data(cleaned_quiz)
                        
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index = df.index+1  
                            st.table(df)   
                            # Display the review in a text box
                            st.text_area(label='Review', value=response['review'])
                        else:
                            st.error('Error in the table data!')
                    else:
                        st.write(response)
