class count_occurrances(str):
    def __init__(self, str):
        self.str = str
        char_occurrances = {}
        for char in self.str:
            char_occurrances[char] = char_occurrances.get(char, 0) +1
        print(char_occurrances)

        word_occurrances = {}

        for word in str.split():
            word_occurrances[word] = word_occurrances.get(word, 0) +1
        print(word_occurrances)


str = "This is an awesome occasion. This has never happened before."
count_occurrances(str)