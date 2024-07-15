import os
import pinecone

from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from langchain.prompts import PromptTemplate

from src.prompt import prompt_template
from src.helper import download_hf_embedding


from flask import Flask, render_template, jsonify, request

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

embedding = download_hf_embedding()

# 
# Once the document is indexed, we can fetch like this
indexed_doc = Pinecone.from_existing_index('regulation-chatbot', embedding)

PROMPT = PromptTemplate(
    template = prompt_template,
    input_variables = ['context', 'question']
)

chain_type_kwargs = {
        'prompt': PROMPT
}

llm = CTransformers(
    model = "model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type = "llama",
    config = {
        "max_new_tokens": 512,
        "temperature": 0.8
    }
)

qa = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever = indexed_doc.as_retriever(search_kwargs = {'k': 3}),
    return_source_documents = True,
    chain_type_kwargs = chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods = ['GET', 'POST'])
def chat():
    msg = request.form["msg"]
    print(msg)
    result = qa({
        "query": msg
    })
    print("Response: ", result['result'])
    return str(result['result'])


if __name__ == '__main__':
    app.run(debug=True)


