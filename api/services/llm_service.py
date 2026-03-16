
# TODO: Import your chosen LLM SDK
# from openai import OpenAI
# import anthropic
# import boto3
# from google.cloud import aiplatform

import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
import json

load_dotenv(override=True)
API_HOST = os.getenv("API_HOST", "github")
client = AsyncOpenAI(base_url="https://models.github.ai/inference", api_key=os.environ["GITHUB_TOKEN"])
MODEL_NAME = os.getenv("GITHUB_MODEL", "openai/gpt-4o")

async def analyze_journal_entry(entry_id: str, entry_text: str) -> dict:
    """
    Analyze a journal entry using your chosen LLM API.

    Args:
        entry_id: The ID of the journal entry being analyzed
        entry_text: The combined text of the journal entry (work + struggle + intention)

    Returns:
        dict with keys:
            - entry_id: ID of the analyzed entry
            - sentiment: "positive" | "negative" | "neutral"
            - summary: 2 sentence summary of the entry
            - topics: list of 2-4 key topics mentioned
            - created_at: timestamp when the analysis was created

    TODO: Implement this function using your chosen LLM provider.
    See the Learn to Cloud curriculum for guidance on:
    - Setting up your LLM API client
    - Crafting effective prompts
    - Handling structured JSON output
    """
    response = await client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    response_format= {"type": "json_object"}, #Ensures the output is json format
    messages=[
        {"role": "system", "content": "You are a helpful agent that analyzes Entries to a Joural, you must analyze the journal entry and return a dictionary with the following keys: entry_id: ID of the analyzed entry, sentiment: 'positive' | 'negative' | 'neutral', summary: 2 sentence summary of the entry, topics: list of 2-4 key topics mentioned, created_at: timestamp when the analysis was created"},
        {"role": "user", "content": f"Analyze this entry {entry_text} with id {entry_id}"},
    ],
    )

    #print(f"Response from {API_HOST}: \n")
    result = response.choices[0].message.content

    if not result:

        raise NotImplementedError(
        "Implement this function using your chosen LLM API. "
        "See the Learn to Cloud curriculum for guidance."
        )
    else:
        return json.loads(result)

