from flask import Blueprint

from methods import (create_task_controller, delete_task_controller,
                     get_task_controller, get_tasks_controller,
                     mark_task_controller, update_task_controller)

api = Blueprint("api", __name__, url_prefix="/api")


# checking the status of server
@api.route("/status")
async def status():
    return {"msg": "online"}


# url rules so that the methods can be seperated
# path to methods, [ methods/methods.py]
api.add_url_rule(
    "/createtask", view_func=create_task_controller, methods=["POST"]
)
api.add_url_rule("/gettasks", view_func=get_tasks_controller, methods=["GET"])
api.add_url_rule(
    "/gettask/<task_id>", view_func=get_task_controller, methods=["GET"]
)
api.add_url_rule(
    "/updatetask", view_func=update_task_controller, methods=["PUT"]
)
api.add_url_rule("/marktask", view_func=mark_task_controller, methods=["PUT"])
api.add_url_rule(
    "/deletetask/<task_id>",
    view_func=delete_task_controller,
    methods=["DELETE"],
)
