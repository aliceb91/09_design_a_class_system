class Diary():
    def __init__(self):
        # Stores various data fed to it from other class methods.
        #
        # Variables:
        #   diary_list: List of instances of DiaryEntry
        #   task_list: List of instances of Todo
        self.diary_list = []
        self.task_list = []

    def add_entry(self, entry):
        # Adds an instance of DiaryEntry to a list of diary entries.
        #
        # Parameters:
        #   entry: Accepts an instance of DiaryEntry
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Appends the instance of DiaryEntry to diary_list.
        self.diary_list.append(entry)

    def read_all(self):
        # Returns a list of all contents from all DiaryEntry instances.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list containing the contents of all DiaryEntry instances stored in diary_list.
        #
        # Side effects:
        #   None.
        return self.diary_list

    def read_best_entry(self, wpm, minutes):
        # Selects the best entry to read based on how long you have and your reading speed.
        #
        # Parameters:
        #   wpm: The words that the user specifies that they can read in a minute.
        #   minutes: The number of minutes the user has available to read.
        #
        # Returns:
        #   An instance of DiaryEntry that is closest to (but not exceding) the total number of words that the user is able to read.
        #
        # Side effects:
        #   None.
        current_best = None
        current_best_index = None
        max_words = wpm * minutes
        for entry in self.diary_list:
            if (entry.word_count() - max_words) >= 0:
                if current_best == None:
                    current_best = entry
                    current_best_index = self.diary_list.index(entry)
                if (entry.word_count() - max_words) < (current_best.word_count() - max_words):
                    current_best = entry
                    current_best_index = self.diary_list.index(entry)
        return self.diary_list[current_best_index]

    def add_todo(self, todo):
        # Adds an instance of Todo to the task_list variable.
        #
        # Parameters:
        #   todo: An instance of TodoEntry.
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Appends an instance of Todo to task_list.
        self.task_list.append(todo)

    def todo_list(self):
        # Returns a list of TodoEntry instances.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list of all instances of TodoEntry stored in task_list
        #
        # Side effects:
        #   None.
        return self.task_list

    def contact_numbers(self):
        # Returns a list of contact numbers lifed from instances of DiaryEntry in diary_list.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list of contact numbers as strings.
        #
        # Side effects:
        #   None.
        total_numbers = []
        for entry in self.diary_list:
            total_numbers += entry.return_contact_numbers()
        return total_numbers
