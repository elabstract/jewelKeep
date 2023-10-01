import unittest
from mobile_app.controllers.store_controller import StoreController
from mobile_app.models.store import Store

class TestStore(unittest.TestCase):

    def setUp(self):
        self.store_controller = StoreController()
        self.store_data = {
            'name': 'Diamonds R Us',
            'location': 'New York',
            'inventory': [
                {'item_name': 'Diamond Ring', 'price': 5000},
                {'item_name': 'Gold Necklace', 'price': 3000}
            ]
        }

    def test_create_store(self):
        store = self.store_controller.createStore(self.store_data)
        self.assertIsInstance(store, Store)
        self.assertEqual(store.name, self.store_data['name'])
        self.assertEqual(store.location, self.store_data['location'])
        self.assertEqual(store.inventory, self.store_data['inventory'])

    def test_update_store(self):
        store = self.store_controller.createStore(self.store_data)
        updated_data = {'name': 'Gems Galore', 'location': 'Los Angeles'}
        updated_store = self.store_controller.updateStore(store.id, updated_data)
        self.assertEqual(updated_store.name, updated_data['name'])
        self.assertEqual(updated_store.location, updated_data['location'])

    def test_delete_store(self):
        store = self.store_controller.createStore(self.store_data)
        self.store_controller.deleteStore(store.id)
        self.assertIsNone(self.store_controller.getStoreById(store.id))

if __name__ == '__main__':
    unittest.main()