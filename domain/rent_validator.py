class ExceptionValidator3(Exception):
    pass

class RentValidator:
    @staticmethod
    def flagValidator(flag):
        if flag!="1" and flag!="0":
            raise  ExceptionValidator3("\n           the flag has to be equal to 1 or 0. \n".upper())