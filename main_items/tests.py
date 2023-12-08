from django.test import TestCase
from .models import Item


# Create your tests here.
class ItemModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        count = Item.objects.count()
        print(f"{message}: #all_items={count}")

    def setUp(self):
        print('-' * 20 + '\n')
        self.print_info('Start setUp')
        self.item = Item.objects.create(name='Test item', description='AAA', price=2000)
        Item.objects.create(name='Second item', description='next add', price=99)
        Item.objects.create(name='Four', description='Four is four', price=0)
        self.print_info('Finish setUp')

    def test_item_creation(self):
        # Проверка создания объекта
        self.print_info('Start test_creation')
        self.assertEqual(self.item.name, 'Test item')
        self.assertEqual(self.item.description, 'AAA')
        self.assertEqual(self.item.price, 2000)
        self.print_info('Finish test_creation')

    def test_get_all_records(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_get_all_records')
        items = Item.objects.all()
        self.assertEqual(len(items), 3)
        self.print_info('Finish test_get_all_records')

    def test_item_get_record(self):
        # Проверка получения записи из бд
        self.print_info('Start test_get_record')
        four = Item.objects.get(name='Four')
        self.assertEqual(four.price, 0)
        self.print_info('Finish test_get_record')

    def test_item_str(self):
        # Проверка метода __str__()
        self.print_info('Start test_str')
        expected_str = 'Test item AAA 2000'
        self.assertEqual(str(self.item), expected_str)
        self.print_info('Finish test_movie_str')
