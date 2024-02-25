# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
#
# 2) Book - name, year, author (author must be an instance of Author class)
#
# 3) Author - name, country, birthday, books = []
#
# Library class
#
# Methods:
#
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class
# and adds the book to the books list for the current library.
#
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
#
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#
# All 3 classes must have a readable __repr__ and __str__ methods.
#
# Also, the book class should have a class variable which holds the amount of all existing books

class Author:
    def __init__(self, author_name: str, author_birth: str, author_country: str):
        self.author_name = author_name
        self.author_birth = author_birth
        self.author_country = author_country
        self.author_books = []

    def author_books_info(self):
        books_info = f""
        if self.author_books:
            books_info += f"\nКниги автора:\n"
            for book in self.author_books:
                books_info += f"{book.book_name} - {book.book_year}р.\n"
        else:
            books_info += f"Ще немає даних про написані книги.\n"
        return books_info

    def __str__(self):
        books_info = self.author_books_info()
        author_info = (f"Ім'я автора: {self.author_name}.\n"
                       f"Дата народження: {self.author_birth}.\n"
                       f"Країна автора: {self.author_country}.\n")
        return author_info + books_info


class Book:
    def __init__(self, book_name: str, book_year: int, author: Author):
        self.book_name = book_name
        self.book_year = book_year
        self.book_author = author
        self.book_author.author_books.append(self)

    def __eq__(self, other):
        return (self.book_author.author_name == other.book_author.author_name) \
            and (self.book_author.author_country == other.book_author.author_country) \
            and (self.book_author.author_birth == other.book_author.author_birth) \
            and (self.book_name == other.book_name)

    def __str__(self):
        return (f"Назва книги: {self.book_name}\n"
                f"Рік випуску: {self.book_year}\n"
                f"Автор: {self.book_author.author_name}")


class Library:
    __common_books_amount = 0

    def __init__(self, library_name):
        self.library_name = library_name
        self.library_books = []
        self.library_authors = set()

    def add_book(self, *books):
        for book in books:
            if book not in self.library_books and isinstance(book, Book):
                self.library_authors.add(book.book_author.author_name)
                self.library_books.append(book)
                self.__common_books_amount += 1

    # Сортую книги автора по його імені
    def sort_by_author(self, authors_name: str) -> str:
        if authors_name not in self.library_authors:
            return f"{authors_name} відсутній у бібліотечному каталозі!\n"
        # Отримую список книг по імені автора і сортую його за назвою книг
        result = [book for book in self.library_books if book.book_author.author_name == authors_name]
        result.sort(key=lambda book: book.book_name)
        sorted_books = (f"Результат вашого пошуку:\n"
                        f"Автор: {authors_name}\n")
        for book in result:
            sorted_books += f"Назва: {book.book_name} - {book.book_year}р.\n"
        return sorted_books

    # Сортую книги по року видання
    def sort_by_year(self, user_book_year: int):
        books_by_year = [book for book in self.library_books if book.book_year == user_book_year]
        if books_by_year:
            sorted_books = f"Результати пошуку по {user_book_year} року:\n"
            for book in books_by_year:
                sorted_books += (f"Рік видання: {book.book_year}р. - Назва: {book.book_name} - "
                                 f"Автор: {book.book_author.author_name}\n")
            return sorted_books
        else:
            return f"{user_book_year} рік був ненадихаючим, або в нас відсутня інформація про видання(."

    def __str__(self):
        return (f"{self.library_name} рада вітати тебе, читаче!\n"
                f"В нашій колеції ви знайдете понад {self.__common_books_amount} книг\n"
                f"більше ніж {len(self.library_authors)} авторів.\n"
                f"Гарної подорожі в світ яскравих пригод і бурхливих почуттів!\n")


if __name__ == "__main__":

    # Створюю екземпляри класу Author
    a_1 = Author("Lincoln Child", "13-10-1957", "USA")
    a_2 = Author("James Rollings", "20-08-1961", "USA")
    a_3 = Author("Rider Haggard", "22-06-1856", "England")

    # Створюю екземпляри класу Book
    b_1 = Book("The Cabinet of Curiosities", 2002, a_1)
    b_2 = Book("Brimstone", 2004, a_1)
    b_3 = Book("White Fire", 2013, a_1)
    b_10 = Book("Cold Ireland", 2004, a_1)

    b_4 = Book("The Starless Crown", 2021, a_2)
    b_5 = Book("Kingdom of Bones", 2004, a_2)

    b_6 = Book("Ayesha", 1905, a_3)
    b_7 = Book("Wisdom`s daughter", 1923, a_3)

    # Створюю Бібліотеку, через яку будуть відбуватися всі операції з книгами
    l_1 = Library("New Town Library")
    l_1.add_book(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_10)

    print(l_1)
    print(a_1)
    print(l_1.sort_by_author("Lincoln Child"))
    print(l_1.sort_by_year(2004))
