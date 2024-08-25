# Use Google Gemini Model Through Python

This project demonstrates how to integrate with the Google Gemini API using Google AI Python SDK. In this script, I'll show you how to configure the API, set up generation parameters, and generate text responses without any formatting.

## Overview

In this project, I’ve set up a Python script to interact with the Google Gemini API. The script is designed to configure the API key, define text generation settings, and generate plain text responses based on a given prompt.

## Prerequisites

Before running the script, make sure you have the following:

1. **Python 3.x**: Ensure Python is installed on your machine.
2. **Google API Key**: You need an API key for Google Gemini. Add this key to a `.env` file in the root directory of your project.

## Setup

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/shaunakbale/UseGoogleGeminiThroughPython.git
cd UseGoogleGeminiThroughPython
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**

```
google-generativeai
python-dotenv
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory with your Google Gemini API key:

```
GOOGLE_AI_STUDIO_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

## Usage

The main script `UseGoogleGemini.py` demonstrates how to use the Google Gemini API. Here’s how you can run it:

```bash
python UseGoogleGemini.py
```

### Script Breakdown

- **`generation_config`**: Sets the parameters for text generation, such as temperature, top_p, top_k, and response mime type.
- **`SYSTEM_INSTRUCTIONS`**: Ensures that the model generates responses without any formatting like bold or italic.
- **`AvailableModels`**: Enum to choose the model you want to use.
- **`PROMPT`**: The text prompt that the model will use to generate a response. Try your different prompts here.

## Example

After executing the script, you will receive an output like:

```
[Generated response from the model]
```

## Notes

- **Model Support**: The script supports various models such as `gemini-1.0-pro`, `gemini-1.5-pro`, `gemini-1.5-pro-exp-0801` and `gemini-1.5-flash`. You can update the model in the script as needed.
- **MIME Types**: The `response_mime_type` can be either `text/plain` or `application/json`.

## Contributing

I welcome contributions! Feel free to open issues or submit pull requests if you have suggestions or improvements.

## Contact

If you have any questions or feedback, please reach out to me via shaunakbale@gmail.com or open an issue in the GitHub repository.
