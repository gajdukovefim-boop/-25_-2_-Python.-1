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


class Book:
    """Класс, представляющий книгу"""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра книги

        Args:
            id_: идентификатор книги
            name: название книги
            pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает валидное Python-представление для создания копии объекта"""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс, представляющий библиотеку"""

    def __init__(self, books=None):
        """
        Инициализация экземпляра библиотеки

        Args:
            books: список книг (по умолчанию None - создается пустой список)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для добавления новой книги

        Returns:
            int: следующий доступный id для книги
        """
        if not self.books:  # если список книг пуст
            return 1
        else:
            # возвращаем id последней книги + 1
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её id

        Args:
            book_id: идентификатор книги

        Returns:
            int: индекс книги в списке

        Raises:
            ValueError: если книга с указанным id не найдена
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        # если книга не найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
