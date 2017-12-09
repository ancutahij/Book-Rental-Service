class RentedBook:
    def __init__(self, title, id, rentedNr):
        """
            There is a new class that uses the DTO(data transfer objects)
        :param title: the book's title
        :param id:      the book's id
        :param rentedNr:    number of how many times the book was rented
        """
        self.__title = title
        self.__id=id
        self.__rentedNR=rentedNr


    def get_title(self):
        """
            Getter for title
        :return: title
        """
        return self.__title

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
        return "Title: {}, ID: {}, Number: {}".format(self.get_title(),self.get_id(), self.get_rentedNr())