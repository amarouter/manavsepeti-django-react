from django.test import TestCase

from .models import Product

# Create your tests here.


class ProductModelTests(TestCase):
    def test_can_a_product_instance_be_created(self):
        """Controls whether a product instance can be created."""
        # given
        product_name = "Elma"
        # when
        new_product = Product(name="Elma", category="meyve",
                              origin="Amasya", price=8.75, count_in_stock=14)
        # then
        self.assertEqual(new_product.name, product_name)
    def test_can_a_product_be_saved_to_database(self):
        """Controls whether a product can be saved to database."""
        # given
        product_name = "Elma"
        new_product = Product(name="Elma", category="meyve",
                              origin="Amasya", price=8.75, count_in_stock=14)
        new_product.save()
        # when
        new_product_from_db = Product.objects.filter(name=product_name)
        # then
        self.assertEqual(new_product_from_db[0].name, product_name)
