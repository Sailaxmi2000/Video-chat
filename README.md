# Video Chat Application

## Overview
This Video Chat Application is an interactive tool that allows users to ask questions about YouTube video content and receive relevant answers. The application uses natural language processing and AI to analyze video transcripts and provide contextual responses to user queries.

## Features
- **YouTube Video Integration**: Input any YouTube video URL to extract and process its transcript
- **Transcript Extraction**: Automatically pulls transcripts from YouTube videos
- **Text Chunking**: Breaks down transcripts into manageable pieces for processing
- **Vector Database**: Stores text embeddings for efficient semantic search
- **Conversational AI**: Engages users in a natural dialogue about the video content
- **Multi-turn Conversations**: Maintains context across multiple questions about the same video

## Technology Stack
- **Frontend**: Streamlit for the user interface
- **Language Model**: OpenAI GPT models (via LangChain)
- **Embeddings**: OpenAI text-embedding-3-small for semantic representation
- **Vector Database**: ChromaDB for storing and retrieving relevant text chunks
- **Text Processing**: LangChain's RecursiveCharacterTextSplitter for text chunking
- **Transcript Extraction**: YouTube Transcript API

## How It Works
1. **Video Input**: User provides a YouTube video URL
2. **Transcript Extraction**: System extracts the transcript from the video
3. **Text Processing**: Transcript is split into chunks and converted to vector embeddings
4. **Question Answering**: User questions are processed to find relevant parts of the transcript
5. **Response Generation**: AI generates contextual responses based on the relevant transcript sections
6. **Conversation History**: The system maintains the conversation context for follow-up questions

## Project Structure
```
video-chat/
├── app.py                  # Main Streamlit application
├── src/
│   ├── __init__.py
│   ├── helper.py           # Contains utility functions for vector storage and conversation
│   ├── youtube_transcript.py  # Functions for YouTube transcript extraction
│   └── styles.py           # Custom styling for the application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key for embeddings and language model

### Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/video-chat.git
   cd video-chat
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   ```
   # Create a .env file
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

### Running the Application
```
streamlit run app.py
```

## Usage
1. Enter a YouTube video URL in the sidebar
2. Click "Get Transcript" to process the video
3. Ask questions about the video content in the text input field
4. Review the AI-generated responses
5. Ask follow-up questions for more information

## Limitations
- Works only with YouTube videos that have available transcripts
- Quality of responses depends on the quality and accuracy of the video transcript
- Processing long videos may take more time and resources

## Future Improvements
- Support for more video platforms beyond YouTube
- Audio extraction and transcription for videos without existing transcripts
- Visual content analysis to incorporate information from the video imagery
- User authentication and saved conversation history
- Transcript correction and improvement tools

## License
MIT LICENCE

## Acknowledgements
- LangChain for providing the framework for building LLM applications
- OpenAI for the language models and embeddings
- Streamlit for the web application framework
- YouTube Transcript API for transcript extraction capabilities
