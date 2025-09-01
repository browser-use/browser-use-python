# Reference
## Accounts
<details><summary><code>client.accounts.<a href="src/browser_use/accounts/client.py">get_account_me</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get authenticated account information including credit balances and account details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.accounts.get_account_me()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tasks
<details><summary><code>client.tasks.<a href="src/browser_use/tasks/client.py">list_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of AI agent tasks with optional filtering by session and status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.tasks.list_tasks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_by:** `typing.Optional[TaskStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/browser_use/tasks/client.py">create_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can either:
1. Start a new task (auto creates a new simple session)
2. Start a new task in an existing session (you can create a custom session before starting the task and reuse it for follow-up tasks)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.tasks.create_task(
    task="task",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task:** `str` — The task prompt/instruction for the agent.
    
</dd>
</dl>

<dl>
<dd>

**llm:** `typing.Optional[SupportedLlMs]` — The LLM model to use for the agent.
    
</dd>
</dl>

<dl>
<dd>

**start_url:** `typing.Optional[str]` — The URL to start the task from.
    
</dd>
</dl>

<dl>
<dd>

**max_steps:** `typing.Optional[int]` — Maximum number of steps the agent can take before stopping.
    
</dd>
</dl>

<dl>
<dd>

**structured_output:** `typing.Optional[str]` — The stringified JSON schema for the structured output.
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — The ID of the session where the task will run.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The metadata for the task.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The secrets for the task.
    
</dd>
</dl>

<dl>
<dd>

**allowed_domains:** `typing.Optional[typing.Sequence[str]]` — The allowed domains for the task.
    
</dd>
</dl>

<dl>
<dd>

**highlight_elements:** `typing.Optional[bool]` — Tells the agent to highlight interactive elements on the page.
    
</dd>
</dl>

<dl>
<dd>

**flash_mode:** `typing.Optional[bool]` — Whether agent flash mode is enabled.
    
</dd>
</dl>

<dl>
<dd>

**thinking:** `typing.Optional[bool]` — Whether agent thinking mode is enabled.
    
</dd>
</dl>

<dl>
<dd>

**vision:** `typing.Optional[bool]` — Whether agent vision capabilities are enabled.
    
</dd>
</dl>

<dl>
<dd>

**system_prompt_extension:** `typing.Optional[str]` — Optional extension to the agent system prompt.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/browser_use/tasks/client.py">get_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed task information including status, progress, steps, and file outputs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.tasks.get_task(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/browser_use/tasks/client.py">update_task</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Control task execution with stop, pause, resume, or stop task and session actions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.tasks.update_task(
    task_id="task_id",
    action="stop",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `TaskUpdateAction` — The action to perform on the task
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tasks.<a href="src/browser_use/tasks/client.py">get_task_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get secure download URL for task execution logs with step-by-step details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.tasks.get_task_logs(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sessions
<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">list_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of AI agent sessions with optional status filtering.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.list_sessions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**filter_by:** `typing.Optional[SessionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">create_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new session with a new task.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.create_session()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**proxy:** `typing.Optional[ProxySettings]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">get_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed session information including status, URLs, and task details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.get_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">delete_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a session and all associated data.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.delete_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">update_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a session and all its running tasks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.update_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">get_session_public_share</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get public share information including URL and usage statistics.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.get_session_public_share(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">create_session_public_share</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or return existing public share for a session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.create_session_public_share(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/browser_use/sessions/client.py">delete_session_public_share</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove public share for a session.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.sessions.delete_session_public_share(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/browser_use/files/client.py">user_upload_file_presigned_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a secure presigned URL for uploading files that AI agents can use during tasks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.files.user_upload_file_presigned_url(
    session_id="session_id",
    file_name="fileName",
    content_type="image/jpg",
    size_bytes=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `Contenttype` 
    
</dd>
</dl>

<dl>
<dd>

**size_bytes:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/browser_use/files/client.py">get_task_output_file_presigned_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get secure download URL for an output file generated by the AI agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.files.get_task_output_file_presigned_url(
    task_id="task_id",
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Profiles
<details><summary><code>client.profiles.<a href="src/browser_use/profiles/client.py">list_profiles</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of profiles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.profiles.list_profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_number:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/browser_use/profiles/client.py">create_profile</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Profiles allow you to preserve the state of the browser between tasks.

They are most commonly used to allow users to preserve the log-in state in the agent between tasks.
You'd normally create one profile per user and then use it for all their tasks.

You can create a new profile by calling this endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.profiles.create_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/browser_use/profiles/client.py">get_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get profile details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.profiles.get_profile(
    profile_id="profile_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.profiles.<a href="src/browser_use/profiles/client.py">delete_browser_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a browser profile and its configuration.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from browser_use import BrowserUse
from browser_use.environment import BrowserUseEnvironment

client = BrowserUse(
    api_key="YOUR_API_KEY",
    environment=BrowserUseEnvironment.PRODUCTION,
)
client.profiles.delete_browser_profile(
    profile_id="profile_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

