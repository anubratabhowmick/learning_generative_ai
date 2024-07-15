from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader

def load_pdf(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    
    return loader.load()


# Create text chunks
def text_split(extracted_data):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 20
    )
    
    return splitter.split_documents(extracted_data)


# Download the Embedding Model
def download_hf_embedding():
    return HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2") # You can search this in HuggingFace to see how the embedding works
