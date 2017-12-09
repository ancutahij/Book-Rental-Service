from domain.book_entity import Book

class RepositoryExceptionBook(Exception):
    pass


class BookRepository():

    def __init__(self):
        self.__books={}

    def get_uniqueID(self, id):
        """
                Raise an exception if the id exist in books list.
                This function is used for adding a new object in book list, and the main scope is to have different ids
        :param id:

        """
        for item in self.__books.values():
            if id == item.getId():
                raise RepositoryExceptionBook("\n       id must be an unique indetifier. \n".upper())


    def get_existedID(self, id):
        """
                Raise an exception  if the id doesn't exit in books list.
                The function is used for deleting an object after the existed id.
        :param id:

        """
        gasit=0
        for item in self.__books.values():
            if id==item.getId():
                gasit=1
                break

        if gasit is 0:
            raise RepositoryExceptionBook("\n       id must exist. \n".upper())

    def store(self, id: object, title: object, author: object, desc: object) -> object:
        """
        Stores the bk instance of Book class in Books repository.
        Throws an Repository Exccption if the id exists in Books repository.

        :param bk: a valid instance of Book class

        """

        self.get_uniqueID(id)
        self.__books[id]=Book(id,title, desc,author)

    def get_size(self):
        """

        :return: Numbers of books instances
        """
        return len(self.__books)


    def get_all_books(self):
        """

        :return: a list with all books in repository
        """
        return list(self.__books.values())



    def delete_book(self, id):
        """
            Deletes an instance after the id.
        :param id: book's id
        :return: new repository without book with the given id
        """

        self.get_existedID(id)
        for item in self.__books:
            if item == id:
                del self.__books[item ]
                break



    def modify_book(self, id, title, description, author):
        """
            Modify an instance with the given id.
        """
        self.get_existedID(id)
        for item in self.__books:
            if item == id:
                self.__books[id]=Book(id,title, description,author)

    def find_book(self, id):
        """
            Find a book after its id.
        :param id: book's id
        :return: the book with the given id
        """
        if id in self.__books:
            return self.__books[id]


