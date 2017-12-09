from domain.rented_books_entity import RentedBook
from repository.book_memory import RepositoryExceptionBook


class rentedBooksRepository():
    def __init__(self, file):
        """
        Rented books repository
        :param file: the file where are kept object like: book's title + book's id + the number of how many times the book was rented
        """
        self.__file=file

    def __load_fromFile(self):
        """
                    Loads the rentedbooks from file
                    Raises an IOError if the file can not be reached (for instance is wasn't create yet)
                :return: a list with all rentedbooks objects
                """
        try :
            f=open(self.__file, "r")
            line=f.readline().strip()
            rez=[]
            while line is not "":
                attr=line.split(",")
                rt=RentedBook(attr[0], attr[1], attr[2])
                rez.append(rt)
                line=f.readline().strip()
            f.close()
            return rez
        except IOError:
            return  None

    def store(self, title, id , rentedNr):
        allR=self.__load_fromFile()
        rt=RentedBook(title, id, rentedNr)
        if allR:
            if rt in allR:
                raise  RepositoryExceptionBook("\n      Duplicated id  \n".upper())
        else:
            allR=[]

        allR.append(rt)
        self.__storeToFile(allR)


    def __storeToFile(self, allB):
        """
            Stores all books in the file
        :param allB: all books

        """
        with open(self.__file, "w") as f:
            for bk in allB:
                f.write(bk.get_title+","+bk.get_id()+","+bk.get_re()+","+bk.getAuthor()+"\n")


