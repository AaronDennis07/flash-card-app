from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_document(url):
    loader = PyPDFLoader(url)
    data = loader.load()
    out=""

    for d in data:
        out+=d.page_content

    return out

def extract_input(data):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    model_name="gpt-4",
    chunk_size=3500,
    chunk_overlap=0,
    )
    texts = text_splitter.split_text(data)
    return texts[0]