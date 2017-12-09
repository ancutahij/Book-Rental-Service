from random import randint, choice
from domain.book_validator import ValidatorException
from repository.book_memory import RepositoryExceptionBook



class BookConsole():

    def __init__(self, srvBook):
        self.__srvBook=srvBook
        self.books_menu()


    def books_menu(self):
        menu = """
            ===== Menu carti ======
            1. Afisare lista de carti
            2. Adaugare carte noua
            3. Stergere carte dupa id
            4. Modificare carte dupa id
            5. Afisare carti ordonate dupa titlu
            6. Cautare dupa id
            7. Adaugare n carti noi
            8. Stergere totala
            0. Iesire

        """
        while True:
            print(menu)

            cmd = input("Da o comanda: ")
            if cmd == "1":
                self.show_all_books()
            elif cmd == "2":
                self.add_book()
            elif cmd == "3":
                self.delete_book()
            elif cmd == "4":
                self.modify_book()
            elif cmd == "5":

                for bk in self.__srvBook.sortare():
                    print (bk)
            elif cmd == "6":
                self.cautare_book()
            elif cmd =="7":
                self.n_entitati()
            elif cmd== "8":
                self.delete_all()
            elif cmd == "0":
                break
            else:
                print("\n      Comanda invalida.\n ")

    def show_all_books(self):
        """
            Prints out all books from repository

        """
        bks=self.__srvBook.get_all_books()
        if len(bks)==0:
            print ("\n          Nu exista instante.\n".upper())
        else:

            for bk in bks:
               print (bk)

    def add_book(self):
        while True:
            try:
                id =input("Da id: ")
                title=input("Da titlu: ")
                author=input("Da autor: ")
                desc=input("Da descriere: " )
                bk = self.__srvBook.create_book(id, title,  author, desc)
                break
            except ValidatorException :
              None
            except RepositoryExceptionBook as msg:
                print(msg)


        print ("\n      Cartea  a fost adaugata.\n".upper())


    def delete_book(self):
        if (len(self.__srvBook.get_all_books())>0):
            while True:
                try:
                    id= input("Da un id: ")

                    self.__srvBook.delete_book(id)
                    break
                except ValidatorException as msg:
                    print (msg)
                except RepositoryExceptionBook as msg:
                    print (msg)

            print ("\n      Instanta a fost stearsa.\n".upper())
        else:
            print ("\n          Nu exista instante de sters.  \n".upper())


    def modify_book(self):
        if len(self.__srvBook.get_all_books())>0:
            while True:
                try:
                    id =input("Da id: ")
                    title=input("Da titlu nou : ")
                    author=input("Da autor nou : ")
                    desc=input("Da descriere noua: " )
                    bk = self.__srvBook.modify_book(id, title, desc, author)
                    break
                except ValidatorException :
                    None
                except RepositoryExceptionBook as msg:
                    print (msg)
            print ("\n            Instanta a fost modificata.".upper())

            #self.__srvBook.modify_book(id,title,desc, author)
        else:
            print("\n          Nu exista instante de modificat.  \n".upper())


    def cautare_book(self):
        if len(self.__srvBook.get_all_books()) > 0:
            while True:
                try:
                    id =input("Da id pentru cautare: ")
                    print (self.__srvBook.cautare(id))
                    break
                except ValidatorException as msg:
                    print (msg)

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


        authors = ["Ion Barbu", "George Cosbuc",  "Mihai", "Ana", "Gabriel", "Monica", "Otilia"]
        desc=["Romance", "Thriller", "Realism", "Horror"]
        titles=["Ion", "Enigma Otiliei", "Rosu si Negru", "Oameni si soareci"]
        copie = n
        while n > 0:
            try:
                id = "b"+str(randint(1, 100))
                title = choice(titles)
                description = choice(desc)
                author = choice(authors)
                self.__srvBook.create_book(id, title, description, author)
                n -= 1
            except ValidatorException:
                None
            except RepositoryExceptionBook:
                None

        print("\n      Au fost adaugate ".upper(), copie, "carti. \n".upper())


    def delete_all(self):
        try:
            lung = len(self.__srvBook.get_all_books())
            self.__srvBook.delete_all()
            print ("\n          There were deleted ",lung," books from file \n".upper())

        except ValueError as msg:
            print (msg)




