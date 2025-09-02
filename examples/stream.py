#!/usr/bin/env -S rye run python

from typing import List

from pydantic import BaseModel

from browser_use import BrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = BrowserUse()


# Regular Task
def stream_regular_task() -> None:
    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Task ID: {task.id}")

    for res in task.stream():
        print(res.status)

        if len(res.steps) > 0:
            last_step = res.steps[-1]
            print(f"{last_step.url} ({last_step.next_goal})")
            for action in last_step.actions:
                print(f" - {action}")

        if res.status == "finished":
            print(res.done_output)

    print("Regular: DONE")


stream_regular_task()


# Structured Output
def stream_structured_task() -> None:
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
        structured_output_json=SearchResult,
    )

    print(f"Task ID: {task.id}")

    for res in task.stream():
        print(res.status)

        if res.status == "finished":
            if res.parsed_output is None:
                print("No output")
            else:
                for post in res.parsed_output.posts:
                    print(f" - {post.title} - {post.url}")
            break

    print("Done")


stream_structured_task()
