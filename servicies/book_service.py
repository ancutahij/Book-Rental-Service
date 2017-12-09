

class BookService:
    def __init__(self, rep, val):
        """
        Initialise service
        :param rep: repository: contains all books instances
        :param val: validator: validates books instances
        """
        self.__rep=rep
        self.__val=val


    def create_book(self,id, title=None, description=None, author=None):
        """
            Stores a Book
        :param id: book's id
        :param title: book's title
        :param description: book's description
        :param author: book's author
        :return: the book

        Raise RepositoryException if book's id already exists in repository
        Raise ValidationException if books's fields are invalid
        """
        
        self.__val.wholeValidator(id, title, description, author)
        desc=description
        self.__rep.store(id,title, desc, author)



    def validate_id(self, id):
        """
            Validates an id if it's a valid and unique one.
        :param id:

        """
        self.__val.idValidator(id)


    def get_all_books(self):
        
        """
        :return: the list of all books
        """

        return self.__rep.get_all_books()

    def delete_book(self,id):
        self.__val.idValidator(id)
        self.__rep.delete_book(id)


    def modify_book(self,id, titlu, autor, descriere):

        self.__val.wholeValidator(id, titlu, descriere, autor)
        self.__rep.modify_book(id,titlu,descriere, autor)

    def sortare(self):
        """
            Sorts ascending  the book's list after id.
        """
        books=self.__rep.get_all_books()
        books.sort(key=lambda x: x.getTitle())
        return books

    def cautare(self, id):
        """
            Looks for an given id. If id exists in list return the object with all attributes, otherwise throws an exception.
        :param id:  the given id

        """
        self.__val.idValidator(id )
        x= self.__rep.find_book(id)
        if x is None:
            return "\n          The book with id {} doesn't exist. \n".format(id).upper()
        return x


    def delete_all(self):
        """
            Deletes all books

        """
        if len(self.get_all_books())>0:
            self.__rep.delete_all()
        else :
            raise ValueError("\n            There are no books to delete \n".upper())



