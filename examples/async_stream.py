#!/usr/bin/env -S poetry run python

import asyncio
from typing import List

from api import API_KEY
from pydantic import BaseModel

from browser_use import AsyncBrowserUse

client = AsyncBrowserUse(api_key=API_KEY)


# Regular Task
async def stream_regular_task() -> None:
    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Regular Task ID: {task.id}")

    async for step in task.stream():
        print(f"Regular Task Status: {step.number}")

    result = await task.complete()

    if result.output is not None:
        print(f"Regular Task Output: {result.output}")

    print("Regular Task Done")


# Structured Output
async def stream_structured_task() -> None:
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

    async for step in task.stream():
        print(f"Structured Task Step {step.number}: {step.url} ({step.next_goal})")

    result = await task.complete()

    if result.parsed_output is not None:
        print("Structured Task Output:")

        for post in result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

    print("Structured Task Done")


# Main


async def main() -> None:
    await asyncio.gather(
        #
        stream_regular_task(),
        stream_structured_task(),
    )


asyncio.run(main())
