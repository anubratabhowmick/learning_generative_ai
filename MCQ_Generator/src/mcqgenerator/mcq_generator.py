"""
A script to generate and evaluate quizzes using the LangChain library and OpenAI's GPT-4 model.

This script sets up a series of chains for generating and evaluating quizzes based on input text,
subject, and other parameters. The generated quizzes and their evaluations are handled sequentially
using LangChain's LLMChain and SequentialChain classes.

Attributes:
    llm (ChatOpenAI): An instance of ChatOpenAI configured to use the 'gpt-4o' model with a temperature of 0.5.
    quiz_generation_prompt (PromptTemplate): A template for generating quizzes.
    quiz_chain (LLMChain): A chain for generating quizzes using the quiz_generation_prompt.
    quiz_evaluation_prompt (PromptTemplate): A template for evaluating quizzes.
    review_chain (LLMChain): A chain for evaluating quizzes using the quiz_evaluation_prompt.
    generate_evaluate_chain (SequentialChain): A sequential chain that first generates a quiz and then evaluates it.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from langchain_openai import ChatOpenAI


from src.mcqgenerator.logger import logging
from src.mcqgenerator.template import TEMPLATE1, TEMPLATE2

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
