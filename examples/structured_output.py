#!/usr/bin/env python3
"""
Structured output example for browser-use Python library.

This example demonstrates:
1. Defining Pydantic models for structured output
2. Creating tasks with structured output schemas
3. Parsing and validating the results
4. Type-safe access to task outputs

Usage:
    python examples/structured_output.py
"""

import os
import time
from typing import List

from pydantic import Field, BaseModel

from browser_use import BrowserUse
from utils import spinner


# Define structured output schemas using Pydantic
class HackerNewsPost(BaseModel):
    """Schema for a single Hacker News post."""

    title: str = Field(description="The title of the post")
    url: str = Field(description="The URL of the post")
    score: int = Field(description="The score/points of the post")


class TaskOutput(BaseModel):
    """Schema for the complete task output."""

    posts: List[HackerNewsPost] = Field(description="List of top Hacker News posts", min_items=1, max_items=10)


def main():
    """Main function demonstrating structured output usage."""
    # Get API key from environment variable
    api_key = os.getenv("BROWSER_USE_API_KEY")
    if not api_key:
        print("Error: BROWSER_USE_API_KEY environment variable not set")
        print("Please set your API key: export BROWSER_USE_API_KEY='your-api-key'")
        return

    # Initialize the client
    browser_use = BrowserUse(api_key=api_key)

    print("🚀 Creating task with structured output...")
    print("📋 Expected output schema:")
    print("   - List of up to 10 Hacker News posts")
    print("   - Each post has: title, URL, and score")

    # Create a task with structured output
    response = browser_use.tasks.create_with_structured_output(
        task="Extract the top 10 Hacker News posts and return the title, URL, and score for each",
        structured_output_json=TaskOutput,
    )

    print(f"✅ Task created with ID: {response.id}")
    print(f"📝 Task: {response.task}")
    print(f"🤖 LLM Model: {response.llm}")
    print(f"🔄 Status: {response.status}")

    if response.session_live_url:
        print(f"🔗 Live session: {response.session_live_url}")

    # Poll for completion
    print("\n⏳ Waiting for task completion...")
    log_message = "starting"
    stop_spinner = spinner(lambda: log_message)

    try:
        while True:
            # Wait a bit before checking
            time.sleep(2)

            # Get task status with structured output parsing
            status = browser_use.tasks.retrieve_with_structured_output(response.id, structured_output_json=TaskOutput)

            if status.status == "finished":
                stop_spinner()
                print(f"\n✅ Task completed!")

                # Access the structured output
                if status.done_output is not None:
                    print("\n📊 STRUCTURED OUTPUT:")
                    print("=" * 50)

                    # Type-safe access to the parsed data
                    for i, post in enumerate(status.done_output.posts, 1):
                        print(f"{i:2d}. {post.title}")
                        print(f"    Score: {post.score} | URL: {post.url}")
                        print()

                    print(f"Total posts extracted: {len(status.done_output.posts)}")
                else:
                    print("❌ No structured output available")
                    print("This might happen if the task output couldn't be parsed")

                # Show additional task information
                if status.steps:
                    print(f"\n📋 Total execution steps: {len(status.steps)}")
                    if status.steps:
                        last_step = status.steps[-1]
                        print(f"🎯 Final goal: {last_step.next_goal}")

                break

            elif status.status in ["started", "paused", "stopped"]:
                steps_count = len(status.steps) if status.steps else 0
                steps_info = f"({steps_count} steps)"

                if status.steps and status.steps[-1].next_goal:
                    last_goal = status.steps[-1].next_goal
                    steps_info += f", last: {last_goal}"

                live_url_info = ""
                if status.session_live_url:
                    live_url_info = f", live: {status.session_live_url}"

                log_message = f"agent {status.status} {steps_info}{live_url_info}"
                # Update the spinner message by redefining the lambda
                stop_spinner = spinner(lambda: log_message)
            else:
                print(f"\n❌ Unexpected status: {status.status}")
                break

    except KeyboardInterrupt:
        stop_spinner()
        print("\n\n⏹️  Task monitoring interrupted by user")
        print("Note: The task will continue running on the server")
    except Exception as e:
        stop_spinner()
        print(f"\n❌ Error: {e}")


def demonstrate_schema_validation():
    """Demonstrate how the Pydantic schema validation works."""
    print("\n🔍 SCHEMA VALIDATION DEMO:")
    print("=" * 40)

    # Valid data
    try:
        valid_data = {"posts": [{"title": "Test Post", "url": "https://example.com", "score": 100}]}
        result = TaskOutput.model_validate(valid_data)
        print("✅ Valid data accepted")
        print(f"   First post title: {result.posts[0].title}")
    except Exception as e:
        print(f"❌ Unexpected validation error: {e}")

    # Invalid data (missing required field)
    try:
        invalid_data = {
            "posts": [
                {"title": "Test Post", "url": "https://example.com"}
                # Missing 'score' field
            ]
        }
        TaskOutput.model_validate(invalid_data)
        print("❌ Invalid data was accepted (this shouldn't happen)")
    except Exception as e:
        print("✅ Invalid data correctly rejected")
        print(f"   Error: {e}")


if __name__ == "__main__":
    # Show schema validation demo
    demonstrate_schema_validation()

    # Run the main example
    print("\n" + "=" * 60)
    main()
