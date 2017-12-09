from domain.customer_entity import Customer
from repository.customer_memory import RepositoryExceptionCust


class CutomersRepositoryFile():
    def __init__(self, fileC):
        """
            Creates the customers repository
        :param fileC: the place where cutomers with their attributes are stored.
        """
        self.__fileC=fileC

    def __loadFromFile(self):
        """
            Loads the customers from file
            Raises an IOError if the file can not be reached (for instance is wasn't create yet)
        :return: a list with all books
        """
        try:
            f=open(self.__fileC, "r")

        except IOError:
            # the file cannot be reached
            return None#("\n      The file cannot be reached\n".upper())

        line =f.readline().strip()
        rez=[]
        while line!="":
            attrs=line.split(",")
            ct=Customer(attrs[0], attrs[1],   attrs[2])
            rez.append(ct)
            line=f.readline().strip()
        f.close()
        return rez




    def store(self, id, name, cnp):
        """
            Stores the new book to the file
        :param id: cust's id
        :param name: cust's name
        :param cnp: cnp's cnp

        """
        allC=self.__loadFromFile()

        ct=Customer(id,name, cnp)
        if allC:
            if ct in allC:
                raise  RepositoryExceptionCust("\n      Duplicated id  \n".upper())

        else:
            allC=[]
        allC.append(ct)
        self.__storeToFile(allC)


    def __storeToFile(self, allC):
        """
            Stores all cutomers in the file
        :param allC: all customers

        """
        with open(self.__fileC, "w") as f:
            for ct in allC:
                f.write(ct.getId()+","+ct.getName()+","+ct.getCnp()+","+"\n")

    def get_all_customers(self):
        """

        :return: the list of all cutomers
        """
        return self.__loadFromFile()

    def delete_customer(self, id):
        """
            Deletes a book by its unique id
        """
        allC=self.__loadFromFile()

        poz=-1
        for index in range(len(allC)):
            if allC[index].getId()==id:
                poz=index
                break
        if poz<0:
            raise RepositoryExceptionCust("\n       The id doesn't exist. \n".upper())

        del allC[poz]
        self.__storeToFile(allC)


    def modify_customer(self, id, name, cnp):
        """
            Modify an instance with the given id.
        """
        allC=self.__loadFromFile()
        bk=Customer(id, name, cnp)
        if bk not  in allC:
            raise RepositoryExceptionCust("\n          The id doesn't exist. \n".upper())
        allC.remove(bk)
        allC.append(bk)
        self.__storeToFile(allC)



    def find_customer(self, id):
        """
            Find a customer after its id.
        :param id: customer's id
        :return: the customer with the given id
        """
        allC=self.__loadFromFile()
        for ct in allC:
            if ct.getId()==id:
                return ct

    def delete_all(self):
        """
            Deletes all customers that can be found in the file.
        :return: a void file/list
        """
        allC=[]
        self.__storeToFile(allC)



