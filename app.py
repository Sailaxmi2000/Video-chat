import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from src.youtube_transcript import get_youtube_id,get_transcript
from src.helper import get_text_chunks,get_vector_store,get_conversational_chain

def user_input(user_question):
    response = st.session_state.conversation({"question": user_question})
    st.session_state.chatHistory = response["chat_history"]
    for i, message in enumerate(st.session_state.chatHistory):
       if i % 2 == 0:
           st.write("User: ", message.content)
       else:
           st.write("Reply: ", message.content)
def main():
    st.title("Video-chat application ") 
    user_question=st.text_input("Ask a question from video Transcript")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_question:
        user_input(user_question)
    with st.sidebar:
         st.markdown("### **Enter your video link**")
         video_link=st.text_input("")
         process_button = st.button("Get Transcript")
         
         if video_link:
             st.video(video_link)
             st.success({video_link})
         if process_button and video_link:
             video_id = get_youtube_id(video_link)
             transcript = get_transcript(video_id)
             chunks = get_text_chunks(transcript)
             vector_store = get_vector_store(chunks)
             st.info(f"Created {len(chunks)} text chunks for processing")
             st.session_state.conversation = get_conversational_chain(vector_store)
        
             st.subheader("Transcript:")
             st.write(transcript)

        
             
             

if __name__=="__main__":
    main()