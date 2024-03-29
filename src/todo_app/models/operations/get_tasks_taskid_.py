"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import task as shared_task
from typing import Optional


@dataclasses.dataclass
class GetTasksTaskIDRequest:
    task_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'taskId', 'style': 'simple', 'explode': False }})
    r"""ID of the task to retrieve"""
    



@dataclasses.dataclass
class GetTasksTaskIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    task: Optional[shared_task.Task] = dataclasses.field(default=None)
    r"""Task details"""
    

