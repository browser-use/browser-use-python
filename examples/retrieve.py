#!/usr/bin/env -S rye run python

import time
from typing import List

from pydantic import BaseModel

from browser_use_sdk import BrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = BrowserUse()

# Regular Task
task = client.tasks.create(
    task="""
    Find top 10 Hacker News articles and return the title and url.
    """
)

print(f"Task ID: {task.id}")

while True:
    regular = client.tasks.retrieve(task.id)
    print(regular.status)
    if regular.status == "finished":
        print(regular.done_output)
        break

    time.sleep(1)


# Structured Output
class HackerNewsPost(BaseModel):
    title: str
    url: str


class SearchResult(BaseModel):
    posts: List[HackerNewsPost]


structured = client.tasks.create(
    task="""
    Find top 10 Hacker News articles and return the title and url.
    """,
    structured_output_json=SearchResult,
)

print(f"Task ID: {structured.id}")

while True:
    structured = client.tasks.retrieve(task_id=structured.id, structured_output_json=SearchResult)
    print(structured.status)

    if structured.status == "finished":
        if structured.parsed_output is None:
            print("No output")
        else:
            for post in structured.parsed_output.posts:
                print(f" - {post.title} - {post.url}")

        break

    time.sleep(1)
