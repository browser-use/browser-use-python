#!/usr/bin/env -S rye run python

import asyncio
from typing import List

from pydantic import BaseModel

from browser_use_sdk import AsyncBrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = AsyncBrowserUse()


# Regular Task
async def retrieve_regular_task() -> None:
    """
    Retrieves a regular task and waits for it to finish.
    """

    print("Retrieving regular task...")

    regular_task = await client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gemini-2.5-flash"},
    )

    print(f"Regular Task ID: {regular_task.id}")

    while True:
        regular_status = await client.tasks.retrieve(regular_task.id)
        print(f"Regular Task Status: {regular_status.status}")
        if regular_status.status == "finished":
            print(f"Regular Task Output: {regular_status.done_output}")
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

    structured_task = await client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gpt-4.1"},
        structured_output_json=SearchResult,
    )

    print(f"Structured Task ID: {structured_task.id}")

    while True:
        structured_status = await client.tasks.retrieve(task_id=structured_task.id, structured_output_json=SearchResult)
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
