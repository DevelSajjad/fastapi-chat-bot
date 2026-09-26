from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from sentence_transformers import SentenceTransformer

def extract_pdf(file):
    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text

def split_document(text):


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=800,

        chunk_overlap=100

    )


    return splitter.split_text(text)



def create_embedding(text):
    client = OpenAI()

    response = client.embeddings.create(

        model="text-embedding-3-small",

        input=text

    )


    return response.data[0].embedding



def create_embeddingTwo(text):
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    embedding = model.encode(text)

    return embedding.tolist()