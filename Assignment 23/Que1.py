class BookStore:
    NoOfBooks = 0

    def __init__(self,name,author):
        self.Name = name
        self.Author = author

        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}.\nNo of Books : {BookStore.NoOfBooks}")

obj1 = BookStore("C Programming","Dennis Ritchie")
obj1.Display()

obj1 = BookStore("Linux System Programming","Robert Love")
obj1.Display()