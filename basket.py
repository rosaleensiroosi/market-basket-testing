from product import Product


class ShoppingBasket:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def __len__(self) -> int:
        return sum([product.quantity for product in self.products])

    def add_product(self, name: str, price: float) -> "ShoppingBasket":
        for product in self.products:
            if product.name == name:
                product.quantity += 1
                return self
        self.products.append(Product(name, price))
        return self

    def get_product(self, index: int) -> Product:
        return self.products[index]

    def total(self, tax: float = 21.0) -> float:
        net_value = sum([product.price * product.quantity for product in self.products])
        return round(net_value * (1 + tax / 100), 2)
