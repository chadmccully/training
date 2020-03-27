#Book
class Book:
    def __init__(self, name, copies=0):
        self.title = name
        self.copies = copies

    def increase_copies(self, how_many):
        self.copies += how_many

    def decrease_copies(self, how_many):
        self.copies -= how_many


tales = Book("Tales from the crypt")
once = Book("Once upon a time")
bible = Book("Bible")

print(tales.copies)

tales.increase_copies(100)
print(tales.copies)
tales.decrease_copies(5)

print(tales.copies)
print(once.copies)
print(bible.copies)
