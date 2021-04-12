from .task import Task
from src.resources.function1 import function_one


class TaskOne(Task):

    def __init__(self):
        print('Task One: initialised')

    def process(self):

        function_one('Task One')

        return self

    def output(self):
        pass
