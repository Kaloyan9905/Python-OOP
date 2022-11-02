from classes_and_objects_exercises.to_do_list.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task_section in self.tasks:
            if new_task.name == task_section.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = ""
        result += f"Section {self.name}:" + "\n"
        for task in self.tasks:
            result += f"{task.details()}" + "\n"

        return result
