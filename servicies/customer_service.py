from domain.customer_entity import Customer
from domain.customer_validator import CustomerValidator


class CustomerService:
    def __init__(self, rep, val):
        """
        Initialise service
        :param rep: repository: contains all books instances
        :param val: validator: validates books instances
        """
        self.__rep = rep
        self.__val=val

    def create_customer(self, id, name, cnp):
        """
            Stores a Book
        :param id: customer's id
        :param title: customer's name
        :param description: customer's chp
        :return: the customer

        Raise RepositoryException if book's id already exists in repository
        Raise ValidationException if books's fields are invalid
        """

        self.__val.wholeValidator(id, name, cnp)

        self.__rep.store(id, name, cnp)


    def validate_id(self, id):
        """
            Validates an id if it's a valid and unique one.
        :param id:

        """
        self.__val.idValidator(id)

    def get_all_customers(self):
        """
        :return: the list of all customers
        """

        return self.__rep.get_all_customers()

    def delete_customer(self, id):
        self.__val.idValidator(id)
        self.__rep.delete_customer(id)

    def modify_customer(self, id, name, cnp):
        self.__val.wholeValidator(id, name, cnp)
        self.__rep.modify_customer(id, name, cnp)

    def cautare(self, id):
        """
            Looks for an given id. If id exists in list return the object with all attributes, otherwise throws an exception.
        :param id:  the given id

        """
        self.__val.idValidator(id)
        x=self.__rep.find_customer(id)
        if x is None:
           return  "\n          The customer with id {} doesn't exist. \n".format(id).upper()

        return x

    def delete_all(self):
        """
            Deletes all customers

        """
        if len(self.get_all_customers()):
            self.__rep.delete_all()
        else :
            raise ValueError("\n            There are no customers to delete \n".upper())



