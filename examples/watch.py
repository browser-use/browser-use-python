#!/usr/bin/env -S poetry run python

from typing import List

from api import API_KEY
from pydantic import BaseModel

from browser_use import BrowserUse

client = BrowserUse(api_key=API_KEY)


# Regular Task
def watch_regular_task() -> None:
    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Task ID: {task.id}")

    for state in task.watch():
        print(f"Regular Task Status: {state.status}")

        if state.status == "finished":
            print(f"Regular Task Output: {state.output}")
            break

    print("Regular: DONE")


watch_regular_task()


# Structured Output
def watch_structured_task() -> None:
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

    for state in task.watch():
        print(f"Structured Task Status: {state.status}")

        if state.status == "finished":
            print(f"Structured Task Output: {state.output}")

            if state.parsed_output is not None:
                for post in state.parsed_output.posts:
                    print(f" - {post.title} - {post.url}")
            else:
                print("No output...")

            break

    print("Structured Task Done")


watch_structured_task()
