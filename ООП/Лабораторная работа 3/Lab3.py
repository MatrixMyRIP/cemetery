class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self):
        return self._name

    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError(f'Переменная pages должна быть типа int, а ввели тип {type(pages)}')
        if pages > 0:
            self.pages = pages
        else:
            raise ValueError(f'Количество страниц должно быть положительным и больше нуля')

    def __str__(self):
        return super().__str__() + f". Количество страниц: {self.pages} стр."
        # return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return super().__repr__()[:-1] + f", pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, int):
            raise TypeError(f'Переменная duration должна быть типа float, а ввели тип {type(duration)}')
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError(f'Длительность должна быть положительной и больше нуля')

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
    book.name = "Поэмы"
    book.author = "Лермонтов"
    print(book)
