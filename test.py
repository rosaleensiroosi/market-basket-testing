import unittest
from product import Product
from basket import ShoppingBasket


class TestProduct(unittest.TestCase):
    def setUp(self) -> None:
        self.product = Product('milk', 3.0)
        
    
    def test_get_product_name(self):
        self.assertEqual(self.product.name, 'milk')
        
    def test_get_product_price(self):
        self.assertEqual(self.product.price, 3.0)
        
    def test_repr_method(self):
        self.assertEqual(
            repr(self.product),
            "Product(name='milk', price=3.0, quantity=1)",
            "Product's __repr__ method did not return expected result"
        )

class TestBasketWithNoProducts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()
        
    def test_size_of_basket_should_be_empty(self):
        self.assertEqual(len(self.basket), 0)
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(0)
 
    def test_total_amount_should_be_zero(self):
        self.assertEqual(self.basket.total(), 0.0)
        
class TestBasketWithOneProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product("milk", 3.0)
        
    def test_size_of_basket_should_be_one(self):
        self.assertEqual(len(self.basket), 1)
        
    def test_total_amount_should_have_tax(self):
        self.assertEqual(self.basket.total(), 3.63)
        
    def test_getting_product(self):
        self.assertEqual(self.basket.get_product(0).name, "milk")
 
    def test_getting_product_out_of_range_should_raise_error(self):
        with self.assertRaises(IndexError):
            self.basket.get_product(1)

if __name__ == '__main__':
    unittest.main()