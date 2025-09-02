import os

_API_KEY = os.getenv("BROWSER_USE_API_KEY")
if not _API_KEY:
    raise RuntimeError("BROWSER_USE_API_KEY environment variable is not set")

API_KEY = _API_KEY
