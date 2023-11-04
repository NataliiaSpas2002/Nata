import os
import unittest
import json
from phonebook2 import new_data, search_by_name, update, delete


class TestPhonebook(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        self.temp_file_path = os.path.join(current_dir, 'test_phonebook2.py.json')
        with open(self.temp_file_path, 'w') as temp_file:
            json.dump({}, temp_file)

    def tearDown(self):
        os.remove(self.temp_file_path)

    def test_new_data(self):
        new_data('+phonenumber', 'name', 'city', 'address')
        with open(self.temp_file_path, 'r') as temp_file:
            phonebook_data = json.load(temp_file)
            self.assertEqual(len(phonebook_data), 1)
    def test_new_data2(self):
        new_data('phonenumber', 'name', 'city', 'address')
        with open(self.temp_file_path, 'r') as temp_file:
            phonebook_data = json.load(temp_file)
            self.assertEqual(len(phonebook_data), 0)
    def test_search_by_name(self):
        new_data("+380936752692","Spasenko Mikhailo", "Kyiv", "Ushakova Mukolu 6")
        new_data("+380996636752","Spasenko Mikhailo", "Kyiv", "Ushakova Mukolu 6")
        result = search_by_name("Spasenko Mikhailo")
        self.assertEqual(result, ['+380936752692', '+380996636752'])

    def test_update(self):
        new_data("+380936752692","Spasenko Mikhailo", "Kyiv", "Ushakova Mukolu 6")
        update('+380936752692', 'Vovk Olena', 'Izum', 'Kvitucha sq.')
        with open(self.temp_file_path, 'r') as temp_file:
            phonebook_data = json.load(temp_file)
            self.assertEqual(phonebook_data['+380936752692']['name'], 'Vovk Olena')
            self.assertEqual(phonebook_data['+380936752692']['city'], 'Izum')
            self.assertEqual(phonebook_data['+380936752692']['address'], 'Kvitucha sq.')
    def test_delete(self):
        new_data('+380936752693', 'Vovk Olena', 'Izum', 'Kvitucha sq.')
        delete('+380936752693')
        with open(self.temp_file_path, 'r') as temp_file:
            phonebook_data = json.load(temp_file)
            self.assertEqual(len(phonebook_data), 0)

if __name__ == '__main__':
    unittest.main()
