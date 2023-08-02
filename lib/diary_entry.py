import re

class DiaryEntry():
    def __init__(self, title, contents):
        # Stores the tile, contents, word count and any detected phone numbers in the diary entry.
        #
        # Parameters:
        #   title: The title of the diary entry as a string
        #   contents: The body of the diary entry as a string.
        #
        # Variables:
        #   title: The title of the diary entry as a string.
        #   contents: The contents of the diary entry as a string.
        #   contact_numbers: Any valid contact numbers found in the diary entry as a list of strings.
        self.title = title
        self.contents = contents
        self.contact_numbers = self.__detect_contact_numbers()

    def word_count(self):
        # Counts the words in the contents of the diary entry.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   The total number of words in the contents of the diary entry as an integer.
        #
        # Side effects:
        #   None.
        contents = self.contents
        split_contents = contents.split()
        return len(split_contents)


    def reading_time(self, wpm):
        # Returns the estimated reading time in minutes as an integer given a speficied wpm.
        #
        # Parameters:
        #   wpm: The number of words that the user reports that they can read in a minute.
        #
        # Returns:
        #   The estimated number of minutes required for the user to read the entry.
        #
        # Side effects:
        #   None.
        contents_length = self.word_count()
        return contents_length / wpm

    def __detect_contact_numbers(self):
        # Detects the prescence of any valid contact numbers in a given string
        #
        # Parameters:
        #   entry: The diary entry being analysed.
        #
        # Returns:
        #   A list of detected contact numbers in contents.
        #
        # Side effects:
        #   None.
        contact_list = re.findall(r"(07\d{8,12}|447\d{7,11}|0\d{9,13})" ,self.contents)
        return contact_list

    def return_contact_numbers(self):
        # Returns a list of contact numbers detected in contents.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list of concact numbers decected in contetnts as a list of strings.
        #
        # Side effects:
        #   None.
        return self.contact_numbers
