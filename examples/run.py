#!/usr/bin/env -S rye run python

from typing import List

from pydantic import BaseModel

from browser_use import BrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = BrowserUse()


# Regular Task
def run_regular_task() -> None:
    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Task ID: {task.id}")

    result = task.complete()

    print(result.output)

    print("Done")


run_regular_task()


# Structured Output
def run_structured_task() -> None:
    class HackerNewsPost(BaseModel):
        title: str
        url: str

    class SearchResult(BaseModel):
        posts: List[HackerNewsPost]

    structured_result = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gpt-4.1",
        structured_output_json=SearchResult,
    )

    print(f"Task ID: {structured_result.id}")

    if structured_result.parsed_output is not None:
        for post in structured_result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

    print("Done")


run_structured_task()
