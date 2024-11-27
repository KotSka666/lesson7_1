
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        cur_products = self.get_products()
        new_entries = []
        for product in products:
            if str(product) not in cur_products:
                new_entries.append(str(product))
            else:
                print(f"Продукт {product.name} уже есть в магазине")
        if new_entries:
            with open(self.file_name, 'a') as file:
                for entry in new_entries:
                    file.write(entry + '\n')
            file.close()

# Пример использования

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str
s1.add(p1, p2, p3)
print(s1.get_products())
