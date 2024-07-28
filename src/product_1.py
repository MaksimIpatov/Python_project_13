
from abc import ABC, abstractmethod
class AbstractProduct(ABC):
    @abstractmethod
    def create_product(self, title, description, price, quantity_in_stock, colour):
        pass

class ReprMixin():
    """Миксин для вывода информации о создании объекта"""
    def __init__(self, *args, **kwargs):
        print(self)
    def __repr__(self):
        attrs = ', '.join(f"{attr}: {value}" for attr, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class Product(ReprMixin, AbstractProduct):
    """Класс продукты обладает свойствами название, описание, цена, количество в наличии"""
    title: str
    description: str
    price: float
    quantity_in_stock: int
    colour: str

    def __init__(self, title, description, price, quantity_in_stock, colour):
        """Инициализация экземпляров класса Product"""
        self.title = title
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock
        self.colour = colour
        super().__init__(title, description, price, quantity_in_stock, colour)

    @classmethod
    def create_product(cls, title, description, price, quantity_in_stock, colour):
        return cls(title, description, price, quantity_in_stock, colour)

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price
    @price.setter
    def price(self, value):
        """Сеттер для проверки цены"""
        price = value
        if price <= 0:
            print('Цена введена некорректная')
        else:
            self.__price = price

    def __str__(self):
        return f"{self.title}, {self.__price} 'руб.' 'Остаток:' {self.quantity_in_stock} 'шт.'"

    def __add__(self, other):
        if self.__class__ != other.__class__:
            raise TypeError("Сложение экземпляров разных  классов запрещено")
        return self.price * self.quantity_in_stock + other.price * other.quantity_in_stock


class Smartphone(Product):
    def __init__(self, title, description, price, quantity_in_stock, colour, efficiency,  model, amount_memory):
        super().__init__(title, description, price, quantity_in_stock, colour)
        self.efficiency = efficiency
        self.model = model
        self.amount_memory = amount_memory


class Lawn_grass(Product):
    def __init__(self, title, description, price, quantity_in_stock, colour, country_origin, germination_period):
        super().__init__(title, description, price, quantity_in_stock, colour)
        self.country_origin = country_origin
        self.germination_period = germination_period


"""Проверка вывода в консоль сообщения"""
product = Product.create_product('Продукт1', 'Описание продукта', 1200, 10, 'red')
print(product)



if __name__ == "__main__":
    phone = Smartphone("iPhone", "Latest model", 999.99, 5, "Black", "High", "13 Pro", 128)
    grass = Lawn_grass("GreenMix", "Lawn grass seed", 19.99, 100, "Green", "USA", 7)









