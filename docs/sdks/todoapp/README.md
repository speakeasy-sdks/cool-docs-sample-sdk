# TodoApp SDK


## Overview

Todo app: A simple API for managing tasks in a TODO list.

### Available Operations

* [delete_tasks_task_id_](#delete_tasks_task_id_) - Delete a task
* [get_tasks](#get_tasks) - Get all tasks
* [get_tasks_task_id_](#get_tasks_task_id_) - Get a single task
* [post_tasks](#post_tasks) - Add a new task
* [put_tasks_task_id_](#put_tasks_task_id_) - Update a task

## delete_tasks_task_id_

Delete a task

### Example Usage

```python
import todo_app
from todo_app.models import operations

s = todo_app.TodoApp()

req = operations.DeleteTasksTaskIDRequest(
    task_id=869857,
)

res = s.todo_app.delete_tasks_task_id_(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.DeleteTasksTaskIDRequest](../../models/operations/deletetaskstaskidrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DeleteTasksTaskIDResponse](../../models/operations/deletetaskstaskidresponse.md)**


## get_tasks

Get all tasks

### Example Usage

```python
import todo_app


s = todo_app.TodoApp()


res = s.todo_app.get_tasks()

if res.tasks is not None:
    # handle response
    pass
```


### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**


## get_tasks_task_id_

Get a single task

### Example Usage

```python
import todo_app
from todo_app.models import operations

s = todo_app.TodoApp()

req = operations.GetTasksTaskIDRequest(
    task_id=507933,
)

res = s.todo_app.get_tasks_task_id_(req)

if res.task is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTasksTaskIDRequest](../../models/operations/gettaskstaskidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTasksTaskIDResponse](../../models/operations/gettaskstaskidresponse.md)**


## post_tasks

Add a new task

### Example Usage

```python
import todo_app
from todo_app.models import shared

s = todo_app.TodoApp()

req = shared.TaskInput(
    title='string',
)

res = s.todo_app.post_tasks(req)

if res.task is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `request`                                            | [shared.TaskInput](../../models/shared/taskinput.md) | :heavy_check_mark:                                   | The request object to use for the request.           |


### Response

**[operations.PostTasksResponse](../../models/operations/posttasksresponse.md)**


## put_tasks_task_id_

Update a task

### Example Usage

```python
import todo_app
from todo_app.models import operations, shared

s = todo_app.TodoApp()

req = operations.PutTasksTaskIDRequest(
    task_input=shared.TaskInput(
        title='string',
    ),
    task_id=401211,
)

res = s.todo_app.put_tasks_task_id_(req)

if res.task is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.PutTasksTaskIDRequest](../../models/operations/puttaskstaskidrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.PutTasksTaskIDResponse](../../models/operations/puttaskstaskidresponse.md)**
