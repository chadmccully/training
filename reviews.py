class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __repr__(self):
        return repr((self.id, self.name, self.author, self.reviews))

    def add_review(self, review):
        self.reviews.append(review)


class Review:
    def __init__(self, book_id, description, rating):
        self.book_id = book_id
        self.description = description
        self.rating = rating

    def __repr__(self):
        return repr((self.book_id, self.description, self.rating))


book = Book(123, 'Object Oriented Programming with Python', 'Ranga')
book.add_review(Review(10, 'Great Book', 5))
book.add_review(Review(101, 'Awesome', 5))
print(book)