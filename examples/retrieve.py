#!/usr/bin/env -S poetry run python

import time
from typing import List

from api import API_KEY
from pydantic import BaseModel

from browser_use_sdk import BrowserUse

client = BrowserUse(api_key=API_KEY)


# Regular Task
def retrieve_regular_task() -> None:
    """
    Retrieves a regular task and waits for it to finish.
    """

    print("Retrieving regular task...")

    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gemini-2.5-flash",
    )

    print(f"Task ID: {task.id}")

    while True:
        regular_status = client.tasks.get_task(task.id)
        print(regular_status.status)
        if regular_status.status == "finished":
            print(regular_status.output)
            break

        time.sleep(1)

    print("Done")


retrieve_regular_task()


def retrieve_structured_task() -> None:
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

    task = client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        llm="gpt-4.1",
        schema=SearchResult,
    )

    print(f"Task ID: {task.id}")

    while True:
        structured_status = client.tasks.get_task(task_id=task.id, schema=SearchResult)
        print(structured_status.status)

        if structured_status.status == "finished":
            if structured_status.parsed_output is None:
                print("No output")
            else:
                for post in structured_status.parsed_output.posts:
                    print(f" - {post.title} - {post.url}")

            break

        time.sleep(1)

    print("Done")


retrieve_structured_task()
