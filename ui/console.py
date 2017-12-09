from ui.book_console import BookConsole
from ui.customer_console import CustomerConsole
from ui.rent_console import RentConsole


class Console:
    def __init__(self, srvBook, srvCustomer, srvRent):

        self.__srvBook=srvBook
        self.__srvCustomer=srvCustomer
        self.__srvRent=srvRent
        self.runUI()


    def runUI(self):
        msg="""
            ==== Meniu Principal ====
            1. Submeniul de carti
            2. Submeniul de clienti
            3. Submeniul de inchirieri
            0. Iesire
        """
        op={"1":BookConsole, "2":CustomerConsole, "3":RentConsole}
        while True:
            try:
                print (msg)
                cmd=input("Da o comanda: ")
                if cmd=="0":
                    print ("La revedere")
                    break
                elif cmd=="1":
                    op["1"](self.__srvBook)
                elif cmd=="2":
                    op["2"](self.__srvCustomer)
                elif cmd=="3":
                    op["3"](self.__srvRent, self.__srvCustomer, self.__srvBook)

            except KeyError:
                print ("\n          Optiune invalida.\n ".upper())




