import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from parser import JobDescriptionOutput
from prompt import SYSTEM_INSTRUCTION


load_dotenv()


def get_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in the .env file.")

    client = genai.Client(api_key=api_key)

    def generate(job_description):
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=job_description,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=JobDescriptionOutput,
            ),
        )

        if response.parsed:
            return response.parsed

        return JobDescriptionOutput.model_validate_json(response.text)

    return generate