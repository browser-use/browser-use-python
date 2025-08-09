# Tasks

Types:

```python
from browser_use.types import (
    LlmModel,
    TaskStatus,
    TaskView,
    TaskRetrieveResponse,
    TaskListResponse,
    TaskRetrieveLogsResponse,
    TaskRetrieveOutputFileResponse,
)
```

Methods:

- <code title="post /tasks">client.tasks.<a href="./src/browser_use/resources/tasks.py">create</a>(\*\*<a href="src/browser_use/types/task_create_params.py">params</a>) -> <a href="./src/browser_use/types/task_view.py">TaskView</a></code>
- <code title="get /tasks/{task_id}">client.tasks.<a href="./src/browser_use/resources/tasks.py">retrieve</a>(task_id, \*\*<a href="src/browser_use/types/task_retrieve_params.py">params</a>) -> <a href="./src/browser_use/types/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="patch /tasks/{task_id}">client.tasks.<a href="./src/browser_use/resources/tasks.py">update</a>(task_id, \*\*<a href="src/browser_use/types/task_update_params.py">params</a>) -> <a href="./src/browser_use/types/task_view.py">TaskView</a></code>
- <code title="get /tasks">client.tasks.<a href="./src/browser_use/resources/tasks.py">list</a>(\*\*<a href="src/browser_use/types/task_list_params.py">params</a>) -> <a href="./src/browser_use/types/task_list_response.py">TaskListResponse</a></code>
- <code title="get /tasks/{task_id}/logs">client.tasks.<a href="./src/browser_use/resources/tasks.py">retrieve_logs</a>(task_id) -> <a href="./src/browser_use/types/task_retrieve_logs_response.py">TaskRetrieveLogsResponse</a></code>
- <code title="get /tasks/{task_id}/output-files/{file_name}">client.tasks.<a href="./src/browser_use/resources/tasks.py">retrieve_output_file</a>(file_name, \*, task_id) -> <a href="./src/browser_use/types/task_retrieve_output_file_response.py">TaskRetrieveOutputFileResponse</a></code>

# Sessions

Types:

```python
from browser_use.types import SessionStatus, SessionView, SessionListResponse
```

Methods:

- <code title="get /sessions/{session_id}">client.sessions.<a href="./src/browser_use/resources/sessions/sessions.py">retrieve</a>(session_id, \*\*<a href="src/browser_use/types/session_retrieve_params.py">params</a>) -> <a href="./src/browser_use/types/session_view.py">SessionView</a></code>
- <code title="patch /sessions/{session_id}">client.sessions.<a href="./src/browser_use/resources/sessions/sessions.py">update</a>(session_id, \*\*<a href="src/browser_use/types/session_update_params.py">params</a>) -> <a href="./src/browser_use/types/session_view.py">SessionView</a></code>
- <code title="get /sessions">client.sessions.<a href="./src/browser_use/resources/sessions/sessions.py">list</a>(\*\*<a href="src/browser_use/types/session_list_params.py">params</a>) -> <a href="./src/browser_use/types/session_list_response.py">SessionListResponse</a></code>

## PublicShare

Types:

```python
from browser_use.types.sessions import ShareView
```

Methods:

- <code title="post /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use/resources/sessions/public_share.py">create</a>(session_id) -> <a href="./src/browser_use/types/sessions/share_view.py">ShareView</a></code>
- <code title="get /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use/resources/sessions/public_share.py">retrieve</a>(session_id) -> <a href="./src/browser_use/types/sessions/share_view.py">ShareView</a></code>
- <code title="delete /sessions/{session_id}/public-share">client.sessions.public_share.<a href="./src/browser_use/resources/sessions/public_share.py">delete</a>(session_id) -> object</code>

# BrowserProfiles

Types:

```python
from browser_use.types import BrowserProfileView, ProxyCountryCode, BrowserProfileListResponse
```

Methods:

- <code title="post /browser-profiles">client.browser_profiles.<a href="./src/browser_use/resources/browser_profiles.py">create</a>(\*\*<a href="src/browser_use/types/browser_profile_create_params.py">params</a>) -> <a href="./src/browser_use/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="get /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use/resources/browser_profiles.py">retrieve</a>(profile_id) -> <a href="./src/browser_use/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="patch /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use/resources/browser_profiles.py">update</a>(profile_id, \*\*<a href="src/browser_use/types/browser_profile_update_params.py">params</a>) -> <a href="./src/browser_use/types/browser_profile_view.py">BrowserProfileView</a></code>
- <code title="get /browser-profiles">client.browser_profiles.<a href="./src/browser_use/resources/browser_profiles.py">list</a>(\*\*<a href="src/browser_use/types/browser_profile_list_params.py">params</a>) -> <a href="./src/browser_use/types/browser_profile_list_response.py">BrowserProfileListResponse</a></code>
- <code title="delete /browser-profiles/{profile_id}">client.browser_profiles.<a href="./src/browser_use/resources/browser_profiles.py">delete</a>(profile_id) -> object</code>

# AgentProfiles

Types:

```python
from browser_use.types import AgentProfileView, AgentProfileListResponse
```

Methods:

- <code title="post /agent-profiles">client.agent_profiles.<a href="./src/browser_use/resources/agent_profiles.py">create</a>(\*\*<a href="src/browser_use/types/agent_profile_create_params.py">params</a>) -> <a href="./src/browser_use/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="get /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use/resources/agent_profiles.py">retrieve</a>(profile_id) -> <a href="./src/browser_use/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="patch /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use/resources/agent_profiles.py">update</a>(profile_id, \*\*<a href="src/browser_use/types/agent_profile_update_params.py">params</a>) -> <a href="./src/browser_use/types/agent_profile_view.py">AgentProfileView</a></code>
- <code title="get /agent-profiles">client.agent_profiles.<a href="./src/browser_use/resources/agent_profiles.py">list</a>(\*\*<a href="src/browser_use/types/agent_profile_list_params.py">params</a>) -> <a href="./src/browser_use/types/agent_profile_list_response.py">AgentProfileListResponse</a></code>
- <code title="delete /agent-profiles/{profile_id}">client.agent_profiles.<a href="./src/browser_use/resources/agent_profiles.py">delete</a>(profile_id) -> object</code>
