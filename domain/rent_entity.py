

class Rent():
    def __init__(self, idBook, idCustomer, flag, id):
        """
            Transfer data object
        :param idBook: book's id
        :param idCustomer:  customer's id
        :param flag: a flag that have value 1 if the book is rent, 0 othewise
        :param id: the unique identifier of every instance

        """
        self.__idBook=idBook
        self.__idCust=idCustomer
        self.__flag= flag
        self.__id=id

    def get_idBook(self):
        """

        :return: the book's id
        """
        return self.__idBook

    def get_idCustomer(self):
        """

        :return: the customer's id
        """
        return self.__idCust

    def get_flag(self):
        """

        :return: the flag that indicates if the book is available or not
        """
        return self.__flag

    def get_id(self):
        return self.__id

    def __repr__(self):
        """
            Prints out an instance with its all attributes.
        """
        return "Customer's id: {}, Book's id: {}, Status: {},  Identifier: {}".format(self.get_idCustomer(), self.get_idBook(), self.get_flag(), self.get_id())

    def __eq__(self, other):
        """
            Return true if 2 entites have the same id(they are equal), otherwise return false

        """
        return self.__id==other.__id

