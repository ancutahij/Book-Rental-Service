from domain.rent_entity import Rent




class RentRepository():
    def __init__(self):
        """
            The repository for all rents contains all customer's id that rent a book.
            The repository keeps the history even if the customer's book was given back.
            That thing is possible due a flag that indicates id the book is or not rent anymore
        """
        self.__rents=[]


    def store(self,  idCustomer,idBook, flag, id):

        """
            Adds a new object in our current rental list.
        :param idBook: book's id
        :param idCustomer: customer's id
        :param flag: indicator
        :param id: the unique identifier for a rent

        """


        #self.get_uniqueId(self.__rents, id)
        self.__rents.append(Rent( idBook,idCustomer,  flag, id))


    def get_all(self):
        """
        :return: all instances from RentRepository
        """
        return self.__rents





