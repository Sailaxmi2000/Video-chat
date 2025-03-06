from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_API_KEY"] = OPENAI_API_KEY
def get_text_chunks(text):
   text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
   chunks = text_splitter.split_text(text)
   return chunks
def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # Create a persistent directory for ChromaDB
    persist_directory = "chroma_db"
    
    # Initialize Chroma with the persistent directory
    vector_store = Chroma.from_texts(
        texts=text_chunks, 
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    return vector_store
def get_conversational_chain(vector_store):
   llm=llm = ChatOpenAI(model_name="gpt-4o",temperature=0.7)
   memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
   retriever = vector_store.as_retriever()
   conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory
        )
   
   return conversation_chain
   