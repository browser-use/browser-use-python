#!/usr/bin/env -S rye run python

import asyncio
from typing import List

from pydantic import BaseModel

from browser_use_sdk import AsyncBrowserUse
from browser_use_sdk.types.task_create_params import AgentSettings

# gets API Key from environment variable BROWSER_USE_API_KEY
client = AsyncBrowserUse()


# Regular Task
async def stream_regular_task() -> None:
    regular_task = await client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings=AgentSettings(llm="gemini-2.5-flash"),
    )

    print(f"Regular Task ID: {regular_task.id}")

    async for res in client.tasks.stream(regular_task.id):
        print(f"Regular Task Status: {res.status}")

        if len(res.steps) > 0:
            last_step = res.steps[-1]
            print(f"Regular Task Step: {last_step.url} ({last_step.next_goal})")
            for action in last_step.actions:
                print(f" - Regular Task Action: {action}")

    print("Regular Task Done")


# Structured Output
async def stream_structured_task() -> None:
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

    async for res in client.tasks.stream(structured_task.id, structured_output_json=SearchResult):
        print(f"Structured Task Status: {res.status}")

        if res.status == "finished":
            if res.parsed_output is None:
                print("Structured Task No output")
            else:
                for post in res.parsed_output.posts:
                    print(f" - Structured Task Post: {post.title} - {post.url}")
            break

    print("Structured Task Done")


# Main


async def main() -> None:
    await asyncio.gather(
        #
        stream_regular_task(),
        stream_structured_task(),
    )


asyncio.run(main())
