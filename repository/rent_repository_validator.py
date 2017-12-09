from repository.rent_memory import RentRepository


class RepositoryExceptionRent(Exception):
    pass


class Validator():


    @staticmethod
    def get_uniqueId(rentalList, id):

        """
            Raise an exception if the rent's id already exists in the rental list
        :param id: the unique identifier

        """
        for i in rentalList:
            if id==i.get_id():
                raise RepositoryExceptionRent("\n           The given id exists.\n".upper())



    @staticmethod
    def available_customer(rentalList, idCustomer):
        """
            Validates if an existed customer has a rent book at the moment.
            If the answer is yes, the customer is not able to rent another book.
        :param rentalList:  rental list
        :param idCustomer:  customer's id
        """
        for rent in reversed(rentalList):
            if idCustomer == rent.get_idCustomer():
                if rent.get_flag()=="1":
                    raise RepositoryExceptionRent ("\n        The customer has already a rented book. \n".upper())
                else:
                    break
                    
                    
    @staticmethod
    def available_book(rentalList, idBook):
        """
            Validates if an existed book is rented or not at the moment.
            If the book is rented, then it's thrown an exception. 
            Othervise the book can be rented.
        :param rentalList: rental list
        :param idBook: book's id
        
        """
        for rent in reversed(rentalList):
            if idBook == rent.get_idBook():
                if rent.get_flag() == "1":
                    raise RepositoryExceptionRent ("\n          The book is already rented.     \n".upper())
                else:
                    break

    @staticmethod
    def rented_book(rentalList, idBook, idCustomer):
        """
            A book can be returned to the library only if it's by the same person who rented.
            The book cannot be returned by somebody else or it cannod be returned if it was never rented.
        :param rentalList:  rental book
        :param idBook:   book's id
        :param idCustomer: customer's id

        """
        gasit=0
        if len(rentalList) is 0:
            raise RepositoryExceptionRent("\n          The book cannot be returned because it was never rented    \n".upper())
        for rent in reversed(rentalList):
            if idBook == rent.get_idBook():
                if rent.get_flag()=="0":
                    raise RepositoryExceptionRent("\n          The book cannot be returned because it was never rented.     \n".upper())
                if rent.get_idCustomer()!=idCustomer:
                    raise RepositoryExceptionRent("\n          The book cannot be returned by somebody else, except the person who rented.".upper())


            if idCustomer==rent.get_idCustomer():
                gasit=1
                if idBook!=rent.get_idBook():
                    raise RepositoryExceptionRent ("\n        The customer has to return the same book.\n ".upper())
            # if idCustomer==rent.get_idCustomer():
            #    if rent.get_flag()=="1" and idBook!=rent.get_idCustomer():
            #        raise RepositoryExceptionRent("\n          A customer can only rent a book.\n".upper())
                break
        if gasit==0:
            raise RepositoryExceptionRent("\n      The customer has to rent a book firstly.\n".upper())

def test_get_uniqueId():
    """
        Checks out if an given id exists in our rental list.
    :return: none
    """
    rep=RentRepository()
    rep.store("12","23","1", "1")
    try:

        idBook="13"
        idCustomer="54"
        flag="1"
        id="1"
        Validator.get_uniqueId(rep.get_all(),id)
        assert False

    except RepositoryExceptionRent as msg:
        assert True


def test_available_customer():
    """
        Checks out if available_customer function works properly.

    """
    rep = RentRepository()
    rep.store( '23','12', '1', '1')
    try:

        idBook = '13'
        idCustomer = '23'
        flag = '1'
        id = '1'
        Validator.available_customer(rep.get_all(), idCustomer)
        assert False

    except RepositoryExceptionRent as msg:
        assert True


def test_available_book():
    """
            Checks out if available_book function works properly.

        """
    rep = RentRepository()
    rep.store( '23','12',  '1', '1')
    try:

        idBook = '12'
        idCustomer = '22'
        flag = '1'
        id = '1'
        Validator.available_book(rep.get_all(), idBook)

        assert False

    except RepositoryExceptionRent as msg:
        assert True

def test_rented_book():
    rep = RentRepository()
    try:
       # rep.store("c1", "b1", "0","2324")
        Validator.rented_book(rep.get_all(), "b1", "c1")
        assert False
    except RepositoryExceptionRent as msg:
        assert True

    rep.store("c1", "b1", "1", "2324")
    #trying to return a book by the somebody else, except person who rented it
    try:
        Validator.rented_book(rep.get_all(), "b1", "c2")
        assert False
    except RepositoryExceptionRent :
        assert True



test_available_book()
test_available_customer()
test_get_uniqueId()
test_rented_book()
