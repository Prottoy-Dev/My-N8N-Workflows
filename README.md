# My N8N Workflows Collection

Welcome to my collection of N8N workflows! This repository contains various automation workflows created and exported from N8N, covering different use cases and integrations.

## About N8N

N8N is an open-source workflow automation tool that allows you to connect different services and automate tasks through a visual interface. Each workflow in this repository is provided as a JSON file that can be imported directly into your N8N instance.

## Workflows & Projects

### 📧 Mail Labeling Workflow
- **File**: `Mail Labeling.json`
- **Purpose**: Automated email classification and labeling system

### 📖 AI Agent Doc Reader
- **File**: `AI Agent Doc Reader.json`  
- **Purpose**: AI-powered document reading and analysis workflow

### 🤖 Article Insights Chatbot Project
- **Folder**: `chatbot-with-article-analysis/`
- **Description**: Complete full-stack application for article analysis and insights generation
- **Tech Stack**: FastAPI + React + TypeScript + N8N + Google Gemini AI
- **Features**: 
  - Web article scraping and analysis
  - Real-time chat interface
  - AI-powered summaries and insights
  - Email notifications
  - Google Sheets data logging

[View detailed documentation](./chatbot-with-article-analysis/README.md)

## How to Use These Workflows

1. **Download** the JSON file for the workflow you're interested in
2. **Open** your N8N instance (local or cloud)
3. **Import** the workflow by uploading the JSON file
4. **Configure** the required credentials and connections
5. **Activate** the workflow and start automating!

## Getting Started with N8N

If you're new to N8N:
1. Visit [n8n.io](https://n8n.io) to learn more
2. Try the [cloud version](https://app.n8n.cloud) or install locally
3. Check out the [documentation](https://docs.n8n.io)
4. Join the [community](https://community.n8n.io)

## Repository Structure

```
My-N8N-Workflows/
├── chatbot-with-article-analysis/    # Full-stack chatbot project
│   ├── Article scraping with n8n workflow.json
│   ├── fast_api.py
│   ├── chatbot_frontend_js/
│   ├── requirements.txt
│   └── README.md
├── AI Agent Doc Reader.json          # AI document reader workflow
├── Mail Labeling.json                # Email labeling workflow
├── LICENSE
└── README.md                         # This file
```

- **Article Processing**: Web scraping and AI-powered analysis
- **Real-time Chat Interface**: Interactive frontend for user queries
- **Email Integration**: Automated email delivery of insights
- **Data Logging**: Google Sheets integration for data persistence
- **AI-Powered Insights**: Google Gemini integration for intelligent analysis

### Tech Stack

- **Backend**: FastAPI with async webhook integration
- **Frontend**: React + TypeScript + Vite + Shadcn UI
- **Automation**: N8N workflow with Google Gemini AI
- **Database**: Google Sheets for data persistence
- **Email**: Gmail integration for notifications

### Installation and Setup

#### Backend Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI server:
```bash
uvicorn fast_api:app --reload
```

#### Frontend Setup

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

#### N8N Workflow Setup

1. Import the workflow file `Article scraping with n8n workflow.json` into your N8N instance
2. Configure the required credentials:
   - Google Gemini API key
   - Gmail credentials
   - Google Sheets access
3. Set up the webhook URL in the FastAPI configuration

### API Endpoints

#### POST /chat

Accepts chat requests and forwards them to the N8N webhook.

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

### Configuration

The webhook URL is configured in the `fast_api.py` file:
```python
WEBHOOK_URL = "https://ranger.app.n8n.cloud/webhook/f67cc3fb-2b7d-462d-8350-8a4dd7bbfc69"
```
