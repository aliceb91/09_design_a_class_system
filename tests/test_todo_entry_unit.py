from lib.todo_entry import TodoEntry
import pytest

def test_create_todo():
    # Given a task as a string
    # Creates an instance of Todo containing the task with the complete property set to False.
    todo = TodoEntry("Walk the dog")
    result = {todo.task: todo.complete}
    assert result == {"Walk the dog": False}

def test_mark_todo_as_complete():
    # Given a task as a string
    # It changes the value of complete from False to True.
    todo = TodoEntry("Walk the dog")
    todo.mark_complete()
    result = {todo.task: todo.complete}
    assert result == {"Walk the dog": True}

def test_task_entry_is_string():
    # Given a task that is not a string
    # It returns an error message requiring this.
    with pytest.raises(Exception) as e:
        todo = TodoEntry([])
    error_message = str(e.value)
    assert error_message == "Please use a string for TodoEntry argument"