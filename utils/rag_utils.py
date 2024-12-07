import os
import shutil
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.schema import Document

def load_and_chunk_documents(md_folder_path):
    documents = []
    for file in os.listdir(md_folder_path):
        if file.endswith('.md'):
            md_path = os.path.join(md_folder_path, file)
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()
            documents.append(Document(page_content=content, metadata={"source": md_path}))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print("amount of documents used: ", len(documents))
    
    with open("combined_documents.md", "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.page_content + "\n\n")
    return chunks

def setup_rag_embeddings(data_dir="input/", chroma_path="chroma"):
    chunks = load_and_chunk_documents(data_dir)
    if os.path.exists(chroma_path):
        shutil.rmtree(chroma_path)

    vectorstore = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=chroma_path
    )
    print(f"Saved {len(chunks)} chunks to {chroma_path}.")

    retriever = vectorstore.as_retriever()
    return retriever

def build_rag_chain(retriever, model_name="gpt-4o-mini"):
    prompt = hub.pull("rlm/rag-prompt")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    llm = ChatOpenAI(model=model_name)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

