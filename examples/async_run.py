#!/usr/bin/env -S rye run python

import asyncio
from typing import List

from pydantic import BaseModel

from browser_use import AsyncBrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = AsyncBrowserUse()


# Regular Task
async def run_regular_task() -> None:
    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Regular Task ID: {task.id}")

    result = await task.complete()

    print(f"Regular Task Output: {result.output}")

    print("Done")


# Structured Output
async def run_structured_task() -> None:
    class HackerNewsPost(BaseModel):
        title: str
        url: str

    class SearchResult(BaseModel):
        posts: List[HackerNewsPost]

    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gpt-4.1",
        schema=SearchResult,
    )

    print(f"Structured Task ID: {task.id}")

    result = await task.complete()

    if result.parsed_output is not None:
        print("Structured Task Output:")
        for post in result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

    print("Structured Task Done")


async def main() -> None:
    await asyncio.gather(
        #
        run_regular_task(),
        run_structured_task(),
    )


asyncio.run(main())
