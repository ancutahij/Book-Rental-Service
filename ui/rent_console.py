from random import randint, choice

from domain.book_validator import ValidatorException
from domain.customer_validator import ValidatorException2
from domain.rent_validator import ExceptionValidator3
from repository.rent_repository_validator import RepositoryExceptionRent


class RentConsole():
    def __init__(self,srvRent, srvCustomer, srvBook):
        self.__srvRent=srvRent
        self.__srvCustomer=srvCustomer
        self.__srvBook=srvBook
        self.rents_menu()

    def rents_menu(self):
        x = ""
        if len(self.__srvBook.get_all_books()) == 0:
            x = "Nu exista carti   ".upper()

        if len(self.__srvCustomer.get_all_customers()) == 0:
            x += "Nu exista clienti.".upper()
        if x is not "":
            print("\n      operatiile nu pot fi efectuate: ".upper(), x, " \n")
            return None

        menu = """
            1. Vizualizare lista inchirieri
            2. Adaugare inchiriere/returnare noua
            3. Stergere totala
            4. Cele mai inchiriate carti
            5. Clienti cu carti inchiariate dupa nume si numarul de carti inchiriate
            6. Primii 20% cei mai activi clienti
            7. Adauga n inchirieri
            0. Iesire
        """
        while True:
            print(menu)
            cmd = input("Alege o optiune: ")
            if cmd == "0":
                break
            elif cmd == "1":
                self.show_all_rents()
            elif cmd=="2":
                self.add_rent()

            elif cmd == "3":
                self.delete_rent()

            elif cmd=="4":
                self.the_most_leased_books()
            elif cmd=="5":
                self.sorted_customers()
            elif cmd=="6":
                self.the_most_active_customers()
            elif cmd == "7":
                self.n_entities()
            else:
                print("\n          Optiune invalida \n".upper())

    def add_rent(self):

        try:
            id= input("Da id pentru inchiriere: ")
            idCustomer=input("Da id pentru client: ")
            idBook=input("Da id pentru carte: ")
            flag=input("Da un status: inchirere-1, returnare-0:   ")
            self.__srvRent.create_rent(idCustomer, idBook, flag, id)
            print ("\n            Inchirierea/Returnarea a fost adaugata. \n".upper())

        except ValidatorException2 as msg:
            print (msg)
        except ValidatorException as msg:
            print (msg)
        except ExceptionValidator3 as msg:
            print (msg)
        except ValueError as msg:
            print(msg)
        except RepositoryExceptionRent as msg:
            print (msg)

    def show_all_rents(self):
        """
            Prints out all rents from repository

        """
        bks=self.__srvRent.get_all()
        if len(bks)==0:
            print ("\n          Nu exista instante.\n".upper())
        else:

            for bk in bks:
               try:
                    print (self.__srvRent.display_rent(bk))
               except ValueError as msg:
                   print (msg)
                   break

    """ n_entities(self):
                    Creates a rental list with n entities randomly(n is read by user) using the Book and Customer Services.
        

        while True:
            try:
                n=int(input("Da n mai mare decat zero: "))
                if n<=0:
                    print ("N trebuie sa fie mai mare decat 0.")
                break
            except ValueError :
                print ("\n      N este invalid.\n".upper())

        copie = n
        flags = ["1", "0"]
       # ct = self.__CustRep.get_all_customers()
        #bk = self.__Bookrep.get_all_books()
        ct =self.__srvCustomer
        bk=self.__srvBook

        while n > 0:
            try:
                idCust = choice(ct.get_all_customers()).getId()
                idBook = choice(bk.get_all_books()).getId()
                flag = choice(flags)
                id = "r" + str(randint(1, copie))
                self.__srvRent.create_rent(idCust, idBook, flag, id)
                n-=1
            except RepositoryExceptionRent :
                None

        print ("\n          Au fost adaugate ".upper(), copie, " inchirieri".upper())
    """

    def delete_rent(self):
        """
            Deletes all rents from file

        """
        length= len(self.__srvRent.get_all())
        self.__srvRent.delete_all()
        print ("\n          There were deleted {} rents. ".format(length))


    def the_most_leased_books(self):
        """
            Prints out the most leased books

        """
        print ("The most leased books are:   ")
        #for index, item in enumerate(self.__srvRent.the_most_leased_books() ):
         #   print(index+1,". ", item)
        list=self.__srvRent.the_most_leased_books()
        for item in list:
            print (item.get_title()," with id: ",item.get_id()," was rented by ", item.get_rentedNr(), " times. ")

    def sorted_customers(self):
        """
            Prints out the sorted customers by their name and by the number of their leased books.
        """
        print ("The sorted customers are: ")
        list=self.__srvRent.sorted_customers()
        #for index in range(len(list[0])):
         #   print ("{} (id: {}) rented {} books.".format(list[0][index], list[2][index], list[1][index]))

        for rt in list:
            print ("Customer {}, with id {}, rented {} books: {} "\
                   .format(rt.get_name(), rt.get_id(), rt.get_rentedNr(), rt.get_leased_book()))
    def the_most_active_customers(self):
        """
        Prints out the most 20% active customers (name+id+number of leased books)

        """
        print ("The most 20% customers are: ")
        list=self.__srvRent.the_most_active_customers()
       # for index in range(len(list[0])):
        #    print ("{} (id: {}) rented {} books.".format(list[0][index], list[2][index], list[1][index]))

        for rt in list:
            print("Customer {}, with id {}, rented {} books. ".format(rt.get_name(), rt.get_id(), rt.get_rentedNr()))


    def n_entities(self):
        """
            Loads to file n rents entities

        :return: None
        """
        while True:
            try:
                n=int (input ("Da n: "))
                if n <=0 :
                    print("\n      the number cannot be less than 0.\n".upper())
                    continue
                break
            except ValueError :
                print ("\n      the number is invalid.\n".upper())
        copie =n
        while copie > 0:
            try:
                id_Book =choice(self.__srvBook.get_all_books())
                id_Book=id_Book.getId()
                id_Cust = choice (self.__srvCustomer.get_all_customers())
                id_Cust=id_Cust.getId()
                flag =str(choice([0, 1]))
                id_rent= "r"+str(randint(1,100))
                self.__srvRent.create_rent(id_Cust, id_Book, flag, id_rent)
                copie-=1
            except ValidatorException2 as msg:
                None
            except ValidatorException as msg:
                None

            except ExceptionValidator3 as msg:
                None

            except ValueError as msg:
                None
            except RepositoryExceptionRent as msg:
                None
        print ("\n          There were added {} rents".format(n))