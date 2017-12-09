from domain.book_validator import BookValidator
from domain.customer_validator import CustomerValidator
from domain.rent_validator import RentValidator
from repository.book_inFile import  BooksRepositoryFile
from repository.customer_inFile import CutomersRepositoryFile
from repository.rent_inFile import RentsRepositoryFile
from servicies.book_service import BookService
from servicies.customer_service import CustomerService
from servicies.rent_service import RentService
from ui.console import Console

from  domain.test_entities import *
import repository.test_repositories
import servicies.test_servicies
#unittest.main()


#creating repositories and validators

#rep_book=BookRepository()
rep_book=BooksRepositoryFile("books.txt")
val_book=BookValidator()
#rep_customer=CustomerRepository()
rep_customer=CutomersRepositoryFile("customers.txt")
val_customer=CustomerValidator()
#rep_rent=RentRepository()
rep_rent=RentsRepositoryFile("rents.txt")
val_rent=RentValidator()


#creating services
srv_book=BookService(rep_book, val_book)
srv_cust=CustomerService(rep_customer, val_customer)
srv_rent=RentService(rep_book, val_book, rep_customer, val_customer, rep_rent, val_rent)



x=Console(srv_book, srv_cust, srv_rent)