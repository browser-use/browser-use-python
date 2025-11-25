# Reference
## Billing
<details><summary><code>client.billing.<a href="src/browser_use_sdk/billing/client.py">get_account_billing</a>()</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.billing.get_account_billing()

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
<details><summary><code>client.tasks.<a href="src/browser_use_sdk/tasks/client.py">list_tasks</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.tasks.<a href="src/browser_use_sdk/tasks/client.py">create_task</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The metadata for the task. Up to 10 key-value pairs.
    
</dd>
</dl>

<dl>
<dd>

**secrets:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — The secrets for the task. Allowed domains are not required for secrets to be injected, but are recommended.
    
</dd>
</dl>

<dl>
<dd>

**allowed_domains:** `typing.Optional[typing.Sequence[str]]` — The allowed domains for the task.
    
</dd>
</dl>

<dl>
<dd>

**op_vault_id:** `typing.Optional[str]` — The ID of the 1Password vault to use for the task. This is used to inject secrets into the task.
    
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

**vision:** `typing.Optional[CreateTaskRequestVision]` — Whether agent vision capabilities are enabled. Set to 'auto' to let the agent decide based on the model capabilities.
    
</dd>
</dl>

<dl>
<dd>

**system_prompt_extension:** `typing.Optional[str]` — Optional extension to the agent system prompt.
    
</dd>
</dl>

<dl>
<dd>

**judge:** `typing.Optional[bool]` — Enable judge mode to evaluate task completion against ground truth.
    
</dd>
</dl>

<dl>
<dd>

**judge_ground_truth:** `typing.Optional[str]` — Expected answer for judge evaluation.
    
</dd>
</dl>

<dl>
<dd>

**judge_llm:** `typing.Optional[SupportedLlMs]` — The LLM model to use for judging. If not provided, uses the default judge LLM.
    
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

<details><summary><code>client.tasks.<a href="src/browser_use_sdk/tasks/client.py">get_task</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.tasks.<a href="src/browser_use_sdk/tasks/client.py">update_task</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.tasks.<a href="src/browser_use_sdk/tasks/client.py">get_task_logs</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">list_sessions</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">create_session</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

**profile_id:** `typing.Optional[str]` — The ID of the profile to use for the session
    
</dd>
</dl>

<dl>
<dd>

**proxy_country_code:** `typing.Optional[ProxyCountryCode]` — Country code for proxy location.
    
</dd>
</dl>

<dl>
<dd>

**start_url:** `typing.Optional[str]` — URL to navigate to when the session starts.
    
</dd>
</dl>

<dl>
<dd>

**browser_screen_width:** `typing.Optional[int]` — Custom screen width in pixels for the browser.
    
</dd>
</dl>

<dl>
<dd>

**browser_screen_height:** `typing.Optional[int]` — Custom screen height in pixels for the browser.
    
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">get_session</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">delete_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a session with all its tasks.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">update_session</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">get_session_public_share</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">create_session_public_share</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.sessions.<a href="src/browser_use_sdk/sessions/client.py">delete_session_public_share</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.files.<a href="src/browser_use_sdk/files/client.py">agent_session_upload_file_presigned_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a secure presigned URL for uploading files to an agent session.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.files.agent_session_upload_file_presigned_url(
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

**file_name:** `str` — The name of the file to upload
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `UploadFileRequestContentType` — The content type of the file to upload
    
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

<details><summary><code>client.files.<a href="src/browser_use_sdk/files/client.py">browser_session_upload_file_presigned_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a secure presigned URL for uploading files to a browser session.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.files.browser_session_upload_file_presigned_url(
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

**file_name:** `str` — The name of the file to upload
    
</dd>
</dl>

<dl>
<dd>

**content_type:** `UploadFileRequestContentType` — The content type of the file to upload
    
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

<details><summary><code>client.files.<a href="src/browser_use_sdk/files/client.py">get_task_output_file_presigned_url</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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
<details><summary><code>client.profiles.<a href="src/browser_use_sdk/profiles/client.py">list_profiles</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.profiles.<a href="src/browser_use_sdk/profiles/client.py">create_profile</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

**name:** `typing.Optional[str]` — Optional name for the profile
    
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

<details><summary><code>client.profiles.<a href="src/browser_use_sdk/profiles/client.py">get_profile</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.profiles.<a href="src/browser_use_sdk/profiles/client.py">delete_browser_profile</a>(...)</code></summary>
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
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

<details><summary><code>client.profiles.<a href="src/browser_use_sdk/profiles/client.py">update_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a browser profile's information.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.profiles.update_profile(
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

**name:** `typing.Optional[str]` — Optional name for the profile
    
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

## Browsers
<details><summary><code>client.browsers.<a href="src/browser_use_sdk/browsers/client.py">list_browser_sessions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of browser sessions with optional status filtering.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.browsers.list_browser_sessions()

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

**filter_by:** `typing.Optional[BrowserSessionStatus]` 
    
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

<details><summary><code>client.browsers.<a href="src/browser_use_sdk/browsers/client.py">create_browser_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new browser session.

**Pricing:** Browser sessions are charged at $0.05 per hour.
The full hourly rate is charged upfront when the session starts.
When you stop the session, any unused time is automatically refunded proportionally.

Billing is rounded to the nearest minute (minimum 1 minute).
For example, if you stop a session after 30 minutes, you'll be refunded $0.025.

**Session Limits:**
- Free users (without active subscription): Maximum 15 minutes per session
- Paid subscribers: Up to 4 hours per session
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.browsers.create_browser_session()

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

**profile_id:** `typing.Optional[str]` — The ID of the profile to use for the session
    
</dd>
</dl>

<dl>
<dd>

**proxy_country_code:** `typing.Optional[ProxyCountryCode]` — Country code for proxy location.
    
</dd>
</dl>

<dl>
<dd>

**timeout:** `typing.Optional[int]` — The timeout for the session in minutes. Free users are limited to 15 minutes, paid users can use up to 240 minutes (4 hours).
    
</dd>
</dl>

<dl>
<dd>

**browser_screen_width:** `typing.Optional[int]` — Custom screen width in pixels for the browser.
    
</dd>
</dl>

<dl>
<dd>

**browser_screen_height:** `typing.Optional[int]` — Custom screen height in pixels for the browser.
    
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

<details><summary><code>client.browsers.<a href="src/browser_use_sdk/browsers/client.py">get_browser_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed browser session information including status and URLs.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.browsers.get_browser_session(
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

<details><summary><code>client.browsers.<a href="src/browser_use_sdk/browsers/client.py">update_browser_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a browser session.

**Refund:** When you stop a session, unused time is automatically refunded.
If the session ran for less than 1 hour, you'll receive a proportional refund.
Billing is ceil to the nearest minute (minimum 1 minute).
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.browsers.update_browser_session(
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

## Workflows
<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">list_workflows</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of workflows with optional filtering.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.list_workflows()

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

**is_archived:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">create_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new workflow. The workflow YAML should be uploaded separately via the update endpoint.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.create_workflow(
    name="name",
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

**name:** `str` — Name of the workflow
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the workflow
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional variables/parameters for the workflow
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed workflow information including presigned URL to download YAML.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_workflow(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">delete_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Archive a workflow (soft delete).
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.delete_workflow(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">update_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update workflow metadata.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.update_workflow(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the workflow
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the workflow
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Variables/parameters for the workflow
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_workflow_generation_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get workflow generation state with live browser URL for polling.

This endpoint returns the current state of workflow generation including
the live browser URL (if available). It's designed to be polled every 2 seconds
during generation to show real-time browser activity in the frontend.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_workflow_generation_state(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_workflow_yaml_presigned_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a presigned URL to upload workflow YAML directly to S3 from the browser.

This avoids sending the YAML content through the backend, reducing latency
and avoiding KMS permission issues in local development.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_workflow_yaml_presigned_url(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**size_bytes:** `int` — Size of the YAML file in bytes
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` — The name of the YAML file to upload
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">run_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a workflow asynchronously.

Returns execution ID immediately and processes in background via Inngest.
Use the GET /workflows/executions/{execution_id} endpoint to check status and retrieve results.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.run_workflow(
    workflow_id="workflow_id",
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

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Input parameters for the workflow execution
    
</dd>
</dl>

<dl>
<dd>

**execution_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional metadata for this execution
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">generate_workflow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a workflow from a natural language task description.

This endpoint uses the workflow-use library's HealingService to:
1. Record browser interactions for the task
2. Convert interactions to a reusable workflow
3. Extract variables for parameterization
4. Save the generated YAML to S3

The generation happens asynchronously via the workflow_worker Lambda.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.generate_workflow(
    workflow_id="workflow_id",
    task_prompt="Go to github.com and search for browser-use",
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

**workflow_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**task_prompt:** `str` — Natural language description of the task to automate
    
</dd>
</dl>

<dl>
<dd>

**workflow_name:** `typing.Optional[str]` — Optional name for the generated workflow. If not provided, will be inferred from prompt.
    
</dd>
</dl>

<dl>
<dd>

**enable_variable_extraction:** `typing.Optional[bool]` — Whether to extract reusable variables from the workflow
    
</dd>
</dl>

<dl>
<dd>

**use_deterministic_conversion:** `typing.Optional[bool]` — Whether to use deterministic conversion (faster and cheaper)
    
</dd>
</dl>

<dl>
<dd>

**use_cloud_browser:** `typing.Optional[bool]` — Whether to use cloud browser for recording (recommended for production)
    
</dd>
</dl>

<dl>
<dd>

**enable_pattern_variable_identification:** `typing.Optional[bool]` — Enable pattern-based variable identification (no LLM, $0 cost)
    
</dd>
</dl>

<dl>
<dd>

**pattern_variable_confidence:** `typing.Optional[float]` — Minimum confidence threshold for pattern-based detection (0.0 to 1.0)
    
</dd>
</dl>

<dl>
<dd>

**enable_ai_validation:** `typing.Optional[bool]` — Enable AI validation to review and fix generated workflow
    
</dd>
</dl>

<dl>
<dd>

**cleanup_yaml:** `typing.Optional[bool]` — Remove verbose fields from generated YAML
    
</dd>
</dl>

<dl>
<dd>

**remove_descriptions:** `typing.Optional[bool]` — Remove step descriptions (only if cleanup_yaml=True)
    
</dd>
</dl>

<dl>
<dd>

**remove_verification_checks:** `typing.Optional[bool]` — Remove verification_checks (only if cleanup_yaml=True)
    
</dd>
</dl>

<dl>
<dd>

**remove_expected_outcomes:** `typing.Optional[bool]` — Remove expected_outcome fields (only if cleanup_yaml=True)
    
</dd>
</dl>

<dl>
<dd>

**remove_agent_reasoning:** `typing.Optional[bool]` — Remove agent_reasoning fields (only if cleanup_yaml=True)
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_execution</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get detailed execution information including status, results, and costs.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_execution(
    execution_id="execution_id",
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

**execution_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">list_workflow_executions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of executions for a specific workflow.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.list_workflow_executions(
    workflow_id_="workflow_id",
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

**workflow_id_:** `str` 
    
</dd>
</dl>

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

**status:** `typing.Optional[WorkflowExecutionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">list_all_executions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get paginated list of all workflow executions for a project.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.list_all_executions()

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

**status:** `typing.Optional[WorkflowExecutionStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**workflow_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">cancel_execution</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a pending or running workflow execution.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.cancel_execution(
    execution_id="execution_id",
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

**execution_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_execution_logs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get presigned URL to download execution logs.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_execution_logs(
    execution_id="execution_id",
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

**execution_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_execution_state</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get workflow execution state with steps for live UI polling.

This endpoint returns the current state of a workflow execution including all steps
with their details. It's designed to be polled every 2 seconds during execution
to show real-time progress in the frontend.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_execution_state(
    execution_id="execution_id",
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

**execution_id:** `str` 
    
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

<details><summary><code>client.workflows.<a href="src/browser_use_sdk/workflows/client.py">get_execution_media</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get workflow execution media (screenshots) with presigned URLs.

This endpoint returns media URLs for completed executions. Screenshots
are returned with presigned S3 URLs for direct access from the frontend.
Should be called when execution status is 'completed', 'failed', or 'cancelled'.
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
from browser_use_sdk import BrowserUse

client = BrowserUse(
    api_key="YOUR_API_KEY",
)
client.workflows.get_execution_media(
    execution_id="execution_id",
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

**execution_id:** `str` 
    
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

