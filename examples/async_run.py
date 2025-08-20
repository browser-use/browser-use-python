#!/usr/bin/env -S rye run python

import asyncio
from typing import List

from pydantic import BaseModel

from browser_use_sdk import AsyncBrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = AsyncBrowserUse()


# Regular Task
async def run_regular_task() -> None:
    regular_result = await client.tasks.run(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gemini-2.5-flash"},
    )

    print(f"Regular Task ID: {regular_result.id}")

    print(f"Regular Task Output: {regular_result.done_output}")

    print("Done")


# Structured Output
async def run_structured_task() -> None:
    class HackerNewsPost(BaseModel):
        title: str
        url: str

    class SearchResult(BaseModel):
        posts: List[HackerNewsPost]

    structured_result = await client.tasks.run(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gpt-4.1"},
        structured_output_json=SearchResult,
    )

    print(f"Structured Task ID: {structured_result.id}")

    if structured_result.parsed_output is not None:
        print("Structured Task Output:")
        for post in structured_result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

    print("Structured Task Done")


async def main() -> None:
    await asyncio.gather(
        #
        run_regular_task(),
        run_structured_task(),
    )


asyncio.run(main())
