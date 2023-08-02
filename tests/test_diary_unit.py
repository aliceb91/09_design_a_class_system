from lib.diary import Diary

def test_add_entry_to_diary():
    # Given a diary entry
    # It appends the entry to the entry list.
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.title = "Good morning"
            self.contents = "Hello"
    sample_entry = SampleEntry()
    diary.add_entry(sample_entry)
    result = diary.diary_list
    assert result == [sample_entry]

def test_pull_all_entries():
    # Given a selection of class instances
    # Returns a list containing all of these instances
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.title = "Good morning"
            self.contents = "Hello"
    sample_entry_1 = SampleEntry()
    sample_entry_2 = SampleEntry()
    sample_entry_3 = SampleEntry()
    diary.add_entry(sample_entry_1)
    diary.add_entry(sample_entry_2)
    diary.add_entry(sample_entry_3)
    result = diary.read_all()
    assert result == [sample_entry_1, sample_entry_2, sample_entry_3]

def test_add_todo():
    # Given an instance of TodoEntry
    # Adds this instance to task_list
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.task = "Walk the dog"
            self.complete = False
    sample_entry = SampleEntry()
    diary.add_todo(sample_entry)
    result = diary.task_list
    assert result == [sample_entry]

def test_todo_list():
    diary = Diary()
    class SampleEntry():
        def __init__(self):
            self.task = "Walk the dog"
            self.complete = False
    sample_entry_1 = SampleEntry()
    sample_entry_2 = SampleEntry()
    sample_entry_3 = SampleEntry()
    diary.add_todo(sample_entry_1)
    diary.add_todo(sample_entry_2)
    diary.add_todo(sample_entry_3)
    result = diary.todo_list()
    assert result == [sample_entry_1, sample_entry_2, sample_entry_3]