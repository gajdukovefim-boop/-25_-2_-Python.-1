from abc import ABC
from typing import Optional


class Book(ABC):
    """
    Класс, описывающий книгу.

    Атрибуты:
        title (str): Название книги
        author (str): Автор книги
        pages (int): Количество страниц

    Исключения:
        ValueError: Если название или автор пустые, или количество страниц <= 0
    """

    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Инициализация объекта книги.

        Args:
            title: Название книги (не может быть пустым)
            author: Автор книги (не может быть пустым)
            pages: Количество страниц (должно быть > 0)

        Raises:
            ValueError: Если нарушены ограничения на аргументы

        Examples:
            >>> book = Book("Преступление и наказание", "Ф.М. Достоевский", 671)
            >>> book.title
            'Преступление и наказание'
            >>> book.pages
            671
        """
        if not title or not isinstance(title, str):
            raise ValueError("Название книги не может быть пустым")
        if not author or not isinstance(author, str):
            raise ValueError("Автор книги не может быть пустым")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read_page(self, page_number: int) -> str:
        """
        Прочитать указанную страницу книги.

        Args:
            page_number: Номер страницы для чтения (должен быть в диапазоне 1..pages)

        Returns:
            Содержимое страницы в виде строки

        Raises:
            ValueError: Если номер страницы вне допустимого диапазона

        Examples:
            >>> book = Book("1984", "Дж. Оруэлл", 328)
            >>> book.read_page(50)  # doctest: +SKIP
            'Содержимое страницы 50'
        """
        if not 1 <= page_number <= self.pages:
            raise ValueError(f"Номер страницы должен быть от 1 до {self.pages}")
        ...

    def get_reading_time(self, reading_speed: int) -> float:
        """
        Рассчитать примерное время чтения книги.

        Args:
            reading_speed: Скорость чтения в страницах в час (должна быть > 0)

        Returns:
            Примерное время чтения в часах

        Raises:
            ValueError: Если скорость чтения <= 0

        Examples:
            >>> book = Book("Мастер и Маргарита", "М. Булгаков", 480)
            >>> book.get_reading_time(20)  # doctest: +SKIP
            24.0
        """
        if reading_speed <= 0:
            raise ValueError("Скорость чтения должна быть положительной")
        ...


class Smartphone(ABC):
    """
    Класс, описывающий смартфон.

    Атрибуты:
        brand (str): Бренд смартфона
        battery_capacity (int): Емкость аккумулятора в mAh
        storage_gb (int): Объем памяти в гигабайтах
    """

    def __init__(self, brand: str, battery_capacity: int, storage_gb: int) -> None:
        """
        Инициализация объекта смартфона.

        Args:
            brand: Бренд смартфона (не может быть пустым)
            battery_capacity: Емкость аккумулятора в mAh (должна быть > 0)
            storage_gb: Объем памяти в GB (должен быть > 0)

        Raises:
            ValueError: Если нарушены ограничения на аргументы

        Examples:
            >>> phone = Smartphone("Apple", 3200, 128)
            >>> phone.brand
            'Apple'
            >>> phone.storage_gb
            128
        """
        if not brand or not isinstance(brand, str):
            raise ValueError("Бренд не может быть пустым")
        if not isinstance(battery_capacity, int) or battery_capacity <= 0:
            raise ValueError("Емкость аккумулятора должна быть положительным целым числом")
        if not isinstance(storage_gb, int) or storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным целым числом")

        self.brand = brand
        self.battery_capacity = battery_capacity
        self.storage_gb = storage_gb

    def make_call(self, phone_number: str) -> bool:
        """
        Совершить телефонный звонок.

        Args:
            phone_number: Номер телефона в международном формате (должен начинаться с '+')

        Returns:
            True если звонок успешно совершен, False в случае ошибки

        Raises:
            ValueError: Если номер телефона имеет неверный формат

        Examples:
            >>> phone = Smartphone("Samsung", 4000, 256)
            >>> phone.make_call("+79161234567")  # doctest: +SKIP
            True
        """
        if not phone_number.startswith('+'):
            raise ValueError("Номер телефона должен начинаться с '+'")
        ...

    def check_storage_space(self) -> float:
        """
        Проверить оставшееся свободное место.

        Returns:
            Процент свободного места от общего объема (от 0.0 до 100.0)

        Examples:
            >>> phone = Smartphone("Xiaomi", 4500, 64)
            >>> phone.check_storage_space()  # doctest: +SKIP
            45.5
        """
        ...


class BankAccount(ABC):
    """
    Класс, описывающий банковский счет.

    Атрибуты:
        account_number (str): Номер счета
        owner_name (str): Имя владельца счета
        balance (float): Текущий баланс счета
    """

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0) -> None:
        """
        Инициализация объекта банковского счета.

        Args:
            account_number: Номер счета (20 цифр)
            owner_name: Имя владельца счета (не может быть пустым)
            initial_balance: Начальный баланс (не может быть отрицательным)

        Raises:
            ValueError: Если нарушены ограничения на аргументы

        Examples:
            >>> account = BankAccount("12345678901234567890", "Иван Иванов", 1000.0)
            >>> account.owner_name
            'Иван Иванов'
            >>> account.balance
            1000.0
        """
        if not account_number.isdigit() or len(account_number) != 20:
            raise ValueError("Номер счета должен состоять из 20 цифр")
        if not owner_name or not isinstance(owner_name, str):
            raise ValueError("Имя владельца не может быть пустым")
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = float(initial_balance)

    def deposit(self, amount: float) -> float:
        """
        Внести средства на счет.

        Args:
            amount: Сумма для внесения (должна быть > 0)

        Returns:
            Новый баланс счета

        Raises:
            ValueError: Если сумма для внесения <= 0

        Examples:
            >>> account = BankAccount("09876543210987654321", "Петр Петров")
            >>> account.deposit(500.0)  # doctest: +SKIP
            500.0
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")
        ...

    def withdraw(self, amount: float) -> Optional[float]:
        """
        Снять средства со счета.

        Args:
            amount: Сумма для снятия (должна быть > 0 и не превышать баланс)

        Returns:
            Новый баланс счета или None если операция не удалась

        Raises:
            ValueError: Если сумма для снятия <= 0 или превышает баланс

        Examples:
            >>> account = BankAccount("11223344556677889900", "Сергей Сергеев", 2000.0)
            >>> account.withdraw(300.0)  # doctest: +SKIP
            1700.0
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
