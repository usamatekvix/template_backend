from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

MAILTRAP_API_KEY = os.getenv("MAILTRAP_API_KEY")
MAILTRAP_URL = os.getenv("MAILTRAP_URL")


class EmailSchema(BaseModel):
    email: EmailStr
    subject: str
    html: str

@router.post("/send-property-email")
async def send_property_email(payload: EmailSchema):
    try:
        data = {
            "from": {
                "email": "hello@example.com",
                "name": "Your Real Estate"
            },
            "to": [
                {
                    "email": payload.email
                }
            ],
            "subject": payload.subject,
            "html": payload.html,
            "category": "Property Notification"
        }

        headers = {
            "Authorization": f"Bearer {MAILTRAP_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(MAILTRAP_URL, headers=headers, json=data)
        response.raise_for_status()

        return {"success": True, "message": "Email sent successfully"}
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
