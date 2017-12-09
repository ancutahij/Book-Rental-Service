class ActiveCustomer:
    def __init__(self, name, id, rentedNr):
        """
            There is a new class that uses the DTO(data transfer objects)
        :param name: the customer's name
        :param id:      the cust's id
        :param rentedNr: the number of rented book per customer


        """
        self.__name = name
        self.__id=id
        self.__rentedNR=rentedNr



    def get_name(self):
        """
            Getter for name
        :return: title
        """
        return self.__name

    def get_id(self):
        """
            GEtter for id
        :return: return id
        """
        return self.__id
    def get_rentedNr(self):
        """Getter for rentedNr"""
        return  self.__rentedNR


    def __eq__(self, other):
        return self.get_id()==other.get_id()

    def __repr__(self):
        return "Name: {}, ID: {}, Number: {}".\
            format(self.get_name(),self.get_id(), self.get_rentedNr())