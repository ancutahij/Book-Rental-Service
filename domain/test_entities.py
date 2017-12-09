from domain.book_entity import Book
from domain.book_validator import BookValidator, ValidatorException
from domain.customer_entity import Customer
from domain.customer_validator import CustomerValidator, ValidatorException2
from domain.rent_entity import Rent
from domain.rent_validator import RentValidator, ExceptionValidator3

import unittest

class TestCaseBookEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.__book1=Book(123,"Gone with the wind","Romance", "Margaret Mitchell")
        cls.__book2=Book(124, "Ion","Realism", "Liviu Rebreanu")
        cls.__book3=Book("","","","")



    @classmethod
    def tearDownClass(cls):
        pass

    def test_getters(self):
        self.assertEqual(self.__book1.getId(), 123)
        self.assertEqual(self.__book2.getId(), 124)
        self.assertEqual(self.__book3.getId(), "")

        self.assertEqual(self.__book1.getTitle(), "Gone with the wind")
        self.assertEqual(self.__book2.getTitle(), "Ion")
        self.assertEqual(self.__book3.getTitle(), "")

        self.assertEqual(self.__book1.getAuthor(), "Margaret Mitchell")
        self.assertEqual(self.__book2.getAuthor(), "Liviu Rebreanu")
        self.assertEqual(self.__book3.getAuthor(), "")

        self.assertIs(self.__book1.getDescription(), "Romance")
        self.assertIs(self.__book2.getDescription(), "Realism")
        self.assertIs(self.__book3.getDescription(), "")


    def test_validators(self):
        with self.assertRaises(ValidatorException):
            BookValidator.idValidator(self.__book3.getId())

        """with self.assertRaises(ValidatorException):
            BookValidator.wholeValidator(self.__book3.getId(), self.__book3.getTitle(), self.__book3.getDescription(), self.__book3.getAuthor())
        """
        with self.assertRaises(ValidatorException):
            BookValidator.titleValidator(self.__book3.getTitle(),1)

        with self.assertRaises(ValidatorException):
            BookValidator.descriptionValidator(self.__book3.getDescription(),1)

        with self.assertRaises(ValidatorException):
            BookValidator.authorValidator(self.__book3.getAuthor(),1)



class TestCaseCustomerEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.__cust1 = Customer("123", "Ion Popescu", "90832423533")
        cls.__cust2 = Customer("1123", "Maria Covali", "90832233533")
        cls.__cust3 = Customer("", "", "")


    @classmethod
    def tearDownClass(cls):
        pass

    def test_getters(self):
        self.assertEqual(self.__cust1.getId(), "123")
        self.assertEqual(self.__cust2.getId(), "1123")
        self.assertEqual(self.__cust3.getId(), "")

        self.assertEqual(self.__cust1.getName(), "Ion Popescu")
        self.assertEqual(self.__cust2.getName(), "Maria Covali")
        self.assertEqual(self.__cust3.getName(), "")


        self.assertTrue(self.__cust1.getCnp()== "90832423533")
        self.assertTrue(self.__cust2.getCnp() ==  "90832233533")
        self.assertTrue(self.__cust3.getCnp()== "")

    def test_validators(self):
        with self.assertRaises(ValidatorException2):
            CustomerValidator.idValidator(self.__cust3.getId())

        """with self.assertRaises(ValidatorException2):
            CustomerValidator.wholeValidator(self.__cust3.getId(), self.__cust3.getName(),self.__cust3.getCnp())
        """
        with self.assertRaises(ValidatorException2):
            CustomerValidator.nameValidator(self.__cust3.getName(), 1)

        with self.assertRaises(ValidatorException2):
            CustomerValidator.cnpValidator(self.__cust3.getCnp(), 1)




class TestCaseRentEntity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.__rent1 = Rent("123", "234", "1", "34")
        cls.__rent2=Rent("324", "23", "12","23")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_getters(self):
        self.assertIs(self.__rent1.get_idCustomer(), "234")
        self.assertIs(self.__rent2.get_idCustomer(), "23")

        self.assertIs(self.__rent1.get_idBook(), "123")
        self.assertIs(self.__rent2.get_idBook(), "324")

        self.assertIs(self.__rent1.get_flag(), "1")
        self.assertIs(self.__rent2.get_flag(), "12")

        self.assertIs(self.__rent1.get_id(), "34")
        self.assertIs(self.__rent2.get_idCustomer(), "23")


    def test_validators(self):
        with self.assertRaises(ExceptionValidator3):
            RentValidator.flagValidator(self.__rent2.get_flag())



if __name__=="__main__":
    unittest.main()








#  OLD TESTS
class Test:
    def __init__(self):
        Test.test_create_book()
        Test.book_validator()
        Test.test_create_customer()
        Test.test_rent()
        Test.test_rent_Validator()

    @staticmethod
    def test_create_book():
        book1=Book(123,"Gone with the wind","Romance", "Margaret Mitchell")
        assert book1.getAuthor()=="Margaret Mitchell"
        assert book1.getDescription()=="Romance"
        assert book1.getId()==123
        assert book1.getTitle()=="Gone with the wind"



    @staticmethod
    def book_validator():
        bk=Book("","","","")

        try :
            BookValidator.idValidator(bk.getId())
            BookValidator.titleValidator(bk.getTitle())
            BookValidator.authorValidator(bk.getAuthor())
            BookValidator.descriptionValidator(bk.getDescription())
            assert False
        except ValidatorException as msg:
            assert True


    @staticmethod
    def test_create_customer():
        cs = Customer("123", "Ion Popescu", 90832423533)
        assert cs.getName() == "Ion Popescu"
        assert cs.getId()=="123"
        assert cs.getCnp()==90832423533

    @staticmethod
    def test_rent():
        object=Rent(123, 234, 1, 34)
        assert object.get_flag()==1
        assert object.get_idBook()==123
        assert object.get_idCustomer()==234
        assert object.get_id() == 34

    @staticmethod
    def test_rent_Validator():
        rent=Rent(12,234, 12, 12)
        try:
            RentValidator.flagValidator(rent.get_flag())
            assert False
        except ExceptionValidator3:
            assert True





x=Test()
