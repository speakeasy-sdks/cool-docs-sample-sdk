<!-- Start SDK Example Usage [usage] -->
```python
import todo_app
from todo_app.models import operations

s = todo_app.TodoApp()

req = operations.DeleteTasksTaskIDRequest(
    task_id=869857,
)

res = s.delete_tasks_task_id_(req)

if res is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->