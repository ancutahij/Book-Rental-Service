class ValidatorException(Exception):
    def __init__(self, errors):
        self.errors = errors
        if type(errors) is list:
            self.getErrors()

    def getErrors(self):
        for err in self.errors:
            print (err)


class BookValidator:
    """
        Throws ValidatorException if attributes are invalid.
    """

    @staticmethod
    def idValidator( id, errors=None ):
        if id.strip() is "" :
            if errors is  None:
                raise ValidatorException(" \n    Id must me an unique identifier.  \n ".upper())
            else :

                errors.append("    Id must me an unique identifier.   ".upper())

    @staticmethod
    def titleValidator(title, ok=None, errors=None):

        if title.strip() is "":
            if ok is not None:
                raise ValidatorException("\n     The title cannot be a void one.  \n".upper())
            errors.append("    The title cannot be a void one.  ".upper())

    @staticmethod
    def descriptionValidator(description,  ok=None, errors=None):

        if description.strip() is "":
            if ok is not None:
                raise ValidatorException("\n     The description cannot be a void one. \n ".upper())
            errors.append("    The description cannot be a void one.  ".upper())

    @staticmethod
    def authorValidator(author, ok=None, errors=None):
        if author.strip() is "" or author.isdigit():
            if ok is not None:
                raise ValidatorException("\n     the author's name has to contain letters.  \n ".upper())
            errors.append("    the author's name has to contain letters.  ".upper())


    @staticmethod
    def wholeValidator(id, title, desc, author):
        """
            Validates all attributes.
        :param id:  book's id
        :param title:  book's title
        :param desc:  book's description
        :param author: book's author
        :return: exceptions if attributes are not valid.
        """
        errors=[]
        BookValidator.idValidator(id, errors)
        BookValidator.titleValidator(title,None, errors)
        BookValidator.authorValidator(author,None, errors)
        BookValidator.descriptionValidator(desc,None , errors)
        if len(errors)>0:
            raise ValidatorException(errors)