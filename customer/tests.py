from django.test import TestCase
from .models import MenuItem, Category, OrderModel

class MenuItemModelTestCase(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            name='Test Item',
            description='Test description',
            image='menu_images/test_image.jpg',
            price=10.99
        )
        self.category = Category.objects.create(name='Test Category')

    def test_menu_item_creation(self):
        """Test the creation of a MenuItem instance"""
        self.assertEqual(self.menu_item.name, 'Test Item')
        self.assertEqual(self.menu_item.description, 'Test description')
        self.assertEqual(self.menu_item.price, 10.99)
        self.assertEqual(self.menu_item.category.count(), 0)

    def test_category_association(self):
        """Test associating a MenuItem with a Category"""
        self.menu_item.category.add(self.category)
        self.assertEqual(self.menu_item.category.count(), 1)
        self.assertEqual(self.menu_item.category.first(), self.category)

class OrderModelTestCase(TestCase):
    def setUp(self):
        self.order = OrderModel.objects.create(
            price=25.50,
            name='Test Order',
            email='test@example.com',
            street='123 Test St',
            city='Test City',
            state='Test State',
            zip_code=12345
        )
        self.menu_item1 = MenuItem.objects.create(
            name='Item 1',
            description='Description 1',
            image='menu_images/item1.jpg',
            price=10.00
        )
        self.menu_item2 = MenuItem.objects.create(
            name='Item 2',
            description='Description 2',
            image='menu_images/item2.jpg',
            price=15.50
        )

    def test_order_creation(self):
        """Test the creation of an OrderModel instance"""
        self.assertEqual(self.order.price, 25.50)
        self.assertEqual(self.order.name, 'Test Order')
        self.assertEqual(self.order.email, 'test@example.com')
        self.assertEqual(self.order.street, '123 Test St')
        self.assertEqual(self.order.city, 'Test City')
        self.assertEqual(self.order.state, 'Test State')
        self.assertEqual(self.order.zip_code, 12345)
        self.assertEqual(self.order.items.count(), 0)

    def test_order_item_association(self):
        """Test associating MenuItem(s) with an OrderModel"""
        self.order.items.add(self.menu_item1, self.menu_item2)
        self.assertEqual(self.order.items.count(), 2)
        self.assertIn(self.menu_item1, self.order.items.all())
        self.assertIn(self.menu_item2, self.order.items.all())