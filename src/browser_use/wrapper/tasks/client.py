from browser_use.tasks.client import SyncClientWrapper, TasksClient


class BrowserUseTasksClient(TasksClient):
    """TasksClient with utility method overrides."""

    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
