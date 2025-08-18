# Users

## Me

Types:

```python
from browser_use_sdk.types.users import MeRetrieveResponse
```

Methods:

- <code title="get /users/me">client.users.me.<a href="./src/browser_use_sdk/resources/users/me/me.py">retrieve</a>() -> <a href="./src/browser_use_sdk/types/users/me_retrieve_response.py">MeRetrieveResponse</a></code>

### Files

Types:

```python
from browser_use_sdk.types.users.me import FileCreatePresignedURLResponse
```

Methods:

- <code title="post /users/me/files/presigned-url">client.users.me.files.<a href="./src/browser_use_sdk/resources/users/me/files.py">create_presigned_url</a>(\*\*<a href="src/browser_use_sdk/types/users/me/file_create_presigned_url_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/users/me/file_create_presigned_url_response.py">FileCreatePresignedURLResponse</a></code>

# Tasks

Types:

```python
from browser_use_sdk.types import (
    FileView,
    LlmModel,
    TaskItemView,
    TaskStatus,
    TaskStepView,
    TaskView,
    TaskCreateResponse,
    TaskListResponse,
    TaskGetLogsResponse,
    TaskGetOutputFileResponse,
    TaskGetUserUploadedFileResponse,
)
```

Methods:

- <code title="post /tasks">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">create</a>(\*\*<a href="src/browser_use_sdk/types/task_create_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">retrieve</a>(task_id) -> <a href="./src/browser_use_sdk/types/task_view.py">TaskView</a></code>
- <code title="patch /tasks/{task_id}">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">update</a>(task_id, \*\*<a href="src/browser_use_sdk/types/task_update_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/task_view.py">TaskView</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">list</a>(\*\*<a href="src/browser_use_sdk/types/task_list_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /tasks/{task_id}/logs">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">get_logs</a>(task_id) -> <a href="./src/browser_use_sdk/types/task_get_logs_response.py">TaskGetLogsResponse</a></code>
- <code title="get /tasks/{task_id}/output-files/{file_id}">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">get_output_file</a>(file_id, \*, task_id) -> <a href="./src/browser_use_sdk/types/task_get_output_file_response.py">TaskGetOutputFileResponse</a></code>
- <code title="get /tasks/{task_id}/user-uploaded-files/{file_id}">client.tasks.<a href="./src/browser_use_sdk/resources/tasks.py">get_user_uploaded_file</a>(file_id, \*, task_id) -> <a href="./src/browser_use_sdk/types/task_get_user_uploaded_file_response.py">TaskGetUserUploadedFileResponse</a></code>

# Sessions

Types:

```python
from browser_use_sdk.types import SessionStatus, SessionView, SessionListResponse
```

Methods:

- <code title="get /sessions/{session_id}">client.sessions.<a href="./src/browser_use_sdk/resources/sessions/sessions.py">retrieve</a>(session_id) -> <a href="./src/browser_use_sdk/types/session_view.py">SessionView</a></code>
- <code title="patch /sessions/{session_id}">client.sessions.<a href="./src/browser_use_sdk/resources/sessions/sessions.py">update</a>(session_id, \*\*<a href="src/browser_use_sdk/types/session_update_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/session_view.py">SessionView</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/browser_use_sdk/resources/sessions/sessions.py">list</a>(\*\*<a href="src/browser_use_sdk/types/session_list_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /sessions/{session_id}">client.sessions.<a href="./src/browser_use_sdk/resources/sessions/sessions.py">delete</a>(session_id) -> None</code>

## PublicShare

Types:

```python
from browser_use_sdk.types.sessions import ShareView
```

Methods:

- <code title="post /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use_sdk/resources/sessions/public_share.py">create</a>(session_id) -> <a href="./src/browser_use_sdk/types/sessions/share_view.py">ShareView</a></code>
- <code title="get /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use_sdk/resources/sessions/public_share.py">retrieve</a>(session_id) -> <a href="./src/browser_use_sdk/types/sessions/share_view.py">ShareView</a></code>
- <code title="delete /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use_sdk/resources/sessions/public_share.py">delete</a>(session_id) -> None</code>

# BrowserProfiles

Types:

```python
from browser_use_sdk.types import BrowserProfileView, ProxyCountryCode, BrowserProfileListResponse
```

Methods:

- <code title="post /browser-profiles">client.browser_profiles.<a href="./src/browser_use_sdk/resources/browser_profiles.py">create</a>(\*\*<a href="src/browser_use_sdk/types/browser_profile_create_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="get /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use_sdk/resources/browser_profiles.py">retrieve</a>(profile_id) -> <a href="./src/browser_use_sdk/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="patch /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use_sdk/resources/browser_profiles.py">update</a>(profile_id, \*\*<a href="src/browser_use_sdk/types/browser_profile_update_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="get /browser-profiles">client.browser_profiles.<a href="./src/browser_use_sdk/resources/browser_profiles.py">list</a>(\*\*<a href="src/browser_use_sdk/types/browser_profile_list_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/browser_profile_list_response.py">BrowserProfileListResponse</a></code>
- <code title="delete /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use_sdk/resources/browser_profiles.py">delete</a>(profile_id) -> None</code>

# AgentProfiles

Types:

```python
from browser_use_sdk.types import AgentProfileView, AgentProfileListResponse
```

Methods:

- <code title="post /agent-profiles">client.agent_profiles.<a href="./src/browser_use_sdk/resources/agent_profiles.py">create</a>(\*\*<a href="src/browser_use_sdk/types/agent_profile_create_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="get /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use_sdk/resources/agent_profiles.py">retrieve</a>(profile_id) -> <a href="./src/browser_use_sdk/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="patch /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use_sdk/resources/agent_profiles.py">update</a>(profile_id, \*\*<a href="src/browser_use_sdk/types/agent_profile_update_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="get /agent-profiles">client.agent_profiles.<a href="./src/browser_use_sdk/resources/agent_profiles.py">list</a>(\*\*<a href="src/browser_use_sdk/types/agent_profile_list_params.py">params</a>) -> <a href="./src/browser_use_sdk/types/agent_profile_list_response.py">AgentProfileListResponse</a></code>
- <code title="delete /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use_sdk/resources/agent_profiles.py">delete</a>(profile_id) -> None</code>
