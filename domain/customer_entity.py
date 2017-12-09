class Customer:
    '''
       An instance has the following attributes:
        -id- an unique number for identification
        -name- customer's name
        -CNP

    '''

    numberOfInstances = 0

    def __init__(self, id, name, cnp):
        self.__id = id
        self.__name = name
        self.__cnp = cnp

        Customer.numberOfInstances += 1

    def getId(self):
        return self.__id


    def getName(self):
        return self.__name

    def getCnp(self):
        return self.__cnp


    @staticmethod
    def getNumberOfInstances():
        '''
            Returns the number of instances in Class Book
        '''
        return Customer.numberOfInstances

    def __repr__(self):
        """
            Prints out an instance with its all attributes.
        """
        return "Name: {}, CNP: {}, ID: {} ".format(self.__name, self.__cnp, self.__id)

    def __eq__(self, other):
        """
            Checks out if the customer have the same id

        """
        return self.__id==other.__id