#!/usr/bin/env -S poetry run python

from typing import List

from pydantic import BaseModel
from utils import API_KEY

from browser_use import BrowserUse

client = BrowserUse(api_key=API_KEY)


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

    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gpt-4.1",
        schema=SearchResult,
    )

    print(f"Task ID: {task.id}")

    result = task.complete()

    if result.parsed_output is not None:
        for post in result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

    print("Done")


run_structured_task()
