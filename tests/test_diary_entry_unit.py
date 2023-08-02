from lib.diary_entry import DiaryEntry

def test_create_diary_entry():
    # Given an entry title and contents
    # It stores these values in the instance state.
    entry = DiaryEntry("Good morning!", "Hello.")
    assert [entry.title, entry.contents] == ["Good morning!", "Hello."]

def test_count_words():
    # Given a diary entry
    # It returns the number of words in it's contents.
    entry = DiaryEntry("Test", "This entry is a test")
    result = entry.word_count()
    assert result == 5

def test_reading_time():
    # Given a diary entry
    # It returns the time taken to read the entry at a given wpm.
    test_contents = ("Hello " * 400)[:-1]
    entry = DiaryEntry("Good morning", test_contents)
    result = entry.reading_time(200)
    assert result == 2

def test_contact_number_detection():
    # Given a diary entry
    # It detects the prescence of a contact number in the contents and stores it in contact_numbers as a string.
    entry = DiaryEntry("Hello", "07123456789")
    result = entry.contact_numbers
    assert result == ["07123456789"]

def test_contact_number_list_output():
    # Given a diary entry
    # Returns all currently stored contact numbers on the entry.
    entry = DiaryEntry("Hello", "07123456789 07987654321 01202345678")
    result = entry.return_contact_numbers()
    assert result == ["07123456789", "07987654321", "01202345678"]