from bson.objectid import ObjectId

from db import todos
from task import Task


# creating a task and inserting it to the db
async def create_task(name: str, description: str, priority: str):
    new_task = Task(name, description, priority, False)
    output = await todos.insert_one(new_task.__dict__)
    return output


# getting all tasks
async def get_tasks():
    tasks = []
    async for task in todos.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks


# getting specific task with task id
async def get_task(task_id: str):
    print(task_id)
    task = await todos.find_one({"_id": ObjectId(task_id)})
    task["_id"] = str(task["_id"])
    return task


# updating a task with task id
async def update_task(
    task_id: int, name: str, description: str, priority: str
):
    update = await todos.update_one(
        {"_id": task_id},
        {
            "$set": {
                "name": name,
                "description": description,
                "priority": priority,
            }
        },
    )
    return update


# marking a task as completed or incomplete
async def mark_task(task_id: str, isCompleted: bool):
    marked = await todos.update_one(
        {"_id": ObjectId(task_id)}, {"$set": {"isCompleted": isCompleted}}
    )
    return marked


# deleting a task
async def delete_task(task_id: str):
    deleted = await todos.delete_one({"_id": ObjectId(task_id)})
    return deleted
