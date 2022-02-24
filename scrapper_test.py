import json
import unittest

from flask import make_response, jsonify
from scrapper import app, di

app.testing = True

mockObject = {'title': ['A Light in the Attic', 'Tipping the Velvet', 'Soumission', 'Sharp Objects', 'Sapiens: A Brief History of Humankind', 'The Requiem Red', 'The Dirty Little Secrets of Getting Your Dream Job', 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 'The Black Maria', 'Starving Hearts (Triangular Trade Trilogy, #1)', "Shakespeare's Sonnets", 'Set Me Free', "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'Rip it Up and Start Again', 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'Olio', 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'Libertarianism for Beginners', "It's Only the Himalayas"], 'price': [
    '51.77', '53.74', '50.10', '47.82', '54.23', '22.65', '33.34', '17.93', '22.60', '52.15', '13.99', '20.66', '17.46', '52.29', '35.02', '57.25', '23.88', '37.59', '51.33', '45.17'], 'note': ['Three', 'One', 'One', 'Four', 'Five', 'One', 'Four', 'Three', 'Four', 'One', 'Two', 'Four', 'Five', 'Five', 'Five', 'Three', 'One', 'One', 'Two', 'Two'], 'stock': ['In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock', 'In stock']}


# use of false value to show that api call verification works


class TestApi(unittest.TestCase):

    def setUp(self):
        pass

    def test_data_scrapper(self):
        self.assertEqual(di, mockObject)

    def test_get_api(self):
        with app.test_client() as client:
            result = client.get(
                '/list',
            )
            # Check the status of the call if it is a 200
            self.assertEqual(result.status_code, 200)

    def test_post_api(self):
        result = app.test_client().post(
            '/add', json={'note': 'huit', 'price': '42.80', 'stock': 'inStock', 'title': 'Max'})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.dumps(result.json), '{"success": true}')

    def test_put_api(self):
        result = app.test_client().put(
            '/update', json={'note': 'huit', 'price': '42.80', 'stock': 'inStock', 'title': 'Maxime'})

        self.assertEqual(result.data, b'{"success":true}\n')
        self.assertEqual(result.status_code, 200)

    def test_delete_api(self):
        result = app.test_client().delete(
            '/delete', json={'note': 'huit', 'price': '42.80', 'stock': 'inStock', 'title': 'Maxime'})

        self.assertEqual(result.data, b'{"success":true}\n')


if __name__ == '__main__':
    unittest.main()

