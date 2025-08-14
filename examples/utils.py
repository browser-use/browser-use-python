#!/usr/bin/env python3
"""
Utility functions for browser-use examples.
"""

import sys
import time
import threading
from typing import Callable

SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]


def spinner(render_text: Callable[[], str]) -> Callable[[], None]:
    """
    Start a spinner that updates the text every 100ms.

    Args:
        render_text: A function that returns the text to display.

    Returns:
        A function to stop the spinner.
    """
    frame_index = 0
    running = True

    def spin():
        nonlocal frame_index
        while running:
            frame = SPINNER_FRAMES[frame_index % len(SPINNER_FRAMES)]
            text = f"{frame} {render_text()}"

            # Clear line and write new text
            sys.stdout.write(f"\r{text}")
            sys.stdout.flush()

            frame_index += 1
            time.sleep(0.1)

    def stop():
        nonlocal running
        running = False
        # Clear the line
        sys.stdout.write("\r" + " " * 80 + "\r")
        sys.stdout.flush()

    # Start spinner in a daemon thread
    thread = threading.Thread(target=spin, daemon=True)
    thread.start()

    return stop
