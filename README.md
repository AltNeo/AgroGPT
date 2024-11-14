# AgroGPT - Agricultural Intelligence Platform

AgroGPT is an AI-powered agricultural knowledge assistant designed to help farmers, agricultural experts, and researchers access and analyze agricultural information efficiently. The platform combines document intelligence with natural language processing to provide instant answers to farming queries and analyze agricultural documents.

## Features

### 🌾 Agricultural Knowledge Base
- Interactive chatbot for agricultural queries
- Real-time answers to farming questions
- Support for multiple languages
- Voice input capability

### 📊 Document Intelligence
- PDF document upload and analysis
- Smart document processing
- Conversion of agricultural documents into actionable insights
- Efficient information retrieval from research papers

### 🤖 AI Assistant
- Natural language interaction
- Context-aware responses
- Agricultural domain expertise
- Multi-lingual support

### 📚 Data Analysis
- Advanced algorithms for agricultural data interpretation
- Research paper analysis
- Statistical insights
- Trend analysis

## Technology Stack

- **Frontend**: Streamlit, HTML, CSS
- **Backend**: Python, Flask
- **AI/ML**: 
  - LangChain for document processing
  - OpenAI for natural language understanding
  - FAISS for efficient vector storage and similarity search
- **Document Processing**: PyPDF2 for PDF handling

## Setup Instructions

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

5. Run the application:
```bash
streamlit run main.py
```

## Usage

### Document Analysis
1. Navigate to the Chat section
2. Upload your agricultural PDF document
3. Ask questions about the document content
4. Receive AI-powered responses based on the document

### Agricultural Queries
1. Use the chat interface
2. Type your question or use voice input
3. Get instant responses from the AI assistant
4. Switch languages as needed

## Project Structure

```
├── main.py                 # Main Streamlit application
├── app.py                  # Flask application
├── pages/
│   └── 1_Chat.py          # Chat interface implementation
├── Attempt3/
│   ├── app.py             # Flask application
│   ├── static/
│   │   └── css/
│   │       └── style.css  # Styling
│   └── templates/
│       ├── chat.html      # Chat interface template
│       └── index.html     # Landing page template
└── requirements.txt        # Project dependencies
```

## Features in Detail

### Smart Document Processing
- Chunks documents into manageable segments
- Creates embeddings for efficient search
- Stores vector representations for quick retrieval
- Provides context-aware responses

### Real-time Assistance
- Instant response to agricultural queries
- Context maintenance during conversations
- Support for follow-up questions
- Integration with agricultural knowledge base

### Multi-language Support
- Interface language switching
- Query processing in multiple languages
- Response generation in user's preferred language

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Contact

[Add your contact information here]
