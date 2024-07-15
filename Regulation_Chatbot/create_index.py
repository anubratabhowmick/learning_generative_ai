import pinecone
from pinecone import ServerlessSpec


from dotenv import load_dotenv
load_dotenv()

pc = pinecone.Pinecone()

pc.create_index(
    name="regulation-chatbot",
    dimension=384, # Replace with your model dimensions
    metric="cosine", # Replace with your model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)
