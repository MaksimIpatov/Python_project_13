

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
        """Метод добавления  продукта"""
        if isinstance(new_product, Category):
            self.products.append(new_product)
        else:
            print("Добавление объектов из других классов запрещено, только из Category")


    @property
    def products(self):
        return_products = []
        for i in self.__products:
            product = f'{i.title}, {i.price} руб. Остаток: {i.quantity_in_stock} шт.'
            return_products.append(product)
        return return_products

    def __str__(self):
        return f"{self.__products}, 'количество продуктов:' {self.quantity_in_stock} 'шт.'"

