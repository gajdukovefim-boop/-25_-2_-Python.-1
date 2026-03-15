from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, Union
from decimal import Decimal


class BankAccount(ABC):
    """
    Базовый класс для всех типов банковских счетов.

    Атрибуты:
        _account_number (str): Уникальный номер счета (непубличный для защиты от изменений)
        _owner (str): Владелец счета
        _balance (Decimal): Текущий баланс (непубличный для контроля через методы)
        _created_at (datetime): Дата создания счета
    """

    def __init__(self, account_number: str, owner: str, initial_balance: Union[float, Decimal] = 0) -> None:
        """
        Конструктор базового класса банковского счета.

        Args:
            account_number: Уникальный номер счета
            owner: ФИО владельца
            initial_balance: Начальный баланс (по умолчанию 0)
        """
        self._account_number = account_number
        self._owner = owner
        self._balance = Decimal(str(initial_balance))  # Конвертация для точности
        self._created_at = datetime.now()

    def __str__(self) -> str:
        """Пользовательское строковое представление счета."""
        return f"Счет №{self._account_number} (Владелец: {self._owner}, Баланс: {self._balance:.2f})"

    def __repr__(self) -> str:
        """Техническое строковое представление для отладки."""
        return f"{self.__class__.__name__}(account_number='{self._account_number}', owner='{self._owner}', balance={self._balance})"

    @abstractmethod
    def withdraw(self, amount: Union[float, Decimal]) -> bool:
        """
        Абстрактный метод для снятия средств.

        Args:
            amount: Сумма для снятия

        Returns:
            True если операция успешна, False в противном случае
        """
        pass

    def deposit(self, amount: Union[float, Decimal]) -> bool:
        """
        Метод для пополнения счета.

        Args:
            amount: Сумма для пополнения

        Returns:
            True если операция успешна, False при неверной сумме
        """
        amount_decimal = Decimal(str(amount))
        if amount_decimal <= 0:
            return False

        self._balance += amount_decimal
        return True

    def get_balance(self) -> Decimal:
        """
        Геттер для получения текущего баланса.

        Returns:
            Текущий баланс счета
        """
        return self._balance


class SavingsAccount(BankAccount):
    """
    Сберегательный счет с процентной ставкой.

    Дополнительные атрибуты:
        _interest_rate (float): Годовая процентная ставка (непубличная для защиты)
        _withdrawal_limit (int): Лимит снятий в месяц (непубличный)
        _withdrawals_this_month (int): Количество снятий в текущем месяце
    """

    def __init__(self, account_number: str, owner: str, initial_balance: Union[float, Decimal] = 0,
                 interest_rate: float = 0.05, withdrawal_limit: int = 3) -> None:
        """
        Расширенный конструктор для сберегательного счета.

        Args:
            account_number: Уникальный номер счета
            owner: ФИО владельца
            initial_balance: Начальный баланс
            interest_rate: Годовая процентная ставка
            withdrawal_limit: Лимит снятий в месяц
        """
        # Вызов конструктора базового класса
        super().__init__(account_number, owner, initial_balance)

        self._interest_rate = interest_rate
        self._withdrawal_limit = withdrawal_limit
        self._withdrawals_this_month = 0
        self._last_withdrawal_month = datetime.now().month

    def __str__(self) -> str:
        """Перегруженный метод с дополнительной информацией о ставке."""
        base_str = super().__str__()
        return f"{base_str} [Сберегательный, ставка {self._interest_rate * 100}%]"

    def __repr__(self) -> str:
        """Перегруженный метод с дополнительными параметрами."""
        return (f"SavingsAccount(account_number='{self._account_number}', owner='{self._owner}', "
                f"balance={self._balance}, interest_rate={self._interest_rate})")

    def withdraw(self, amount: Union[float, Decimal]) -> bool:
        """
        Перегруженный метод снятия с проверкой лимита.

        Причина перегрузки: для сберегательных счетов обычно действуют ограничения
        на количество снятий в месяц. Метод проверяет текущий месяц и лимит снятий.

        Args:
            amount: Сумма для снятия

        Returns:
            True если операция успешна, False при превышении лимита или недостатке средств
        """
        # Проверка месяца для сброса счетчика
        current_month = datetime.now().month
        if current_month != self._last_withdrawal_month:
            self._withdrawals_this_month = 0
            self._last_withdrawal_month = current_month

        # Проверка лимита снятий
        if self._withdrawals_this_month >= self._withdrawal_limit:
            return False

        amount_decimal = Decimal(str(amount))
        if amount_decimal <= 0 or amount_decimal > self._balance:
            return False

        self._balance -= amount_decimal
        self._withdrawals_this_month += 1
        return True

    def apply_interest(self) -> None:
        """Метод для начисления процентов (уникальный для SavingsAccount)."""
        monthly_rate = self._interest_rate / 12
        interest = self._balance * Decimal(str(monthly_rate))
        self._balance += interest


class CheckingAccount(BankAccount):
    """
    Расчетный счет с возможностью овердрафта.

    Дополнительные атрибуты:
        _overdraft_limit (Decimal): Лимит овердрафта (непубличный)
        _monthly_fee (Decimal): Ежемесячная плата за обслуживание
    """

    def __init__(self, account_number: str, owner: str, initial_balance: Union[float, Decimal] = 0,
                 overdraft_limit: Union[float, Decimal] = 1000, monthly_fee: Union[float, Decimal] = 10) -> None:
        """
        Расширенный конструктор для расчетного счета.

        Args:
            account_number: Уникальный номер счета
            owner: ФИО владельца
            initial_balance: Начальный баланс
            overdraft_limit: Лимит овердрафта
            monthly_fee: Ежемесячная плата за обслуживание
        """
        super().__init__(account_number, owner, initial_balance)

        self._overdraft_limit = Decimal(str(overdraft_limit))
        self._monthly_fee = Decimal(str(monthly_fee))

    def __str__(self) -> str:
        """Перегруженный метод с информацией об овердрафте."""
        base_str = super().__str__()
        return f"{base_str} [Расчетный, овердрафт: {self._overdraft_limit}]"

    def __repr__(self) -> str:
        """Перегруженный метод с дополнительными параметрами."""
        return (f"CheckingAccount(account_number='{self._account_number}', owner='{self._owner}', "
                f"balance={self._balance}, overdraft_limit={self._overdraft_limit})")

    def withdraw(self, amount: Union[float, Decimal]) -> bool:
        """
        Перегруженный метод снятия с учетом овердрафта.

        Причина перегрузки: расчетные счета могут допускать отрицательный баланс
        в пределах лимита овердрафта. Метод учитывает эту возможность.

        Args:
            amount: Сумма для снятия

        Returns:
            True если операция успешна (включая использование овердрафта)
        """
        amount_decimal = Decimal(str(amount))
        if amount_decimal <= 0:
            return False

        # Проверка с учетом овердрафта
        max_allowed_withdrawal = self._balance + self._overdraft_limit
        if amount_decimal > max_allowed_withdrawal:
            return False

        self._balance -= amount_decimal
        return True

    def deduct_monthly_fee(self) -> None:
        """Метод для списания ежемесячной платы (уникальный для CheckingAccount)."""
        self._balance -= self._monthly_fee


if __name__ == "__main__":
    # Примеры использования (для демонстрации)

    # Создание сберегательного счета
    savings = SavingsAccount("SA001", "Иван Петров", 1000, interest_rate=0.06)
    print(savings)  # Вызов __str__
    print(repr(savings))  # Вызов __repr__

    # Пополнение счета (унаследованный метод)
    savings.deposit(500)

    # Снятие средств (перегруженный метод)
    savings.withdraw(200)  # Успешно
    savings.withdraw(200)  # Успешно
    savings.withdraw(200)  # Успешно
    savings.withdraw(200)  # Превышен лимит снятий -> False

    # Начисление процентов (уникальный метод)
    savings.apply_interest()

    # Создание расчетного счета
    checking = CheckingAccount("CA001", "Мария Сидорова", 500, overdraft_limit=2000)
    print(checking)

    # Снятие с использованием овердрафта
    checking.withdraw(2000)  # Баланс станет -1500, но в пределах лимита
    print(f"Баланс после овердрафта: {checking.get_balance()}")

    # Списание ежемесячной платы
    checking.deduct_monthly_fee()
