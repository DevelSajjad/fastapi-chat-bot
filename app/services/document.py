from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from openai import OpenAI
from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session
from app.models.document import Document

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


def rag_prompt(
    db,
    message
):

    question_embedding = create_embeddingTwo(message)

    documents = (
        db.query(Document)
        .order_by(
            Document.embedding.cosine_distance(
                question_embedding
            )
        )
        .limit(5)
        .all()
    )


    context = "\n\n".join(
        document.content
        for document in documents
    )


    prompt = f"""
    Answer using only the following context.

    Context:
    {context}

    Question:
    {message}
    """

    return prompt