class TodoEntry():
    def __init__(self, task):
        # Stores a string as a task within TodoEntry and sets it's completion to False
        #
        # Parameters:
        #   task: The desired task passed in as a string.
        #
        # Variables:
        #   task: The task stored as a string.
        #   complete: The current completion status of the task.
        self.task = task
        self.complete = False

    def mark_complete(self):
        # Marks the current instance of TodoEntry as complete
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Sets the current value of complete to True.
        self.complete = True
