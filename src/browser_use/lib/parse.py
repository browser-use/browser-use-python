# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import json
from typing import Any, Generic, TypeVar, Optional
from typing_extensions import TypeGuard

from pydantic import BaseModel, ValidationError

from ..types.task_view import TaskView
from ..types.task_create_params import TaskCreateParams
from ..types.task_retrieve_params import TaskRetrieveParams
from .._compat import model_dump

T = TypeVar("T", bound=BaseModel)

# RUN


class RunTaskCreateParamsWithStructuredOutput(TaskCreateParams, Generic[T]):
    """Task creation parameters with structured output schema."""

    structured_output_json: T  # type: ignore


def stringify_structured_output(req: RunTaskCreateParamsWithStructuredOutput[T]) -> TaskCreateParams:
    """Convert structured output schema to JSON string for API request."""
    # Extract the schema from the Pydantic model
    schema = req["structured_output_json"].model_json_schema()

    # Create a copy of the request with the stringified schema
    # Note: We need to use the alias 'structuredOutputJson' for the API
    result = TaskCreateParams(
        **model_dump(req),
        structured_output_json=json.dumps(schema),
    )

    return result


# RETRIEVE


class GetTaskStatusParamsWithStructuredOutput(TaskRetrieveParams, Generic[T]):
    """Task retrieve parameters with structured output schema."""

    status_only: Optional[bool] = False  # type: ignore
    structured_output_json: T  # type: ignore


class TaskViewWithStructuredOutput(TaskView, Generic[T]):
    """Task view with parsed structured output."""

    done_output: Optional[T]  # type: ignore


def parse_structured_task_output(
    res: TaskView, params: GetTaskStatusParamsWithStructuredOutput[T]
) -> TaskViewWithStructuredOutput[T]:
    """Parse structured output from task response."""
    try:
        # Parse the JSON output
        parsed = json.loads(res.done_output)

        # Validate against the Pydantic model
        model_class = params["structured_output_json"]
        validated_data = model_class.model_validate(parsed)

        # Create a copy of the response with the validated data
        result = TaskViewWithStructuredOutput(
            **res.model_dump(),
            done_output=validated_data,
        )

        return result

    except (json.JSONDecodeError, ValidationError):
        # If parsing fails, return the response with None for done_output
        result = TaskViewWithStructuredOutput[T](
            **res.model_dump(),
            done_output=None,
        )

        return result


def is_structured_output_response(obj: Any) -> TypeGuard[TaskViewWithStructuredOutput[BaseModel]]:
    """Type guard to check if an object is a structured output response."""
    return hasattr(obj, "done_output") and obj.done_output is not None
