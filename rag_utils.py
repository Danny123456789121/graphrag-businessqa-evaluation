import os
import shutil
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
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
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print("amount of documents used: ", len(documents))
    
    with open("combined_documents.md", "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(doc.page_content + "\n\n")
    return chunks

def setup_rag_embeddings(data_dir, faiss_path, embeddings_model, reembed=False):
    if os.path.exists(faiss_path) and not reembed:
        print(f"Loading existing FAISS index from {faiss_path}...")
        vectorstore = FAISS.load_local(faiss_path, embeddings_model, allow_dangerous_deserialization=True)
    else:
        print("Embedding documents...")
        chunks = load_and_chunk_documents(data_dir)
        if os.path.exists(faiss_path):
            shutil.rmtree(faiss_path)
        vectorstore = FAISS.from_documents(chunks, embeddings_model)
        vectorstore.save_local(faiss_path)
        print(f"Saved {len(chunks)} chunks to {faiss_path}.")

    retriever = vectorstore.as_retriever()
    return retriever

def build_rag_chain(retriever, llm):
    prompt = hub.pull("rlm/rag-prompt")
    print("prompt",prompt)

    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

