<img src="https://raw.githubusercontent.com/browser-use/browser-use-python/refs/heads/main/assets/cloud-banner-python.png" alt="Browser Use Python" width="full"/>

# BrowserUse Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fbrowser-use%2Fbrowser-use-python)
[![pypi](https://img.shields.io/pypi/v/browser-use)](https://pypi.python.org/pypi/browser-use)

The BrowserUse Python library provides convenient access to the BrowserUse APIs from Python.

## Three-Step QuickStart

1. 📦 Install Browser Use SDK

   ```sh
   # PIP
   pip install browser-use-sdk

   # Poetry
   poetry add browser-use-sdk

   # UV
   uv add browser-use-sdk
   ```

1. 🔑 Get your API Key at [Browser Use Cloud](https://cloud.browser-use.com)!

1. 🦄 Automate the Internet!

   ```python
   from browser_use_sdk import BrowserUse

   client = BrowserUse(api_key="bu_...")

   task = client.tasks.create_task(
       task="Search for the top 10 Hacker News posts and return the title and url.",
       llm="gpt-4.1"
   )

   result = task.complete()

   result.output
   ```

> The full API of this library can be found in [api.md](api.md).

## Structured Output with Pydantic

Browser Use Python SDK provides first class support for Pydantic models.

```py
from browser_use_sdk import AsyncBrowserUse

client = AsyncBrowserUse(api_key=API_KEY)

class HackerNewsPost(BaseModel):
    title: str
    url: str

class SearchResult(BaseModel):
    posts: List[HackerNewsPost]

async def main() -> None:
    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        schema=SearchResult,
    )

    result = await task.complete()

    if result.parsed_output is not None:
        print("Top HackerNews Posts:")
        for post in result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

asyncio.run(main())
```

## Streaming Updates with Async Iterators

> When presenting a long running task you might want to show updates as they happen.

Browser Use SDK exposes a `.stream` method that lets you subscribe to a sync or an async generator that automatically polls Browser Use Cloud servers and emits a new event when an update happens (e.g., live url becomes available, agent takes a new step, or agent completes the task).

```py
class HackerNewsPost(BaseModel):
    title: str
    url: str

class SearchResult(BaseModel):
    posts: List[HackerNewsPost]


async def main() -> None:
    task = await client.tasks.create_task(
        task="""
        Find top 10 Hacker News articles and return the title and url.
        """,
        schema=SearchResult,
    )

    async for step in task.stream():
        print(f"Step {step.number}: {step.url} ({step.next_goal})")

    result = await task.complete()

    if result.parsed_output is not None:
        print("Top HackerNews Posts:")
        for post in result.parsed_output.posts:
            print(f" - {post.title} - {post.url}")

asyncio.run(main())
```

## Verifying Webhook Events

> You can configure Browser Use Cloud to emit Webhook events and process them easily with Browser Use Python SDK.

Browser Use SDK lets you easily verify the signature and structure of the payload you receive in the webhook.

```py
import uvicorn
import os
from browser_use_sdk import Webhook, verify_webhook_event_signature

from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

SECRET_KEY = os.environ['SECRET_KEY']

@app.post('/webhook')
async def webhook(request: Request):
    body = await request.json()

    timestamp = request.headers.get('X-Browser-Use-Timestamp')
    signature = request.headers.get('X-Browser-Use-Signature')

    verified_webhook: Webhook = verify_webhook_event_signature(
        body=body,
        timestamp=timestamp,
        secret=SECRET_KEY,
        expected_signature=signature,
    )

    if verified_webhook is not None:
        print('Webhook received:', verified_webhook)
    else:
        print('Invalid webhook received')

    return {'status': 'success', 'message': 'Webhook received'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
```

## Async usage

Simply import `AsyncBrowserUse` instead of `BrowserUse` and use `await` with each API call:

```python
import os
import asyncio
from browser_use_sdk import AsyncBrowserUse

client = AsyncBrowserUse(
    api_key=os.environ.get("BROWSER_USE_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    task = await client.tasks.create_task(
        task="Search for the top 10 Hacker News posts and return the title and url.",
    )

    print(task.id)


asyncio.run(main())
```

## Requirements

Python 3.8 or higher.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

## Reference

A full reference for this library is available [here](https://github.com/browser-use/browser-use-python/blob/HEAD/./reference.md).
