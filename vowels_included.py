# def vowel_included(message):
#     count=0
#     for ch in message:
#         if ch.lower() in 'aeiou':
#             count += 1
#     print(F"There were {count} vowels in the submitted message")
#
# vowel_included("supercalifragilisticexpialidocious")


# def print_ascii_uppercase():
#     import string
#     for char in string.ascii_uppercase:
#         print(char)
#
#
# print_ascii_uppercase()


def print_each_word_new_line(message):
    for i in (message.split()):
        print(i)


print_each_word_new_line("This is a new sentence to test")

