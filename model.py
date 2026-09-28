import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

from parser import JobDescriptionOutput
from prompt import SYSTEM_INSTRUCTION


load_dotenv()


MODEL_NAME = "gemma-4-26b-a4b-it"


def get_model():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    def generate(job_description):
        last_error = None

        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=job_description,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_INSTRUCTION,
                        response_mime_type="application/json",
                        response_schema=JobDescriptionOutput,
                    ),
                )

                if response.parsed:
                    return response.parsed

                return JobDescriptionOutput.model_validate_json(
                    response.text
                )

            except ServerError as e:
                last_error = e

                if "503" not in str(e):
                    raise

                if attempt < 2:
                    time.sleep(3)

        raise RuntimeError(
            "Gemini is temporarily unavailable due to high demand. "
            "Please try again in a few minutes."
        ) from last_error

    return generate