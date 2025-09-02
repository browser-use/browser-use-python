# BrowserUse Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fbrowser-use%2Fbrowser-use-python)
[![pypi](https://img.shields.io/pypi/v/browser-use)](https://pypi.python.org/pypi/browser-use)

The BrowserUse Python library provides convenient access to the BrowserUse APIs from Python.

## Two-Step QuickStart

1. ☝️ Get your API Key at [Browser Use Cloud](https://cloud.browser-use.com)...

1. ✌️ Automate the web!

```python
from browser_use_sdk import BrowserUse

client = BrowserUse(api_key="bu_...")

task = client.tasks.create_task(
    task="Search for the top 10 Hacker News posts and return the title and url."
    llm="gpt-4.1",
)

result = task.complete()

result.output
```

> The full API of this library can be found in [api.md](api.md).

## Structured Output with Pydantic

Browser Use Python SDK provides first class support for Pydantic models.

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
    task = await client.tasks.create(
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

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install browser-use-sdk[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import asyncio
from browser_use_sdk import DefaultAioHttpClient
from browser_use_sdk import AsyncBrowserUse


async def main() -> None:
    async with AsyncBrowserUse(
        api_key="My API Key",
        http_client=DefaultAioHttpClient(),
    ) as client:
        task = await client.tasks.run(
            task="Search for the top 10 Hacker News posts and return the title and url.",
        )
        print(task.done_output)


asyncio.run(main())
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from browser_use import BrowserUse

client = BrowserUse(
    ...,
)
response = client.tasks.with_raw_response.create_task(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.tasks.create_task(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from browser_use import BrowserUse

client = BrowserUse(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.tasks.create_task(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from browser_use import BrowserUse

client = BrowserUse(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `browser_use_sdk.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `browser_use_sdk.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `browser_use_sdk.APIError`.

```python
import browser_use_sdk
from browser_use_sdk import BrowserUse

client = BrowserUse()

try:
    client.tasks.create(
        task="Search for the top 10 Hacker News posts and return the title and url.",
    )
except browser_use_sdk.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except browser_use_sdk.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except browser_use_sdk.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from browser_use_sdk import BrowserUse

# Configure the default for all requests:
client = BrowserUse(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).tasks.create(
    task="Search for the top 10 Hacker News posts and return the title and url.",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from browser_use_sdk import BrowserUse

# Configure the default for all requests:
client = BrowserUse(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = BrowserUse(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).tasks.create(
    task="Search for the top 10 Hacker News posts and return the title and url.",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `BROWSER_USE_LOG` to `info`.

```shell
$ export BROWSER_USE_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from browser_use_sdk import BrowserUse

client = BrowserUse()
response = client.tasks.with_raw_response.create(
    task="Search for the top 10 Hacker News posts and return the title and url.",
)
print(response.headers.get('X-My-Header'))

task = response.parse()  # get the object that `tasks.create()` would have returned
print(task.id)
```

These methods return an [`APIResponse`](https://github.com/browser-use/browser-use-python/tree/main/src/browser_use_sdk/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/browser-use/browser-use-python/tree/main/src/browser_use_sdk/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from browser_use_sdk import BrowserUse, DefaultHttpxClient

client = BrowserUse(
    # Or use the `BROWSER_USE_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from browser_use_sdk import BrowserUse

with BrowserUse() as client:
  # make requests here
  ...

# HTTP client is now closed
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

## Installation

```sh
pip install browser-use
```

## Reference

A full reference for this library is available [here](https://github.com/browser-use/browser-use-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from browser_use import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.tasks.create_task(
    task="task",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from browser_use import AsyncBrowserUse

client = AsyncBrowserUse(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.tasks.create_task(
        task="task",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from browser_use.core.api_error import ApiError

try:
    client.tasks.create_task(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```
