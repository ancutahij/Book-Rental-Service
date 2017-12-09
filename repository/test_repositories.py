from domain.book_entity import Book
from domain.customer_entity import Customer
from repository.book_inFile import BooksRepositoryFile
from repository.book_memory import BookRepository, RepositoryExceptionBook
from repository.customer_inFile import CutomersRepositoryFile
from repository.customer_memory import RepositoryExceptionCust
from repository.rent_inFile import RentsRepositoryFile
from repository.rent_memory import RentRepository

import  unittest

from repository.rent_repository_validator import RepositoryExceptionRent


class TestCaseBookRepository (unittest.TestCase):


    def setUp(self):
        #creates files
        #file1.txt doesn't exist
        self.__file1= BooksRepositoryFile("file1.txt")
        self.__file2=BooksRepositoryFile("tests.txt")

    def tearDown(self):
        #delelte all objects from file
        self.__file2.delete_all()

    def test_getAll(self):
        """
        White box
        Tests out if the objects may be load from the given file.
        :return:  None
        """
        """with self.assertRaises(IOError):
            self.__file1.get_all_books()
        """
        self.assertIsNone(self.__file1.get_all_books())
        self.assertIsNotNone(self.__file2.get_all_books())

    def test_store(self):
        """
            Checks out if an given valid instance can be stored in a file
        :return: none
        """
        id="134"
        title="Ion"
        author="Liviu Rebreanu"
        desc="Realism"

        self.__file2.store(id, title,  desc, author)
        books=self.__file2.get_all_books()
        self.assertEqual(books[0].getId(), "134")
        self.assertEqual(books[0].getDescription(), "Realism")
        self.assertEqual(books[0].getAuthor(), "Liviu Rebreanu")
        self.assertEqual(books[0].getTitle(), "Ion")

        #EAFP
        id = "134"
        title = "Ion"
        author = "Liviu Rebreanu"
        desc = "Realism"
        
        with self.assertRaises(RepositoryExceptionBook):
            self.__file2.store(id, title, desc, author)

    def test_delete_book(self):
        """
            Tests out the deleting function
        :return: None
        """
        #trying to delete an element that doesn't exist
        with self.assertRaises(RepositoryExceptionBook):
            self.__file2.delete_book("fictive id")


        #delenting an existed object
        self.__file2.store("12", "Iin",   "Realism", "Liviu Rebreanu",)
        self.__file2.store("13", "Padurea Spanzuratiilor",  "Realism", "Liviu Rebreanu",)


        self.__file2.delete_book("12")
        books=self.__file2.get_all_books()
        self.assertEqual(books[0].getId(), "13")
        self.assertEqual(books[0].getDescription(), "Realism")
        self.assertEqual(books[0].getAuthor(), "Liviu Rebreanu")
        self.assertEqual(books[0].getTitle(), "Padurea Spanzuratiilor")

    def test_update_book(self):
        """
            Tests out if the upade function works properly.
        :return:   None
        """
        #trying to update a book that doesn't exist
        with self.assertRaises(RepositoryExceptionBook):
            self.__file2.modify_book("12", "Iin",  "Liviu Rebreanu", "Realism")

        self.__file2.store("12", "Iin", "Liviu Rebreanu", "Realism")
        self.__file2.store("13", "Padurea Spanzuratiilor", "Liviu Rebreanu", "Realism")
        self.__file2.store("14", "Iin", "Liviu Rebreanu", "Realism")
        books = self.__file2.get_all_books()
        self.__file2.modify_book("12", "Enigma Otiliei", "Realism", "George Calinescu")

        books=self.__file2.get_all_books()
        self.assertEqual(books[-1].getId(), "12")
        self.assertEqual(books[-1].getDescription(), "Realism")
        self.assertEqual(books[-1].getAuthor(), "George Calinescu")
        self.assertEqual(books[-1].getTitle(), "Enigma Otiliei")


    def test_find_book(self):
        """
            Checks out the find_book after id method
        :return: None

        """

        #trying to find a book by an id which doesn't exist
        self.assertIsNone(self.__file2.find_book("23"))

        self.__file2.store("12", "Iin",  "Realism", "Liviu Rebreanu",)
        self.__file2.store("13", "Padurea Spanzuratiilor",  "Realism", "Liviu Rebreanu",)

        bk1= Book("12", "Iin",  "Realism", "Liviu Rebreanu")
        bk2= self.__file2.find_book("12")
        self.assertTrue (bk1 == bk2)
        self.assertTrue (bk1.getAuthor() == bk2.getAuthor())
        self.assertTrue (bk1.getDescription() == bk2.getDescription())
        self.assertTrue (bk1.getTitle() == bk2.getTitle())


class TestCaseCustomerRepository(unittest.TestCase):
    def setUp(self):
        # creates files
        # file1.txt doesn't exist
        self.__file1 = CutomersRepositoryFile("file1.txt")
        self.__file2 = CutomersRepositoryFile("tests.txt")

    def tearDown(self):
        # delelte all objects from file
        self.__file2.delete_all()

    def test_getAll(self):
        """
        White box
        Tests out if the objects may be load from the given file.
        :return:  None
        """
        """with self.assertRaises(IOError):
            self.__file1.get_all_books()
        """
        self.assertIsNone(self.__file1.get_all_customers())
        self.assertIsNotNone(self.__file2.get_all_customers())

    def test_store(self):
        """
            Checks out if an given valid instance can be stored in a file
        :return: none
        """
        id = "134"
        name = "Ion"
        cnp="2324253"

        self.__file2.store(id, name, cnp)
        customers = self.__file2.get_all_customers()
        self.assertEqual(customers[0].getId(), "134")
        self.assertEqual(customers[0].getCnp(), "2324253")
        self.assertEqual(customers[0].getName(), "Ion")


        # EAFP
        id = "134"
        name = "Ion"
        cnp = "2324253"


        with self.assertRaises(RepositoryExceptionCust):
            self.__file2.store(id, name, cnp)


    def test_delete_customer(self):
        """
            Tests out the deleting function
        :return: None
        """
        # trying to delete an element that doesn't exist
        with self.assertRaises(RepositoryExceptionCust):
            self.__file2.delete_customer("fictive id")

        # delenting an existed object
        self.__file2.store("12", "Ion Popescu", "243535436" )
        self.__file2.store("13", "George Avram", "24534363" )

        self.__file2.delete_customer("12")
        books = self.__file2.get_all_customers()
        self.assertEqual(books[0].getId(), "13")
        self.assertEqual(books[0].getName(), "George Avram")
        self.assertEqual(books[0].getCnp(), "24534363")


    def test_update_customer(self):
        """
            Tests out if the upade function works properly.
        :return:   None
        """
        # trying to update a book that doesn't exist
        with self.assertRaises(RepositoryExceptionCust):
            self.__file2.modify_customer("12", "Iin",  "1242545")

        self.__file2.store("12", "Ion Popescu", "243535436")
        self.__file2.store("13", "George Avram", "24534363")
        books = self.__file2.get_all_customers()
        self.__file2.modify_customer("12", "Otilia Grigorovici", "23354643")

        books = self.__file2.get_all_customers()
        self.assertEqual(books[-1].getId(), "12")
        self.assertEqual(books[-1].getName(), "Otilia Grigorovici")
        self.assertEqual(books[-1].getCnp(), "23354643")

    def test_find_customer(self):
        """
            Checks out the find_customer after id method
        :return: None

        """

        # trying to find a book by an id which doesn't exist
        self.assertIsNone(self.__file2.find_customer("23"))

        self.__file2.store("13", "Ion Popescu", "243535436")
        self.__file2.store("12", "George Avram", "24534363")


        bk1 = Customer("12", "George Avram",  "24534363")
        bk2 = self.__file2.find_customer("12")
        self.assertTrue(bk1 == bk2)
        self.assertTrue(bk1.getName() == bk2.getName())
        self.assertTrue(bk1.getCnp() == bk2.getCnp())


class TestCaseRentRepository(unittest.TestCase):
    def setUp(self):
        # creates files
        # file1.txt doesn't exist
        self.__file1 = RentsRepositoryFile("file1.txt")
        self.__file2 = RentsRepositoryFile("tests.txt")

    def tearDown(self):
        # delelte all objects from file
        self.__file2.delete_all()

    def test_getAll(self):
        """
        White box
        Tests out if the objects may be load from the given file.
        :return:  None
        """
        self.assertIsNone(self.__file1.get_all())
        self.assertIsNotNone(self.__file2.get_all())

    def test_store(self):
        """
            Checks out if an given valid instance can be stored in a file
        :return: none
        """
        idCust = "134"
        idBook = "xd2342"
        id="2324"
        flag="1"

        self.__file2.store(idCust, idBook, flag, id)
        rents = self.__file2.get_all()
        self.assertEqual(rents[0].get_idBook(), "xd2342")
        self.assertEqual(rents[0].get_idCustomer(), "134")
        self.assertEqual(rents[0].get_flag(), "1")
        self.assertEqual(rents[0].get_id(), "2324")



        # EAFP

        idCust = "134"
        idBook = "xd2342"
        id="2324"
        flag="1"

        with self.assertRaises(RepositoryExceptionRent):
            self.__file2.store(idCust, idBook, flag, id)

if __name__=="__main__":
    unittest.main()

class Test:
    def __init__(self):
        Test.test_get_size()
        Test.test_store()
        Test.test_delete_book()
        Test.test_modidy_book()
        Test.test_store_rent()
        Test.test_find_afterTitle()

    @staticmethod
    def test_get_size():

        rep=BookRepository()
        assert rep.get_size()==0
        rep.store(123, "Gone with the wind", "Romance", "Margaret Mitchell")
        assert rep.get_size()==1

    @staticmethod
    def test_store():
        rep=BookRepository()

        rep.store(123, "Gone with the wind", "Romance", "Margaret Mitchell")

        try:
            rep.store(123,"Ion ", "Realism", "Liviu Rebreanu")
            assert False
        except RepositoryExceptionBook as msg:
            assert True

    @staticmethod
    def test_delete_book():
        rep = BookRepository()
        rep.store("123", "Ion", "Realism", "Liviu Rebreanu")

        rep.store("124", "Enigma Otiliei", "Realism", "George Calinescu")

        rep.delete_book("123")
        assert len(rep.get_all_books())==1

    @staticmethod
    def test_modidy_book():
        rep = BookRepository()
        rep.store("123", "Ion", "Realism", "Liviu Rebreanu")
        rep.store("124", "Enigma Otiliei", "Realism", "George Calinescu")
        rep.modify_book("123","Moara cu noroc", "Realism", "Ioan Slavici")


        for item in rep.get_all_books():
            if item.getId()=="123":
                assert item.getAuthor()=="Ioan Slavici"
                assert item.getDescription()=="Realism"
                assert item.getTitle()=="Moara cu noroc"
    @staticmethod
    def test_store_rent():
        rep=RentRepository()

        rep.store("123", "89", 1, 12)

        for item in rep.get_all():
            assert item.get_flag()==1
            assert item.get_idBook()=="89"
            assert item.get_idCustomer()=="123"
            assert item.get_id()==12

    @staticmethod
    def test_find_afterTitle ():
        rep=BooksRepositoryFile("..\\tests.txt")
        rep.store("12","Ion","Liviu Rebreanu", "Realism")
        rep.store("11","Ion","Liviu Rebreanu", "Realism")
        rep.store("10","Ion","Liviu Rebreanu", "Realism")

        assert len(rep.find_afterTitle("Ion"))==3

        rep.store("9","Iona","Marin Sorescu", "Realism")

        assert len(rep.find_afterTitle("Iona"))==1

        #clearing the file after testing
        rep.delete_all()


x=Test()


