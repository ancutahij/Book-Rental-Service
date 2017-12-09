from domain.customer_entity import Customer


class RepositoryExceptionCust(Exception):
    pass


class CustomerRepository():

    def __init__(self):
        self.__customers={}

    def get_uniqueID(self, id):
        """
                Raise an exception if the id exist in customers list.
                This function is used for adding a new object in customers list, and the main scope is to have different ids
        :param id:

        """
        for item in self.__customers.values():
            if id == item.getId():
                raise RepositoryExceptionCust("\n       id must be an unique indetifier. \n".upper())

    def get_existedID(self, id):
        """
                Raise an exception  if the id doesn't exit in customers list.
                The function is used for deleting an object after the existed id.
        :param id:
        """
        gasit = 0
        for item in self.__customers.values():
            if id == item.getId():
                gasit = 1
                break

        if gasit is 0:
            raise RepositoryExceptionCust("\n       id must exist. \n".upper())

    def store(self, id: object, name: object, cnp: object) -> object:
        """
        Stores the bk instance of Book class in Books repository.
        Throws an Repository Exccption if the id exists in Books repository.

        :param bk: a instance of Book class

        """
        self.get_uniqueID(id)
        self.__customers[id]=Customer(id,name, cnp)

    def get_size(self):
        """

        :return: Numbers of books instances
        """
        return len(self.__customers)


    def get_all_customers(self):
        """

        :return: a list with all books in repository
        """
        return list(self.__customers.values())


    def get_customers(self):
        return self.__customers

    def delete_customer(self, id):
        """
            Deletes an instance after the id.
        :param id: book's id
        :return: new repository without book with the given id
        """

        self.get_existedID(id)
        for item in self.__customers:
            if item == id:
                del self.__customers[item ]
                break



    def modify_customer(self, id, name, cnp):
        """
            Modify an instance with the given id.
        """

        self.get_existedID(id)
        for item in self.__customers:
            if item == id:
                self.__customers[id]=Customer(id,name, cnp)

    def find_customer(self, id):
        """
            Finds a customers with the given id.
        :param id: customer's id
        :return: the found customer
        """
        if id in self.__customers:
            return self.__customers[id]

