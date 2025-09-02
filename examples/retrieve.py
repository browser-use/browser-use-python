#!/usr/bin/env -S rye run python

import time
from typing import List

from pydantic import BaseModel

from browser_use_sdk import BrowserUse

# gets API Key from environment variable BROWSER_USE_API_KEY
client = BrowserUse()


# Regular Task
def retrieve_regular_task() -> None:
    """
    Retrieves a regular task and waits for it to finish.
    """

    print("Retrieving regular task...")

    regular_task = client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gemini-2.5-flash"},
    )

    print(f"Task ID: {regular_task.id}")

    while True:
        regular_status = client.tasks.retrieve(regular_task.id)
        print(regular_status.status)
        if regular_status.status == "finished":
            print(regular_status.done_output)
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

    structured_task = client.tasks.create(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        agent_settings={"llm": "gpt-4.1"},
        structured_output_json=SearchResult,
    )

    print(f"Task ID: {structured_task.id}")

    while True:
        structured_status = client.tasks.retrieve(task_id=structured_task.id, structured_output_json=SearchResult)
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
