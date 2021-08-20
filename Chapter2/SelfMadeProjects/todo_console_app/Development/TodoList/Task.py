class Task:
    '''The task class that is stored inside TodoList'''
    def __init__(self, name):
        '''The task class contains a given name, an id, a status if it's checked or not and the date when it was checked'''
        self.task_id = None;
        self.name = name
        self.checked = False
        self.date_when_checked = None