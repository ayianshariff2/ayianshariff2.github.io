from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Add CORSMiddleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define the data model for the form submission
class FormSubmission(BaseModel):
    name: str
    country: str
    message: str
    submittedAt: str


# This will hold the form submissions in-memory (as a list)
form_submissions: List[FormSubmission] = []


@app.post("/api/messages")
async def submit_message(form_data: FormSubmission):
    # Store the form submission (you could save it to a database here)
    form_submissions.append(form_data)
    return {"message": "Form submitted successfully!", "data": form_data}


@app.get("/api/messagev")
async def get_messages():
    # Retrieve the stored form submissions
    return form_submissions
