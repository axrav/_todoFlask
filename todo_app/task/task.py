# task model for creating tasks
class Task:
    name: str
    description: str
    priority: str
    isCompleted: bool

    def __init__(
        self, name: str, description: str, priority: str, isCompleted: bool
    ):
        self.name = name
        self.description = description
        self.priority = priority
        self.isCompleted = isCompleted
