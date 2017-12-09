from domain.book_entity import Book
from domain.book_validator import BookValidator, ValidatorException
from domain.customer_entity import Customer
from domain.customer_validator import CustomerValidator, ValidatorException2
from domain.rent_validator import RentValidator
from domain.rented_books_entity import RentedBook
from repository.book_inFile import BooksRepositoryFile
from repository.book_memory import BookRepository, RepositoryExceptionBook
from repository.customer_inFile import CutomersRepositoryFile
from repository.customer_memory import CustomerRepository
from repository.rent_inFile import RentsRepositoryFile
from repository.rent_memory import RentRepository
from repository.rent_repository_validator import RepositoryExceptionRent
from servicies.book_service import BookService
from servicies.customer_service import CustomerService
from servicies.rent_service import RentService
import unittest


import unittest
class TestCaseBookService(unittest.TestCase):
    def setUp(self):

        self.__srv=BookService(BooksRepositoryFile("tests.txt"), BookValidator())
    def tearDown(self):
        self.__srv.delete_all()
        #BookService.delete_all(self.__book)


    def test_create_book(self):
        """
        BLACK BOX TESTING
        We don't know how our code is supposed to look.
        We only know what the code should do (throwing errors, adding books, etc)
        :return: none
        """

        id_invalid = ""
        title_invalid = ""
        description_invalid = ""
        author_invalid=""


        """with self.assertRaises(ValidatorException):
            BookValidator.idValidator(self.__book.getId())

        with self.assertRaises(ValidatorException):
            BookValidator.titleValidator(self.__book.getTitle(),1)

        with self.assertRaises(ValidatorException):
            BookValidator.descriptionValidator(self.__book.getDescription(),1)

        with self.assertRaises(ValidatorException):
            BookValidator.authorValidator(self.__book.getAuthor(),1)
            
        
        with self.assertRaises(ValidatorException):
            self.__srv.create_book(id_invalid,title_invalid,description_invalid, author_invalid)
        """

        id_valid="12"
        title_valid="Ion"
        author_valid="Liviu Rebreanu"
        description_valid="Realism"
        self.__srv.create_book(id_valid, title_valid, description_valid, author_valid)
        books=self.__srv.get_all_books()
        bk=Book(id_valid, title_valid, description_valid, author_valid)

        self.assertEqual(books[0] ,bk)


class TestCaseCustomerService(unittest.TestCase):
    def setUp(self):
        self.__srv = CustomerService(CutomersRepositoryFile("tests.txt"), CustomerValidator())

    def tearDown(self):
        self.__srv.delete_all()
        # BookService.delete_all(self.__book)

    def test_create_customer(self):
        """
        Checks the create_customer fucntion
        :return: none
        """

        id_invalid = ""
        name_invalid = ""
        cnp_invalid = ""

        """with self.assertRaises(ValidatorException2):
            self.__srv.create_customer(id_invalid, name_invalid, cnp_invalid)
        """

        id_valid = "12"
        name_valid = "Ion"
        cnp_valid = "232345"

        self.__srv.create_customer(id_valid, name_valid, cnp_valid)
        custs = self.__srv.get_all_customers()
        ct = Customer(id_valid, name_valid, cnp_valid)

        self.assertEqual(custs[0], ct)


class TestCaseRentService(unittest.TestCase):
    def setUp(self):
        self.__srvBook=BookService(BooksRepositoryFile("bks.txt"), BookValidator())
        self.__srvCust=CustomerService(CutomersRepositoryFile("cts.txt"), CustomerValidator())
        self.__srvRent = RentService(BooksRepositoryFile("bks.txt"), BookValidator(),CutomersRepositoryFile("cts.txt"),\
                                     CustomerValidator(),RentsRepositoryFile("tests.txt"), RentValidator())

    def tearDown(self):
        self.__srvBook.delete_all()
        self.__srvCust.delete_all()
        self.__srvRent.delete_all()

    def test_create_rent(self):
        """
            Checks out if the create_rent function work properly
        :return: None
        """

        self.__srvBook.create_book("1342","Enigma Otiliei", "Realism", "Liviu Rebreanu")
        self.__srvBook.create_book("1343","Morometii", "Realism", "Marin Preda")
        self.__srvBook.create_book("1344","Iona", "Realism", "Marin Sorescu")

        self.__srvCust.create_customer("55", "Ion Gheorghe", "99927373")
        self.__srvCust.create_customer("56", "Ioana Gheorghe", "9923243373")
        self.__srvCust.create_customer("57", "Marin Preda", "999272331")

        #invalid id for customer
        with self.assertRaises(ValidatorException2):
            self.__srvRent.create_rent("", "1342", "1", "133")


        # invalid id for book
        with self.assertRaises(ValidatorException):
            self.__srvRent.create_rent("56", "", "1", "133")

        # id which doesn't exit
        with self.assertRaises(ValueError):
            self.__srvRent.create_rent("12", "231", "1", "133")

        self.__srvRent.create_rent("55", "1342", "1","224")
        allR=self.__srvRent.get_all()
        self.assertEqual(allR[0].get_idCustomer(), "55")
        self.assertEqual(allR[0].get_idBook(), "1342")
        self.assertEqual(allR[0].get_flag(), "1")
        self.assertEqual(allR[0].get_id(), "224")

    def test_the_most_leased_books(self):
        """
            BLACK BOX TESTING
            We don't know how the code is supposed to look.
            We only know what the code should do.
        :return: None
        """
        #the files the contain books, customers and rents are empthy
        #they have to be populated first

        #creating books objects
        self.__srvBook.create_book("1342", "Enigma Otiliei", "Realism", "Liviu Rebreanu")
        self.__srvBook.create_book("1343", "Morometii", "Realism", "Marin Preda")
        self.__srvBook.create_book("1344", "Iona", "Realism", "Marin Sorescu")

        #creating customers objects
        self.__srvCust.create_customer("55", "Ion Gheorghe", "99927373")
        self.__srvCust.create_customer("56", "Ioana Gheorghe", "9923243373")
        self.__srvCust.create_customer("57", "Marin Preda", "999272331")

        #checking what is going to happen if there are no rents in file
        #if there are no rents, the length of leasedBooks should be 0
        leasedBooks= self.__srvRent.the_most_leased_books()
        self.assertEqual(len(leasedBooks),0)

        #creating rents objects
        self.__srvRent.create_rent("55","1342", "1", "243")
        self.__srvRent.create_rent("55","1342", "0", "244")
        self.__srvRent.create_rent("56","1342", "1", "245")
        self.__srvRent.create_rent("57","1343", "1", "246")
        self.__srvRent.create_rent("56","1342", "0", "247")
        self.__srvRent.create_rent("56","1342", "1", "248")

        leasedBooks = self.__srvRent.the_most_leased_books()
        #there are 2 books, so the length should be 2
        self.assertEqual(len(leasedBooks),2)
        #checks if the order is correct
        self.assertTrue(leasedBooks[0].get_title() == "Enigma Otiliei")
        self.assertTrue(leasedBooks[0].get_id() == "1342")
        self.assertTrue(leasedBooks[0].get_rentedNr() == 3)


        self.assertTrue(leasedBooks[1].get_title() == "Morometii")
        self.assertTrue(leasedBooks[1].get_id() == "1343")
        self.assertTrue(leasedBooks[1].get_rentedNr() == 1)

        #what will it happen if we ask for an element on a position that doesn't exit.
        with self.assertRaises(IndexError):
            self.assertTrue(leasedBooks[2].get_title() == None)




    def test_sorted_customers(self):
        """
            Checks out if the sorted customers work properly
        :return: None
        """

        # creating books objects
        self.__srvBook.create_book("1342", "Enigma Otiliei", "Realism", "Liviu Rebreanu")
        self.__srvBook.create_book("1343", "Morometii", "Realism", "Marin Preda")
        self.__srvBook.create_book("1344", "Iona", "Realism", "Marin Sorescu")

        # creating customers objects
        self.__srvCust.create_customer("55", "Ion Gheorghe", "99927373")
        self.__srvCust.create_customer("57", "Marin Preda", "999272331")
        self.__srvCust.create_customer("56", "Ion Gheorghe", "9923243373")



        #checking what is going to happen if there are no rents in file
        #if there are no rents, the length of leasedBooks should be 0
        leasedBooks= self.__srvRent.sorted_customers()
        self.assertEqual(len(leasedBooks),0)

        #creating rents objects
        self.__srvRent.create_rent("55","1342", "1", "243")
        self.__srvRent.create_rent("55","1342", "0", "244")
        self.__srvRent.create_rent("56","1342", "1", "245")
        self.__srvRent.create_rent("57","1343", "1", "246")
        self.__srvRent.create_rent("56","1342", "0", "247")
        self.__srvRent.create_rent("56","1342", "1", "248")

        leasedBooks= self.__srvRent.sorted_customers()
        self.assertTrue(leasedBooks[0].get_name() == "Ion Gheorghe")
        self.assertTrue(leasedBooks[0].get_id() == "56")
        self.assertTrue(leasedBooks[0].get_rentedNr() == 2)

        self.assertTrue(leasedBooks[1].get_name() == "Ion Gheorghe")
        self.assertTrue(leasedBooks[1].get_id() == "55")
        self.assertTrue(leasedBooks[1].get_rentedNr() == 1)

        self.assertTrue(leasedBooks[2].get_name() == "Marin Preda")
        self.assertTrue(leasedBooks[2].get_id() == "57")
        self.assertTrue(leasedBooks[2].get_rentedNr() == 1)

    def test_the_most_active_customers(self):
        """
            Checks out if the the rapport:  the most 20% active customers is made properly
        :return: None
        """

        # creating books objects
        self.__srvBook.create_book("1342", "Enigma Otiliei", "Realism", "Liviu Rebreanu")
        self.__srvBook.create_book("1343", "Morometii", "Realism", "Marin Preda")
        self.__srvBook.create_book("1344", "Iona", "Realism", "Marin Sorescu")

        # creating customers objects
        self.__srvCust.create_customer("55", "Ion Gheorghe", "99927373")
        self.__srvCust.create_customer("57", "Marin Preda", "999272331")
        self.__srvCust.create_customer("56", "Ion Gheorghe", "9923243373")



        #checking what is going to happen if there are no rents in file
        #if there are no rents, the length of leasedBooks should be 0
        leasedBooks= self.__srvRent.the_most_active_customers()
        self.assertEqual(len(leasedBooks),0)

        #creating rents objects
        self.__srvRent.create_rent("55","1342", "1", "243")
        self.__srvRent.create_rent("55","1342", "0", "244")
        self.__srvRent.create_rent("56","1342", "1", "245")
        self.__srvRent.create_rent("57","1343", "1", "246")
        self.__srvRent.create_rent("56","1342", "0", "247")
        self.__srvRent.create_rent("56","1342", "1", "248")

        leasedBooks= self.__srvRent.the_most_active_customers()
        self.assertTrue(leasedBooks[0].get_name() == "Ion Gheorghe")
        self.assertTrue(leasedBooks[0].get_id() == "56")
        self.assertTrue(leasedBooks[0].get_rentedNr() == 2)

        with self.assertRaises(IndexError):
            self.assertTrue(leasedBooks[1].get_name() == None)




if __name__=="__main__":
    unittest.main()

class Test:
    def __init__(self):
        #Test.test_create_book()
        Test.test_create_rent()


    @staticmethod
    def test_create_book():
        rep=BookRepository()
        val=BookValidator()
        srv= BookService(rep,  val)
        srv.create_book("123","Ion","Realism", "Liviu Rebreanu")
        bk=srv.get_all_books()
        assert bk[0].getId()=="123"
        assert bk[0].getDescription()=="Realism"
        assert bk[0].getAuthor()=="Liviu Rebreanu"
        assert bk[0].getTitle()=="Ion"

        try:
            bk = srv.create_book("123", "Enigma Otiliei", "Realism", "George Calinescu")
            assert False
        except RepositoryExceptionBook :
            assert True



    @staticmethod
    def test_create_rent():
        """
            Checks out if the the function create_list from rent service adds only valid instances in rental list.
        :return:
        """
        #creating repositories and validators
        rep_book = BookRepository()
        val_book = BookValidator()
        rep_customer = CustomerRepository()
        val_customer = CustomerValidator()
        rep_rent = RentRepository()
        val_rent = RentValidator()

        #creating services
        srv_book = BookService(rep_book, val_book)
        srv_cust = CustomerService(rep_customer, val_customer)
        srv_rent = RentService(rep_book, val_book, rep_customer, val_customer, rep_rent, val_rent)

        srv_book.create_book("123","Ion","Realism", "Liviu Rebreanu")
        srv_book.create_book("23", "Ion", "Realism", "Liviu Rebreanu")

        srv_cust.create_customer("65", "Ion Popescu", "123323240")
        srv_cust.create_customer("66", "Radu Popescu", "143533323240")

        #getting the necessary ids
        bk=srv_book.get_all_books()
        idBook=bk[0].getId()

        ct =srv_cust.get_all_customers()
        idCust=ct[0].getId()

        id="12"
        flag ="1"
        srv_rent.create_rent(idCust, idBook,flag, id)

        #the customer with a rented book tryes to rent another one
        try:
            srv_rent.create_rent(idCust, "23", "1", "123")
            assert False
        except RepositoryExceptionRent as msg:
            assert True

        #trying to rent a book witch is alreadt taken
        try:
            srv_rent.create_rent("66", idBook, "1", "123")
            assert False
        except RepositoryExceptionRent  as msg:
            assert True


x=Test()