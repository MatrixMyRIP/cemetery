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
        self.id_ = id_

    # def __str__(self):
    #     return f"Книга: {self.name}; Количество страниц: '{self.pages}'; ID: '{self.id_}'"
    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})"




if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
