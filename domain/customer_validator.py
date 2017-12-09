class ValidatorException2(Exception):

    def __init__(self, errors):
        self.errors = errors
        if type(errors) is list:
            self.getErrors()

    def getErrors(self):
        for err in self.errors:
            print(err)

class CustomerValidator:
    """
        Throws ValidatorException if attributes are invalid.
    """


    @staticmethod
    def idValidator(id, errors=None):
        if id.strip() is "":
            if errors is  None:
                raise ValidatorException2(" \n    Id must me an unique identifier.  \n ".upper())
            else :
                errors.append("    Id must me an unique identifier.   ".upper())


    @staticmethod
    def nameValidator(name,ok=None ,  errors=None):

        x = name.split(" ")
        for nm in x:
            if not nm.isalpha():
                if ok is not None:
                    raise ValidatorException2("\n     The name has to contain letters.  \n".upper())
                errors.append("    The name has to contain letters.   ".upper())


    @staticmethod
    def cnpValidator(cnp, ok= None ,errors= None):
        if cnp.strip().isalpha() or cnp.strip()=="":
            if ok is not None:
                raise ValidatorException2("\n     The CNP cannot be a void one or contain letters . \n ".upper())
            errors.append("    The CNP cannot be a void one or contain letters   ".upper())

    @staticmethod
    def wholeValidator(id, name, cnp):
        """
            Validates all attributes.
        :param id:  cutomer's id
        :param name: customer's name
        :param cnp: customer's cnp
        :return:    exceptions if attributes are not valid.
        """
        errors=[]
        CustomerValidator.idValidator(id,errors)
        CustomerValidator.nameValidator(name,None, errors)
        CustomerValidator.cnpValidator(cnp,None, errors)

        if len(errors)>0:
            raise ValidatorException2(errors)