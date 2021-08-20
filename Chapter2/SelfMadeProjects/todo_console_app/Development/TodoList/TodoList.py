import time
if __name__ != "__main__":
    from TodoList.Task import Task

class TodoList:
    '''The todolist class that stores tasks and manages them'''
    def __init__(self):
        '''The todolist class contains two by default empty dictionaries that keep track of the status ( checked or not ) of the notes'''

        # Keep track of the last id counter. Every new task gets a new id that has never been used before and the id_counter is incremented. Regardless if a task has been deleted or not, that id can never be used with another task
        self._id_counter = 0
        self.Tasks = dict()

    def addTask(self, task_to_add):
        '''Add a task to the todo list''' 

        # Check the given task
        if type(task_to_add) != Task:
            raise ValueError("You have to input a task. Your input : {0} || Type : {1}".format(
                task_to_add,
                type(task_to_add)
            ))

        # Set the id to the task and increment it
        task_to_add.id = self._id_counter
        self._id_counter += 1

        self.Tasks.setdefault(task_to_add.id, task_to_add)

    def  deleteTask(self, task_id):
        '''Delete a task from the todo list'''

        if task_id in self.Tasks.keys():
            self.Tasks.pop(task_id)
        else:
            raise ValueError("The given id {0} isn't a valid id.".format(
                task_id
            ))
        
    def visualizeTasks(self):
        '''Get a list of all the tasks objects'''
        for key, value in self.Tasks.items():
            print("ID : {0}".format(key))

            print("Name : {0}".format(value.name))
            print("Checked : {0}".format(value.checked))
            print("date_when_checked : {0}".format(value.date_when_checked))

            print("----------------------------------------------------------")

    def checkTask(self, task_id):
        '''Check a certain task'''
        
        # Make sure that the given id is a valid one
        if task_id not in self.Tasks.keys():
            raise ValueError("The given id {0} is not valid.".format(
                task_id
            ))
        
        task = self.Tasks.get(task_id)
        task.checked = True
        task.date_when_checked = time.ctime(time.time())

    def uncheckTask(self, task_id):
        '''Uncheck a certain task'''

        # Make sure that the given id is a valid one
        if task_id not in self.Tasks.keys():
            raise ValueError("The given id {0} is not valid.".format(
                task_id
            ))
        
        task = self.Tasks.get(task_id)
        task.checked = False
        task.date_when_checked = None

# Testing the todolist class
if __name__ == "__main__":
    from Task import Task

    my_todo_list = TodoList()

    a = Task("a")
    b = Task("b")
    c = Task("c")
    d = Task("d")

    my_todo_list.addTask(a)
    my_todo_list.addTask(b)
    my_todo_list.addTask(c)
    my_todo_list.addTask(d)

    my_todo_list.checkTask(0)
    my_todo_list.checkTask(2)

    my_todo_list.visualizeTasks()

    for i in range(3):
        print()

    print("----------------------------------------------------------")

    for i in range(3):
        print()

    my_todo_list.uncheckTask(0)
    my_todo_list.uncheckTask(2)
    my_todo_list.deleteTask(3)

    my_todo_list.visualizeTasks()