import os
from openai import OpenAI

def get_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
