#!/usr/bin/env -S rye run python

from typing import List

from pydantic import BaseModel

from browser_use_sdk import BrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = BrowserUse()


# Regular Task
def create_regular_task() -> None:
    res = client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gemini-2.5-flash"},
    )

    print(res.id)


create_regular_task()


# Structured Output
def create_structured_task() -> None:
    class HackerNewsPost(BaseModel):
        title: str
        url: str

    class SearchResult(BaseModel):
        posts: List[HackerNewsPost]

    res = client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gpt-4.1"},
        structured_output_json=SearchResult,
    )

    print(res.id)


create_structured_task()
