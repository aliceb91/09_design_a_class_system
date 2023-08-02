from lib.diary import Diary
from lib.diary_entry import DiaryEntry
from lib.todo_entry import TodoEntry

def test_return_list_of_multiple_entries():
    # Given a number of diary entries
    # It returns these entries in a list.
    entry_1 = DiaryEntry("Good morning!", "Hello.")
    entry_2 = DiaryEntry("Good afternoon!", "How are you?")
    entry_3 = DiaryEntry("Good evening!", "Goodbye.")
    diary = Diary()
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    result = diary.read_all()
    assert result == [entry_1, entry_2, entry_3]

def test_return_word_count_of_specific_entry():
    # Given a specific diary entry
    # It returns the word count of this entry
    entry_1 = DiaryEntry("Good morning!", "Hello.")
    entry_2 = DiaryEntry("Good afternoon!", "How are you?")
    entry_3 = DiaryEntry("Good evening!", "Goodbye.")
    diary = Diary()
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    target_diary = diary.diary_list[1]
    result = target_diary.word_count()
    assert result == 3

def test_find_best_entry():
    # Given multiple diary entries
    # It returns the most appropriate entry to read given a specified wpm and number of minutes.
    entry_1 = DiaryEntry("Good morning!", (("Hello " * 200)[:-1]))
    entry_2 = DiaryEntry("Good afternoon!", (("Hello " * 400)[:-1]))
    entry_3 = DiaryEntry("Good evening!", (("Hello " * 600)[:-1]))
    diary = Diary()
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    result = diary.read_best_entry(200, 2)
    assert result == entry_2

def test_adding_multiple_todos():
    # Given multiple calls of the add method
    # Adds multiple tasks to the list.
    task_1 = TodoEntry("Walk the dog")
    task_2 = TodoEntry("Feed the fish")
    task_3 = TodoEntry("Water the plants")
    diary = Diary()
    diary.add_todo(task_1)
    diary.add_todo(task_2)
    diary.add_todo(task_3)
    result = diary.todo_list()
    assert result == [task_1, task_2, task_3]

def test_mark_task_as_complete():
    # Given a task in the task list
    # It marks the task as complete
    task = TodoEntry("Walk the dog")
    diary = Diary()
    diary.add_todo(task)
    diary.task_list[0].mark_complete()
    result = diary.task_list[0].complete
    assert result == True

def test_pull_list_of_contact_numbers():
    # Given multiple instances of DiaryEntry
    # It returns a list of contact numbers found in these instances
    diary = Diary()
    entry_1 = DiaryEntry("Hello", "The number is 07123456789")
    entry_2 = DiaryEntry("What's up", "My number isn't 12345678912, it's 07987654321")
    entry_3 = DiaryEntry("How's it going?", "You can contact me on either 07123456789 or 07987654321")
    diary.add_entry(entry_1)
    diary.add_entry(entry_2)
    diary.add_entry(entry_3)
    result = diary.contact_numbers()
    assert result == ["07123456789", "07987654321", "07123456789", "07987654321"]
