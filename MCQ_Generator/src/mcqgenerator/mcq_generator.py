import json
import traceback
import pandas as pd

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from langchain_openai import ChatOpenAI

from langchain_community.llms import OpenAI
from langchain_community.callbacks.manager import get_openai_callback

from src.mcqgenerator.logger import logging
from src.mcqgenerator.template import TEMPLATE1, TEMPLATE2
from src.mcqgenerator.utils import read_file, get_table_data

from dotenv import load_dotenv
load_dotenv()

# Create the ChatOpenAI object
llm = ChatOpenAI(
    model_name = 'gpt-4o',
    temperature = 0.5
)

quiz_generation_prompt = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=TEMPLATE1
)

quiz_chain = LLMChain(
    llm= llm,
    prompt = quiz_generation_prompt,
    output_key = 'quiz',
    verbose = True
)

quiz_evaluation_prompt = PromptTemplate(
    input_variables =['subject', 'quiz'], 
    template=TEMPLATE2
)

review_chain = LLMChain(
    llm = llm,
    prompt = quiz_evaluation_prompt,
    output_key = 'review',
    verbose = True
)

generate_evaluate_chain = SequentialChain(
    chains = [quiz_chain, review_chain],
    input_variables = ['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables = ['quiz', 'review'],
    verbose = True
)




