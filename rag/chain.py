import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config import GROQ_API_KEY, LLM_MODEL, RETRIEVAL_K, SYSTEM_PROMPT
from rag.ingest import get_vectorstore


@st.cache_resource
def get_llm():
    return ChatGroq(model=LLM_MODEL, api_key=GROQ_API_KEY, temperature=0)


def format_docs(docs) -> str:
    parts = []
    for doc in docs:
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "?")
        parts.append(f"[{source}, p.{page}]\n{doc.page_content}")
    return "\n\n---\n\n".join(parts)


def get_retriever(k: int = RETRIEVAL_K):
    store = get_vectorstore()
    return store.as_retriever(search_kwargs={"k": k})


def build_chain():
    retriever = get_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            (
                "human",
                "Document excerpts:\n{context}\n\nQuestion: {question}",
            ),
        ]
    )

    llm = get_llm()

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain, retriever


def answer_question(question: str):
    chain, retriever = build_chain()
    sources = retriever.invoke(question)
    answer = chain.invoke(question)
    return answer, sources
