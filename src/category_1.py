from src.product_1 import Product


class Category:
    """Класс категория обладает свойствами название, описание и списком товары"""
    title: str
    description: str
    products: []
    number_categories: int
    unique_products: int

    number_categories = 0
    unique_products = 0


    def __init__(self, title, description, products):
        """Инициализация экземпляров класса Category"""
        self.title = title
        self.description = description
        self.__products = products
        Category.number_categories += 1
        Category.unique_products += len(products)


    def add_product(self, new_product):
        """Метод добавления  продукта, при попытке добавить товар с остатком ноль завершение метода!!!!"""
        if isinstance(new_product, Product):
            if new_product.quantity_in_stock == 0:
                raise ValueError("Товар с количеством ноль нельзя быть добавить!!!!")
            self.__products.append(new_product)
        raise TypeError("Добавление экземпляров класса запрещено!!!!!")


    def get_average_price(self):
        """Метод подсчета средней цены товаров или 0 если количество товаров ноль!!!"""
        try:
            sum_price = sum([product.price for product in self.products])
            average_price = sum_price / len(self.products)
            return average_price
        except ZeroDivisionError:
            return 0


    @property
    def products(self):
        return_products = []
        for i in self.__products:
            product = f'{i.title}, {i.price} руб. Остаток: {i.quantity_in_stock} шт.'
            return_products.append(product)
        return return_products

    def __str__(self):
        return f"{self.__products}, 'количество продуктов:' {self.quantity_in_stock} 'шт.'"




