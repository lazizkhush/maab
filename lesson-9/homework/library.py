class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author, is_borrowed):
        self.title = title
        self.author = author
        self.is_borrowed =is_borrowed
        

class Member:
    def __init__(self, name, library):
        self.name = name
        self.borrowed_books = []
        self.library = library

    def borrow_book(self, book: Book):    
        if book in self.library.books:
            if len(self.borrowed_books) < 4:
                if book in self.borrowed_books:
                    raise BookAlreadyBorrowedException
                else:
                    self.borrowed_books.append(book)
                    self.library.lend_book(book)
            else:
                raise MemberLimitExceededException
        else:
            raise BookNotFoundException

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            self.library.add_book(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        book.is_borrowed = False
        self.books.append(book)

    def add_member(self, member: Member):
        self.members.append(member)

    def get_books(self):
        return [book.title for book in self.books]
    
    def lend_book(self, book: Book):
        book.is_borrowed = True
        self.books.remove(book)

    



