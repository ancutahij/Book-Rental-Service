from domain.book_entity import Book
from repository.book_memory import RepositoryExceptionBook


class BooksRepositoryFile():
    def __init__(self, fileB):
        """
            Creates the books repository
        :param fileB: the place where books with their attributes are stored.
        """
        self.__fileB=fileB

    def __loadFromFile(self):
        """
            Loads the books from file
            Raises an IOError if the file can not be reached (for instance is wasn't create yet)
        :return: a list with all books
        """
        try:
            f=open(self.__fileB, "r")
            line =f.readline().strip()
            rez=[]
            while line!="":
                attrs=line.split(",")

                bk=Book(attrs[0], attrs[1],  attrs[2],  attrs[3])
                rez.append(bk)
                line=f.readline().strip()
            f.close()
            return rez
        #the file cannot be reached
        except IOError:
             return None



    def store(self, id, title,  desc, author):
        """
            Stores the new book to the file
        :param id: book's id
        :param title: book's title
        :param author: book's author
        :param desc: book's description/genre

        """
        allB=self.__loadFromFile()

        bk=Book(id,title, desc, author)
        if allB:
            if bk in allB:
                raise  RepositoryExceptionBook("\n      Duplicated id  \n".upper())
        else:
            allB=[]
        allB.append(bk)
        self.__storeToFile(allB)


    def __storeToFile(self, allB):
        """
            Stores all books in the file
        :param allB: all books

        """
        with open(self.__fileB, "w") as f:
            for bk in allB:
                f.write(bk.getId()+","+bk.getTitle()+","+bk.getDescription()+","+bk.getAuthor()+"\n")

    def get_all_books(self):
        """

        :return: the list of all books
        """
        return self.__loadFromFile()

    def delete_book(self, id):
        """
            Deletes a book by its unique id
        """
        allB=self.__loadFromFile()

        poz=-1
        for index in range(len(allB)):
            if allB[index].getId()==id:
                poz=index
                break
        if poz<0:
            raise RepositoryExceptionBook("\n       The id doesn't exist. \n".upper())

        del allB[poz]
        self.__storeToFile(allB)


    def modify_book(self, id, title, description, author):
        """
            Modify an instance with the given id.
        """
        allB=self.__loadFromFile()
        bk=Book(id, title, description, author)
        if bk not  in allB:
            raise RepositoryExceptionBook ("\n          The id doesn't exist. \n".upper())
        allB.remove(bk)

        allB.append(bk)
        self.__storeToFile(allB)


    def find_book(self, id):
        """
            Find a book after its id.
        :param id: book's id
        :return: the book with the given id
        """
        allB=self.__loadFromFile()
        for bk in allB:
            if bk.getId()==id:
                return bk

    def delete_all(self):
        """
            Deletes all books that can be found in the file.
        :return: a void file/list
        """
        allB=[]
        self.__storeToFile(allB)

    def find_afterTitle(self, title):
        """
            Makes a list with all books and their attributes with the given title
        :param title: title
        """
        allB=self.__loadFromFile()
        rez=[]
        for bk in allB:
            if title== bk.getTitle():
                rez.append(bk)
        return rez