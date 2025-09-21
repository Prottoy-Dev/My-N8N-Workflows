from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import httpx
import json
from typing import Optional

# Create FastAPI instance
app = FastAPI(title="Chat API", description="API to handle chat requests and forward to webhook")

# Add CORS middleware to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=False,  # Set to False when using allow_origins=["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Webhook URL
WEBHOOK_URL = "https://ranger.app.n8n.cloud/webhook/f67cc3fb-2b7d-462d-8350-8a4dd7bbfc69"

class ChatRequest(BaseModel):
    user_question: str
    user_email: EmailStr
    session_id: str
    article_url: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint that accepts user question, email, and session ID
    and forwards the data to the configured webhook.
    """
    try:
        print(f"Received request: {request}")
        
        # Prepare the payload for the webhook
        payload = {
            "user_question": request.user_question,
            "user_email": request.user_email,
            "session_id": request.session_id,
            "article_url": request.article_url
        }
        
        print(f"Sending payload to webhook: {payload}")
        
        # Send POST request to the webhook
        async with httpx.AsyncClient(timeout=600.0) as client:  # 10 minutes timeout
            response = await client.post(
                WEBHOOK_URL,
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            
            print(f"Webhook response status: {response.status_code}")
            print(f"Webhook response text: {response.text}")
            
            # Check if the webhook request was successful
            if response.status_code >= 400:
                print(f"Webhook failed with status {response.status_code}")
                raise HTTPException(
                    status_code=500,
                    detail=f"Webhook request failed with status {response.status_code}"
                )
            
            # Try to parse webhook response as JSON, fallback to text if not JSON
            try:
                webhook_data = response.json()
                print(f"Webhook JSON response: {webhook_data}")
            except Exception as json_error:
                print(f"Failed to parse JSON: {json_error}")
                webhook_data = {"response": response.text}
            
            # Return the webhook response data
            return {
                "status": "success",
                "webhook_status": response.status_code,
                "session_id": request.session_id,
                "data": webhook_data
            }
            
    except httpx.TimeoutException as e:
        print(f"Timeout error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Webhook request timed out"
        )
    except httpx.RequestError as e:
        print(f"Request error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Error connecting to webhook: {str(e)}"
        )
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Chat API is running"}

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)