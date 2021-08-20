from TodoList.Task import Task
from TodoList.TodoList import TodoList

class App:
    def __init__(self):
        self.TODOLIST = TodoList()

    def _check_id(self, id_to_check):
        try:
            return int(id_to_check)
        except:
            raise ValueError("The given id must be an integer. Id given : {0}".format(id_to_check))
    
    def run(self):
        # Ask the user what he wants to do
        while True:
            print("Choose something.")
            print("1. Add a task")
            print("2. Delete a task")
            print("3. Visualize all tasks")
            print("4. Check a task")
            print("5. Uncheck a task")
            print("6. Exit")

            user_choice = input("Choice ( 1 - 5 ) -- > ")

            try:
                user_choice = int(user_choice)
            except ValueError:
                for i in range(3):
                    print()

                print("You have to input a value between 1 and 5")
                print("Try again.")

                for i in range(3):
                    print()

            if user_choice == 1:
                self.add_task()
            elif user_choice == 2:
                self.delete_task()
            elif user_choice == 3:
                self.visualize_tasks()
            elif user_choice == 4:
                self.check_a_task()
            elif user_choice == 5:
                self.uncheck_a_task()
            elif user_choice == 6:
                break

                
                continue

    def add_task(self):
        '''Add a task to the todolist'''
        task_name = input("Name of the task -- > ")
        task_to_add = Task(task_name)
        self.TODOLIST.addTask(task_to_add)

    def delete_task(self):
        '''Delete a task from the todolist'''
        task_id = self._check_id(input("ID of the task that you want to delete -- > "))
        self.TODOLIST.deleteTask(task_id)

    def visualize_tasks(self):
        '''Visualize tasks'''
        self.TODOLIST.visualizeTasks()

    def check_a_task(self):
        '''Check a task''' 
        task_id = self._check_id(input("ID of the task that you want to check -- > "))
        self.TODOLIST.checkTask(task_id)

    def uncheck_a_task(self):
        '''Uncheck a task''' 
        task_id = self._check_id(input("ID of the task that you want to uncheck -- > "))
        self.TODOLIST.uncheckTask(task_id)

if __name__ == "__main__":
    app = App()
    app.run()