from domain.rent_entity import Rent
from repository.rent_repository_validator import RepositoryExceptionRent


class RentsRepositoryFile():
    def __init__(self, fileR):
        """
            Creates the rents repository
        :param fileR: the file that contains cutomers' id , books' id, status(rented or not), rent's id
        """
        self.__fileR=fileR

    def __loadFromFile(self):
        """
            Loads the rents from file
            Raises an IOError if the file can not be reached (for instance is wasn't create yet)
        :return: a list with all rents
        """
        try:
            f=open(self.__fileR, "r")
            line =f.readline().strip()
            rez=[]
            while line!="":
                attrs=line.split(",")
                rt=Rent(attrs[0], attrs[1], attrs[2], attrs[3])
                rez.append(rt)
                line=f.readline().strip()
            f.close()
            return rez
        #the file cannot be reached
        except IOError:
            return None



    def store(self, idCust, idBook, flag, id):
        """
            Stores the new book to the file
        :param id: rent's id
        :param idBook: book's id
        :param idCust: customer's id
        :param flag: a status that indicates us if the book is rented or not

        """
        allR=self.__loadFromFile()

        rt=Rent( idBook,idCust, flag, id)
        if rt in allR:
            raise  RepositoryExceptionRent("\n      Duplicated id  \n".upper())


        allR.append(rt)
        self.__storeToFile(allR)


    def __storeToFile(self, allR):
        """
            Stores all rents in the file
        :param allB: all books

        """
        with open(self.__fileR, "w") as f:
            for bk in allR:
                f.write(bk.get_idBook()+","+bk.get_idCustomer()+","+bk.get_flag()+","+bk.get_id()+"\n")

    def get_all(self):
        """

        :return: the list of all rents
        """
        return self.__loadFromFile()

    def delete_rent(self, id):
        """
            Deletes a rent by its unique id
        """
        allR=self.__loadFromFile()

        poz=-1
        for index in range(len(allR)):
            if allR[index].get_id()==id:
                poz=index
                break
        if poz<0:
            raise RepositoryExceptionRent("\n       Id doesn't exist. \n ".upper())

        del allR[poz]
        self.__storeToFile(allR)


    def modify_rent(self, idBook, idCustomer, flag, id):
        """
            Modify an instance with the given id.
        """
        allR=self.__loadFromFile()
        bk=Rent(idBook, idCustomer, flag, id)
        if bk  not in allR:
            raise RepositoryExceptionRent("\n           Id doesn't exit. \n".upper())
        allR.remove(bk)
        allR.append(bk)
        self.__storeToFile(allR)


    def find_rent(self, id):
        """
            Find a rent after its id.
        :param id: rent's id
        :return: the entire rent with the given id
        """
        allR=self.__loadFromFile()
        for bk in allR:
            if bk.getId()==id:
                return bk


    def delete_all(self):
        allB=[]
        self.__storeToFile(allB)
