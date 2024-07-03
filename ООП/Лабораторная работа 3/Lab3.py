class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError(f'Переменная name должна быть типа str, а ввели тип {type(name)}')
        self.name = name
        if not isinstance(author, str):
            raise TypeError(f'Переменная author должна быть типа str, а ввели тип {type(author)}')
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError(f'Переменная pages должна быть типа int, а ввели тип {type(pages)}')
        self.pages = pages

    def __str__(self):
        return super().__str__() + f". Количество страниц: {self.pages} стр."
        # return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return super().__repr__()[:-1] + f", pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, int):
            raise TypeError(f'Переменная duration должна быть типа float, а ввели тип {type(duration)}')
        self.duration = duration

    def __str__(self):
        return super().__str__() + f". Длительность: {self.duration} минут"
        # return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return super().__repr__()[:-1] + f", duration = {self.duration!r})"


if __name__ == "__main__":
    book = Book("Сказки", "Пушкин")
    print(book)
    print(repr(book))
    book2 = PaperBook("Сказки", "Пушкин", 150)
    print(book2)
    print(repr(book2))
    book3 = AudioBook("Сказки", "Пушкин", 60)
    print(book3)
    print(repr(book3))
