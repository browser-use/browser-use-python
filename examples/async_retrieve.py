#!/usr/bin/env -S poetry run python

import asyncio
from typing import List

from api import API_KEY
from pydantic import BaseModel

from browser_use_sdk import AsyncBrowserUse

client = AsyncBrowserUse(api_key=API_KEY)


# Regular Task
async def retrieve_regular_task() -> None:
    """
    Retrieves a regular task and waits for it to finish.
    """

    print("Retrieving regular task...")

    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Regular Task ID: {task.id}")

    while True:
        regular_status = await client.tasks.get_task(task.id)
        print(f"Regular Task Status: {regular_status.status}")
        if regular_status.status == "finished":
            print(f"Regular Task Output: {regular_status.output}")
            break

        await asyncio.sleep(1)

    print("Done")


async def retrieve_structured_task() -> None:
    """
    Retrieves a structured task and waits for it to finish.
    """

    print("Retrieving structured task...")

    # Structured Output
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

    while True:
        structured_status = await client.tasks.get_task(task_id=task.id, schema=SearchResult)
        print(f"Structured Task Status: {structured_status.status}")

        if structured_status.status == "finished":
            if structured_status.parsed_output is None:
                print("Structured Task No output")
            else:
                for post in structured_status.parsed_output.posts:
                    print(f" - {post.title} - {post.url}")

            break

        await asyncio.sleep(1)

    print("Done")


# Main


async def main() -> None:
    await asyncio.gather(
        #
        retrieve_regular_task(),
        retrieve_structured_task(),
    )


asyncio.run(main())
