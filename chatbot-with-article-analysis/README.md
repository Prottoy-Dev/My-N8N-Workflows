# Article Insights Chatbot Project

A complete full-stack application built around an N8N workflow for article analysis and insights generation.

## Project Overview

This project creates an intelligent chatbot that can analyze web articles and provide AI-powered insights. Users can submit article URLs, ask questions about the content, and receive summaries and key insights via both the chat interface and email.

## Features

- **Article Processing**: Web scraping and AI-powered analysis using Firecrawl and Google Gemini
- **Real-time Chat Interface**: Interactive React frontend for user queries
- **Email Integration**: Automated email delivery of insights via Gmail
- **Data Logging**: Google Sheets integration for data persistence
- **AI-Powered Insights**: Google Gemini integration for intelligent analysis
- **Session Management**: Track conversations with unique session IDs

## Tech Stack

- **Backend**: FastAPI with async webhook integration
- **Frontend**: React + TypeScript + Vite + Shadcn UI
- **Automation**: N8N workflow with Google Gemini AI
- **Database**: Google Sheets for data persistence
- **Email**: Gmail integration for notifications
- **Web Scraping**: Firecrawl for article content extraction

## Project Structure

```
chatbot-with-article-analysis/
├── Article scraping with n8n workflow.json  # Main N8N workflow
├── fast_api.py                              # FastAPI backend server
├── chatbot_frontend_js/                     # React frontend application
├── requirements.txt                         # Python dependencies
├── start-frontend.bat                       # Frontend startup script
└── README.md                               # This file
```

## Installation and Setup

### Prerequisites

- Python 3.8+
- Node.js 16+
- N8N instance (local or cloud)
- Google Cloud Platform account (for Gemini API)
- Gmail account for email integration
- Google Sheets for data logging

### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:
```bash
uvicorn fast_api:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd chatbot_frontend_js
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

Or use the provided batch file:
```bash
start-frontend.bat
```

The frontend will be available at `http://localhost:8080`

### N8N Workflow Setup

1. Import the workflow file `Article scraping with n8n workflow.json` into your N8N instance
2. Configure the required credentials:
   - **Google Gemini API**: Add your Google AI API key
   - **Gmail**: Configure Gmail OAuth credentials
   - **Google Sheets**: Set up Google Sheets access
   - **Firecrawl**: Add Firecrawl API key for web scraping
3. Update the webhook URL in `fast_api.py` if using a different N8N instance

## API Documentation

### POST /chat

Accepts chat requests and forwards them to the N8N webhook for processing.

**Request Body:**
```json
{
  "user_question": "What are the key insights from this article?",
  "user_email": "user@example.com",
  "session_id": "session_123",
  "article_url": "https://example.com/article"
}
```

**Response:**
```json
{
  "status": "success",
  "webhook_status": 200,
  "session_id": "session_123",
  "data": {
    "output": "AI-generated insights and summary"
  }
}
```

## Configuration

### Webhook URL
Update the webhook URL in `fast_api.py`:
```python
WEBHOOK_URL = "https://your-n8n-instance.com/webhook/your-webhook-id"
```

### CORS Settings
The FastAPI backend is configured to allow all origins for development. Update CORS settings for production:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # Restrict in production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Usage

1. **Start the Backend**: Run the FastAPI server
2. **Start the Frontend**: Launch the React application
3. **Configure N8N**: Import and configure the workflow
4. **Test the Application**:
   - Enter your email and a session ID
   - Provide an article URL
   - Ask questions about the article
   - Receive insights via chat and email

## N8N Workflow Details

The workflow includes:
- **Webhook Trigger**: Receives requests from FastAPI
- **Firecrawl Node**: Extracts article content
- **Google Gemini AI**: Processes content and generates insights
- **Gmail Node**: Sends email notifications
- **Google Sheets Node**: Logs conversation data

## Features in Detail

### AI Agent Capabilities
- Answer user questions about article content
- Generate 3-5 sentence summaries
- Extract 3-5 key insights
- Maintain conversation context
- Handle error scenarios gracefully

### Frontend Features
- Auto-scrolling chat interface
- Form validation
- Loading states
- Error handling
- Responsive design

### Backend Features
- Async request handling
- 600-second timeout for long-running processes
- Comprehensive error logging
- Email validation
- JSON response formatting

## Testing

Test the API using curl:
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_question": "What are the main points of this article?",
    "user_email": "test@example.com",
    "session_id": "test_session_001",
    "article_url": "https://example.com/sample-article"
  }'
```

Or use the interactive documentation at `http://localhost:8000/docs`

## Contributing

This project was created as a learning exercise for N8N automation. Feel free to fork and modify for your own use cases.

## License

This project is open source and available under the [MIT License](../LICENSE).