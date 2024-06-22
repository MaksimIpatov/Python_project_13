class Product:
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

    @classmethod
    def create_product(cls, prod_dict):
        return cls(**prod_dict)

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
        if not isinstance(other, Product):
            raise ValueError('Складывать можно объекты Product или дочерние')
        return f"{self.__price*self.quantity_in_stock + other.__price*other.quantity_in_stock}"


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















