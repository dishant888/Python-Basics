# Book Mgt (add, lend, return books)

class Lib:

    def __init__(self,books):
        self.books = books
        self.lendRecords = {}

    def add(self):
        self.books.append(input('Enter name of book: '))
        print('Book added successfully!')

    def list(self):
        for i in self.books:
            print(i)

    def lend(self):
        book = input('Enter name of Book: ')
        if book not in self.books:
            print('Book is not in the list')
        elif book in self.lendRecords:
            print('This Book is already issued to ',self.lendRecords.get(book))
        else:
            user = input('Enter name of the user: ')
            self.lendRecords[book] = user
            print('Book Issued!')

    def ret(self):
        book = input('Enter name of Book: ')
        if book not in self.books:
            print('Book is not in the list')
        elif book in self.lendRecords:
            self.lendRecords.pop(book)
            print('Booked Returned!')
        else:
            print('This book is not issued to anyone')

    def issueList(self):
        for book,user in self.lendRecords.items():
            print(book,' book is issued to ',user)


obj = Lib(['Python','C++','DS','DBMS'])

while True:
    print('Welcome to Library')
    print('1. Add Book')
    print('2. List Books')
    print('3. Lend Book')
    print('4. Return Book')
    print('5. Issue List')
    print('6. Exit')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        obj.add()
    elif choice == 2:
        obj.list()
    elif choice == 3:
        obj.lend()
    elif choice == 4:
        obj.ret()
    elif choice == 5:
        obj.issueList()
    elif choice == 6:
        exit()
    else:
        print('Invalid')