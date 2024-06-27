from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:     # TODO написать класс Book
    def __init__(self, name: str, pages: int, id_: int):
        if not isinstance(name, str):
            raise TypeError(f'Переменная name должна быть типа str, а ввели тип {type(name)}')
        self.name = name

        if not isinstance(pages, int):
            raise TypeError(f'Переменная pages должна быть типа int, а ввели тип {type(pages)}')
        self.pages = pages

        if not isinstance(id_, int):
            raise TypeError(f'Переменная id_ должна быть типа int, а ввели тип {type(id_)}')
        self.id = id_

    def __str__(self):
        return f'Книга {self.name!r}'

    def __repr__(self):
        return f"{self.__class__.__name__}(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})"




class Library:      # TODO написать класс Library
    def __init__(self, books: list[Book] = None):
        if books is None:
            self.books = []
        elif not isinstance(books, list):
            raise TypeError(f'Переменная books должна быть типа list, а ввели тип {type(books)}')
        else:
            self.books = books

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            # return self.books[-1].id_ + 1
            return max(self.books, key=lambda book: book.id).id + 1

    def get_index_by_book_id(self, id_):
        if self.books:
            for i in range(len(self.books)):
                if id_ == self.books[i].id:
                    return i
        raise ValueError(f"Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
