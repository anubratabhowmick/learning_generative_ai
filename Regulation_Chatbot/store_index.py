import pinecone

from langchain.vectorstores import Pinecone

from src.helper import load_pdf, text_split, download_hf_embedding

from dotenv import load_dotenv
load_dotenv()


pc = pinecone.Pinecone()
index = pc.Index("regulation-chatbot")

extracted_data = load_pdf("data")
text_chunks = text_split(extracted_data)
embedding = download_hf_embedding()

docsearch = Pinecone.from_texts(
    [t.page_content for t in text_chunks],
    embedding,
    index_name = 'regulation-chatbot'
)
