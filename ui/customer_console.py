from random import randint, choice

from domain.customer_validator import ValidatorException2
from repository.customer_memory import RepositoryExceptionCust


class  CustomerConsole():
    def __init__(self, srvCustomer):
        self.__srvCustomer=srvCustomer
        self.customers_menu()

    def customers_menu(self):
        menu = """

            ===== Menu clienti ======
            1. Afisare lista de clienti
            2. Adaugare client nou
            3. Stergere client dupa id
            4. Modificare client dupa id
            5. Cautare dupa id
            6. Adaugare random n clienti
            7. Stergere totala
            0. Iesire

        """
        while True:
            print(menu)

            cmd = input("Da o comanda: ")
            if cmd == "1":
                self.show_all_customers()
            elif cmd == "2":
                self.add_customer()
            elif cmd == "3":
                self.delete_customer()
            elif cmd == "4":
                self.modify_customer()
            elif cmd == "5":
                self.cautare_carte()
            elif cmd == "6":
                self.n_entitati()
            elif cmd == "7":
                self.delete_all()
            elif cmd == "0":
                break
            else:
                print("\n      Comanda invalida.\n ".upper())

    def show_all_customers(self):
        """
            Prints out all customers from repository

        """

        bks = self.__srvCustomer.get_all_customers()
        if bks == None :
            print ("\n      The file cannot be reached. \n".upper())
        elif len(bks)==0:
            print("\n          Nu exista instante. \n".upper())

        else:

            print("id          nume          cnp".upper())
            for bk in bks:
                print(bk)

    def add_customer(self):
        while True:
            try:
                id = input("Da id: ")
                name = input("Da name: ")
                cnp = input("Da CNP: ")
                bk = self.__srvCustomer.create_customer(id, name, cnp)
                break
            except ValidatorException2:
                None
            except RepositoryExceptionCust as msg:
                print(msg)

        print("\n          Clientul  a fost adaugat.\n".upper())

    def delete_customer(self):
        if (len(self.__srvCustomer.get_all_customers()) > 0):
            while True:
                try:
                    id = input("Da un id: ")

                    self.__srvCustomer.delete_customer(id)
                    break
                except ValidatorException2 as msg:
                    print(msg)
                except RepositoryExceptionCust as msg:
                    print(msg)

            print("\n      Instanta a fost stearsa.\n".upper())
        else:
            print("\n          Nu exista instante de sters.  \n".upper())

    def modify_customer(self):
        if len(self.__srvCustomer.get_all_customers()) > 0:

            while True:
                try:
                    id = input("Da id:")
                    name = input("Da nume nou: ")
                    cnp = input("Da cnp: ")
                    self.__srvCustomer.modify_customer(id, name, cnp)
                    break
                except ValidatorException2:
                    None
                except RepositoryExceptionCust as msg:
                    print(msg)
            print("\n            Instanta a fost modificata.".upper())

        else:
            print("\n          Nu exista instante de modificat.  \n".upper())

    def cautare_carte(self):
        if len(self.__srvCustomer.get_all_customers()) > 0:
            while True:
                try:
                    id = input("Da id pentru cautare: ")
                    print(self.__srvCustomer.cautare(id))
                    break
                except ValidatorException2 as msg:
                    print(msg)

        else:
            print("\n          Nu exista instante.  \n".upper())


    def n_entitati(self):
        """
            Generates n valid entities randomly.

        """
        while True:
            try:
                n=int(input("Da n mai mare decat zero: "))
                if n<=0:
                    print ("N trebuie sa fie mai mare decat 0.")
                    continue
                break
            except ValueError :
                print ("\n      N este invalid.\n".upper())

        names = ["Ion", "George", "Alina", "Mihai", "Ana", "Mihai", "Ioana", "Otilia"]
        copie = n
        while n > 0:
            try:
                id = "c"+str(randint(1, 100))
                name = choice(names)
                cnp = str(randint(1234, 90909090))
                self.__srvCustomer.create_customer(id, name, cnp)
                n -= 1
            except ValidatorException2:
                None
            except RepositoryExceptionCust:
                None

        print("\n      Au fost adaugati ".upper(), copie, "clienti. \n".upper())



    def delete_all(self):
        try:
            lung = len(self.__srvCustomer.get_all_customers())
            self.__srvCustomer.delete_all()
            print ("\n          There were deleted ".upper(),lung," customers from file \n".upper())

        except ValueError as msg:
            print (msg)



