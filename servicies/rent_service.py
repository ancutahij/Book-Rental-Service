from random import randint, choice

from domain.active_customers_entity import ActiveCustomer
from domain.ordered_customers import OrderedCustomer
from domain.rented_books_entity import RentedBook
from repository.rent_repository_validator import Validator


class RentService:
    def __init__(self, Bookrep, Bookval, Custrep, Custval, Rentrep, Rentval):
        """
            The service for rental package
        :param Bookrep:
        :param Bookval:
        :param Custrep:
        :param Custval:
        :param Rentrep:
        :param Rentval:
        """
        self.__Bookval = Bookval
        self.__Bookrep = Bookrep
        self.__CustRep = Custrep
        self.__CustVal = Custval
        self.__Rentrep = Rentrep
        self.__Rentval = Rentval


    def create_rent(self, idCust, idBook, flag, id ):
        """
            Create a new object in rental list.
        :param idCust:
        :param idBook:
        :param flag:
        """

        self.__Bookval.idValidator(idBook)
        # checks out if the book's id exists
        if self.__Bookrep.find_book(idBook) is None:
            raise ValueError("\n            Book's id must exist.\n".upper())

        self.__CustVal.idValidator(idCust)
        if self.__CustRep.find_customer(idCust) is None:
            raise ValueError("\n            Customer's id must exist.\n".upper())

        self.__Rentval.flagValidator(flag)
        self.__Bookval.idValidator(id)

        # repository validations:
        Validator.get_uniqueId(self.__Rentrep.get_all(), id)
        if flag == "1": # we checks out the condition for validy only if we want to make a rent
            Validator.available_book(self.__Rentrep.get_all(),idBook)
            Validator.available_customer(self.__Rentrep.get_all(), idCust)
        else:
            Validator.rented_book(self.__Rentrep.get_all(),idBook, idCust)
        self.__Rentrep.store(idCust, idBook, flag, id)


    def delete_rent(self, id):
        """Deletes a rent after a given id. """

        self.__CustVal.idValidator(id)
        self.__Rentrep.delete_rent(id)


   # def update_rent(self, idCustomer, idBook, id, flag):
    def get_all(self):
        """

        :return: the list of rents

        """
        return self.__Rentrep.get_all()


    def get_all_books(self):
        """

        :return:  the list of books
        """
        return self.__Bookrep.get_all_books()

    def get_all_customers(self):
        """

        :return: the list of customers
        """
        return self.__CustRep.get_all_customers()


    def display_rent(self, rt):
        """
            Displays a rent in a special format
            ie: from: Customer's id: c3, Book's id: b40, Status: 1,  Identifier: r1
                to:   Ion Popescu rented "Enigma Otiliei".

        """
        #get the customer id
        cust = rt.get_idCustomer()
        #get the entire customer with all his attributes
        cust = self.__CustRep.find_customer(cust)
        if cust is None:
            raise ValueError("\n    there must be a problem with date base\n ".upper())
        #get the customer's name
        custName=cust.getName()

        book= rt.get_idBook()
        book=self.__Bookrep.find_book(book)
        if book is None:
            raise ValueError("\n    there must be a problem with date base\n ".upper())

        bookTitle=book.getTitle()

        rez=custName
        rez+=" with id: {}".format(cust.getId())
        if rt.get_flag()=="1":
            rez+=" rented "
        else:
            rez+=" returned "
        rez+=" ' "+bookTitle
        rez += " with id: {} .".format(book.getId())
        return rez

    def getTitle_afterID(self, idBook):
        """
            Get the title of a book from books repository knowing only its id/
        :param idBook: book's unique identifier
        """

        #Catching the entire book object with its all attributes
        book = self.__Bookrep.find_book(idBook)

        #Catching the title
        bookTitle = book.getTitle()
        return bookTitle


    def count_rented_book(self, idBook):
        """
            Returns the number os how many times a book was rented

        """
        allR=self.get_all()
        count=0
        for rt in allR:
            if rt.get_idBook()==idBook and rt.get_flag()=="1":
                count+=1

        return count


    def the_most_leased_books(self):
        allR=self.get_all()
        allRentedBooks=[]
        if allR:
            for rt in allR:
                title=self.getTitle_afterID(rt.get_idBook())
                nr=self.count_rented_book(rt.get_idBook())
                rent=RentedBook(title, rt.get_idBook(), nr)
                if rent not  in allRentedBooks:
                    allRentedBooks.append(rent)

            allRentedBooks.sort( key= lambda x: x.get_rentedNr(), reverse=True)
        return  allRentedBooks

    def getName_afterID(self, id):
        """
            Returns the name for the customer with the given id.
        :param id: customer's unique identifier
        """
        #looking after the customer
        name=self.__CustRep.find_customer(id)
        #extracting the name
        name=name.getName()
        return name

    def get_number_rented_books(self, idCust):
        """
            Returns the number of rented books for a customer.
        :param idCust: customer's id

        """
        nr=0
        allR= self.__Rentrep.get_all()
        for rt in allR:
            if idCust  ==  rt.get_idCustomer() and rt.get_flag()=="1":
                nr+=1

        return nr

    def get_leased_books(self, idCust):
        """
            Returns the list of all leased book per customer
        :param idCust: customer's id
        :return: the list with all books per customer
        """
        books = []
        allR = self.__Rentrep.get_all()
        for rt in allR:
            if idCust == rt.get_idCustomer() and rt.get_flag() == "1":
                books.append(self.getTitle_afterID(rt.get_idBook()))


        return books

    def sorted_customers(self):
        """
            Returns  an ascending list with sorted customers by their name and
            by the number of rented books

        """
        allR=self.get_all()
        sortedCust=[]
        if allR:
            for rt in allR:
                name=self.getName_afterID(rt.get_idCustomer())
                nr=self.get_number_rented_books(rt.get_idCustomer())
                books=self.get_leased_books(rt.get_idCustomer())
                rent=OrderedCustomer(name, rt.get_idCustomer(), nr, books)
                if rent not  in sortedCust:
                    sortedCust.append(rent)

            sortedCust.sort(key=lambda x: x.get_name())


            for index in range (len(sortedCust)-1):
                if sortedCust[index].get_name() == sortedCust[index+1].get_name():
                    if sortedCust[index].get_rentedNr()<sortedCust[index+1].get_rentedNr():
                        sortedCust[index], sortedCust[index+1]= sortedCust[index+1], sortedCust[index]
                        index-=1

        return sortedCust


    def the_most_active_customers(self):
        """
            Creates a list with object like: nameCustomer+idCustomer+number of rented books
            The list is sorted by the number of rented books
        """
        allR = self.get_all()
        sortedCust = []
        if allR:
            for rt in allR:
                name = self.getName_afterID(rt.get_idCustomer())
                nr = self.get_number_rented_books(rt.get_idCustomer())

                rent = ActiveCustomer(name, rt.get_idCustomer(), nr)
                if rent not in sortedCust:
                    sortedCust.append(rent)

            sortedCust.sort(key= lambda x: x.get_rentedNr(), reverse=True )
            n=0.2*len(sortedCust)
            n=round(n)
            return sortedCust[:n]
        return sortedCust


    def delete_all(self):
        """
        Deletes all rents from the file
        :return: a void file
        """
        self.__Rentrep.delete_all()

    """def sorted_customers(self):
        
        #the list of ids
        l_ids=[]

        allR=self.__Rentrep.get_all()
        for rt in allR:
            if rt.get_idCustomer()  not in l_ids:
                #if the l_ids is void or the name of customer is bigger than the last name in list
                if len(l_ids)==0 or self.getName_afterID(l_ids[-1])<self.getName_afterID(rt.get_idCustomer()):
                    l_ids.append(rt.get_idCustomer())
                  #  l_bks.append(rt.get_idCustomer())


                else:
                    # if the last name in ids list and the rt name are equal
                    if self.getName_afterID(rt.get_idCustomer()) == self.getName_afterID(l_ids[-1]) :
                        #checks if the rt numbers of leased books is less then the last element number of books
                        if self.get_number_rented_books(rt.get_idCustomer())>self.get_number_rented_books(l_ids[-1]):
                            l_ids.append(rt.get_idCustomer())
                            #l_bks.append(rt.get_idCustomer())
                            continue

                    #we go throw through the list of ids
                    for poz in range(len(l_ids)):
                        # if the name is smaller, we make the insertion
                        if self.getName_afterID(rt.get_idCustomer()) < self.getName_afterID(l_ids[poz]):
                            l_ids.insert(poz,rt.get_idCustomer() )
                            break

                        #if the names are equals:
                        if self.getName_afterID(rt.get_idCustomer()) == self.getName_afterID(l_ids[poz]):
                            #but the number of rented books for rt is less than l_ids[poz]'s number
                            if self.get_number_rented_books(rt.get_idCustomer())<=self.get_number_rented_books(l_ids[poz]):
                                l_ids.insert(poz, rt.get_idCustomer())
                                break


                            #but the next name is smaller than rt's name, we make the insertion
                            if poz <len(l_ids)-1 and self.getName_afterID(rt.get_idCustomer()) < self.getName_afterID(l_ids[poz+1]):
                                l_ids.insert(poz+1, rt.get_idCustomer())
                                #l_bks.append(rt.get_idCustomer())
                                break

                            #and the next name is equal to rt's name,
                            if poz <len(l_ids)-1 and  self.getName_afterID(rt.get_idCustomer()) == self.getName_afterID(l_ids[poz+1]):
                                #and rt's number of leased book is less than l_ids[poz+1]'s number
                                if self.get_number_rented_books(rt.get_idCustomer())<self.get_number_rented_books(l_ids[poz+1]):
                                    l_ids.insert(poz + 1, rt.get_idCustomer())
                                    break


        #creating the list of number of rented books for every customer
        l_bks=[]
        for id in l_ids:
            l_bks.append(self.get_number_rented_books(id))

        #creating a new list from ids list in names list:
        l_names=[]
        for index in range(len(l_ids)):
            l_names.append(self.getName_afterID(l_ids[index]))

        return [l_names, l_bks, l_ids]
    """

    """def the_most_active_customers(self):
        
            Creates a descending list, by the number of leased books,with customers' ids.
            Creates a new list with number of rented books for the above list
            Creates a names list by converting the ids in names.
            IMPOTANT: The order of elements from the first list is the same for 2 others.

        
        l_ids=[]
        allR = self.__Rentrep.get_all()
        for rt in allR:
            rentID=rt.get_idCustomer()
            if rentID not in l_ids:
                if len(l_ids)==0 or self.get_number_rented_books(rentID)<=self.get_number_rented_books(l_ids[-1]):
                    l_ids.append(rentID)
                    continue

                for index in range(len(l_ids)):
                    if self.get_number_rented_books(rentID)>self.get_number_rented_books(l_ids[index]):
                        l_ids.insert(index, rentID)
                        break

        #the the most 20% active customers
        n=0.2*len(l_ids)
        n=round (n)
        # creating the list of number of rented books for every customer

        l_bks = []
        for id in l_ids[:n]:
            l_bks.append(self.get_number_rented_books(id))

        # creating a new list from ids list in names list:
        l_names = []
        for index in range(n):
            l_names.append(self.getName_afterID(l_ids[index]))

        return [l_names, l_bks, l_ids]
    """




