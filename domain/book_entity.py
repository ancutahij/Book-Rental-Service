
class Book:
    '''
       An instance has the following attributes:
        -id- an unique number for identification
        -title- the title of the book
        -description- the genre of the book
        - author- the author of the book
    '''

    numberOfInstances = 0

    def __init__(self, id, title, description, author):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        Book.numberOfInstances += 1

    def getId(self):
        return self.__id


    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getAuthor(self):
        return self.__author

    @staticmethod
    def getNumberOfInstances():
        '''
            Returns the number of instances in Class Book
        '''
        return Book.numberOfInstances

    def __repr__(self):
        """
            Prints out an instance with its all attributes.
        """
        return "Title: {}       , Description: {},       Author: {},         Id: {} ".format(self.__title, self.__description, self.__author, self.__id)


    def __eq__(self, other):
        """
            Checks out if 2 books have the same id
        """
        return self.__id==other.__id