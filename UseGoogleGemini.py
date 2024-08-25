import os
import google.generativeai as genai
from dotenv import load_dotenv

from AvailableModels import AvailableModels

# To Load environment variables
load_dotenv()

# Tweak generation_config for experiments
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain" # allowed mimetypes are `text/plain` and `application/json`
}

# Configue Google Gemini API Key (Add "GOOGLE_AI_STUDIO_API_KEY" in .env File)
genai.configure(api_key=os.getenv("GOOGLE_AI_STUDIO_API_KEY"))

# Instructions to model so that it generates response without any formatting
SYSTEM_INSTRUCTIONS = """No Formatting: Do not use any text formatting (bold, italic, underline, etc.)."""

"""
USE AvailableModels ENUM

Currently supports models:
- gemini-1.0-pro
- gemini-1.5-pro
- gemini-1.5-pro-exp-0801
- gemini-1.5-flash
"""

# Setting up the gemini model for use
model = genai.GenerativeModel(
  model_name=AvailableModels.GEMINI_1_5_FLASH.value,
  generation_config=generation_config,
  system_instruction= SYSTEM_INSTRUCTIONS
)

# Write your prompt here
PROMPT = """ Write A Short Summary About Google Gemini """

# Model response output
response = model.generate_content(PROMPT)

print(response.text)