# Chat API

A FastAPI application that provides a `/chat` endpoint to forward user chat requests to an n8n webhook.

## Features

- FastAPI-based REST API
- Email validation for user emails
- Error handling and timeout management
- Async webhook forwarding

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. The API will be available at `http://localhost:8000`
3. Interactive API documentation will be available at `http://localhost:8000/docs`

## API Endpoints

### POST /chat

Accepts chat requests and forwards them to the configured webhook.

**Request Body:**
```json
{
  "user_question": "What is the weather today?",
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
    "response": "This is the data returned from the n8n webhook"
  }
}
```

### GET /

Health check endpoint that returns a simple message.

### GET /health

Health check endpoint that returns the application status.

## Configuration

The webhook URL is configured in the `main.py` file:
```python
WEBHOOK_URL = "https://ranger.app.n8n.cloud/webhook/f67cc3fb-2b7d-462d-8350-8a4dd7bbfc69"
```

## Testing

You can test the API using curl:

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_question": "Hello, how are you?",
    "user_email": "test@example.com",
    "session_id": "test_session_001",
    "article_url": "https://example.com/article"
  }'
```

Or use the interactive documentation at `http://localhost:8000/docs` to test the endpoints.