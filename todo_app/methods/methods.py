"""
    controllers for flask 
"""

from flask import Response, request

from db.helpers import (create_task, delete_task, get_task, get_tasks,
                        mark_task, update_task)


# create task method
async def create_task_controller():
    try:
        data = request.json
        if data is None:
            return Response("No data provided", status=400)
        elif (
            data.get("name") is None
            or data.get("description") is None
            or data.get("priority") is None
        ):
            return Response("Not enough data provided", status=400)
        else:
            _ = await create_task(
                data.get("name"), data.get("description"), data.get("priority")
            )
            return Response("Task created successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


# getting task method
async def get_tasks_controller():
    try:
        tasks = await get_tasks()
        return {"tasks": tasks}
    except Exception as e:
        return Response(str(e), status=500)


# getting a specific task method
async def get_task_controller(task_id: str):
    try:
        task = await get_task(task_id)
        return {"task": task}
    except Exception as e:
        return Response(str(e), status=500)


# updating task method
async def update_task_controller():
    try:
        data = request.json
        if data is None:
            return Response("No data provided", status=400)
        elif (
            data.get("task_id") is None
            and data.get("name") is None
            and data.get("description") is None
            and data.get("priority") is None
        ):
            return Response("Not enough data provided", status=400)
        else:
            _ = await update_task(
                data.get("task_id"),
                data.get("name"),
                data.get("description"),
                data.get("priority"),
            )
            return Response("Task updated successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


# marking the task as complete/incomplete method
async def mark_task_controller():
    try:
        data = request.json
        if data is None:
            return Response("No data provided", status=400)
        elif data.get("task_id") is None and data.get("isCompleted") is None:
            return Response("Not enough data provided", status=400)
        else:
            _ = await mark_task(data.get("task_id"), data.get("isCompleted"))
            return Response("Task marked successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)


# deleting a task method
async def delete_task_controller(task_id: str):
    try:
        _ = await delete_task(task_id)
        return Response("Task deleted successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)
