#!/usr/bin/env python3
"""
Basic demo example for browser-use Python library.

This example demonstrates:
1. Creating a task
2. Polling for task completion
3. Displaying the results

Usage:
    python examples/demo.py
"""

import os
import time

from utils import spinner

from browser_use import BrowserUse
from browser_use.types.task_view import TaskView


def main():
    """Main function demonstrating basic task usage."""
    # Get API key from environment variable
    api_key = os.getenv("BROWSER_USE_API_KEY")
    if not api_key:
        print("Error: BROWSER_USE_API_KEY environment variable not set")
        print("Please set your API key: export BROWSER_USE_API_KEY='your-api-key'")
        return

    # Initialize the client
    browser_use = BrowserUse(api_key=api_key)

    print("🚀 Creating task...")

    # Create a simple task
    response = browser_use.tasks.create(task="What's the current weather in San Francisco and what's the temperature?")

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

            # Get task status
            status = browser_use.tasks.retrieve(response.id, status_only=False)

            # Handle different status types
            if isinstance(status, TaskView):
                if status.status == "finished":
                    stop_spinner()
                    print(f"\n✅ Task completed!")
                    print(f"📊 Output: {status.done_output}")

                    if status.steps:
                        print(f"📋 Total steps: {len(status.steps)}")
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
            else:
                print(f"\n❌ Unexpected response type: {type(status)}")
                break

    except KeyboardInterrupt:
        stop_spinner()
        print("\n\n⏹️  Task monitoring interrupted by user")
        print("Note: The task will continue running on the server")
    except Exception as e:
        stop_spinner()
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
