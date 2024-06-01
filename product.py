class Product:
    def __init__(self, name: str, price: float, quantity: int = 1) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
