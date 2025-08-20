#!/usr/bin/env -S rye run python

import asyncio
from typing import List

from pydantic import BaseModel

from browser_use_sdk import AsyncBrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = AsyncBrowserUse()


# Regular Task
async def create_regular_task() -> None:
    res = await client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gemini-2.5-flash"},
    )

    print(f"Regular Task ID: {res.id}")


# Structured Output
async def create_structured_task() -> None:
    class HackerNewsPost(BaseModel):
        title: str
        url: str

    class SearchResult(BaseModel):
        posts: List[HackerNewsPost]

    res = await client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gpt-4.1"},
        structured_output_json=SearchResult,
    )

    print(f"Structured Task ID: {res.id}")


# Main


async def main() -> None:
    await asyncio.gather(
        #
        create_regular_task(),
        create_structured_task(),
    )


asyncio.run(main())
