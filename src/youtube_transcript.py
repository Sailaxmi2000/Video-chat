import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_id(url):
    video_id = None
    if "youtube.com/watch" in url:
        video_id = re.search(r"v=([^&]+)", url).group(1)
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    return video_id
def get_transcript(video_id):
     transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
     transcript = " ".join([entry["text"] for entry in transcript_list])
     return transcript