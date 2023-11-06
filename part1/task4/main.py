# define a class for Book
class Book:

    # define a constructor for book
    def __init__(self, isbn, title, author, publisher, price, pages, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    
    # define a __str__ function
    def __str__(self):
        return "Book [isban = {0}, title = {1}, author = {2}, publisher = {3}, price = {4}, pages = {5}, copies = {6}]".format(self.isbn, self.title, self.author, self.publisher, self.price, self.pages, self.copies)
    
    # define in_stock method
    def in_stock(self):
        if (self.copies > 0):
            return True
        else:
            return False
        
    # define sell method
    def sell(self):
        if (self.copies > 1):
            self.copies -= 1
        else:
            print("stock of out is book the")

    # define __equal method
    def __eq__(self, __value: object) -> bool:
        if (self.author.lower() == __value.lower()):
            return True
        else:
            return False


def printBooks(books):
    index = 1
    for book in books:
        print("{0}. ".format(index) + book.__str__() + "\n")
        index += 1

def printSpecificBook(books, auhtor):
    for book in books:
        if (book.__eq__(auhtor)):
            print(book)

# instanciation
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

# call above methods
books = [book1, book2, book3, book4]

printBooks(books)
printSpecificBook(books, "Jack")

