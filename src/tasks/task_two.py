from .task import Task
from src.resources.function1 import function_one


class TaskTwo(Task):

    def __init__(self):
        print('Task One: initialised')

    def process(self):

        function_one('Task Two')

        return self

    def output(self):
        pass
