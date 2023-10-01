import unittest
from mobile_app.models.user import User
from mobile_app.services.user_service import UserService
from mobile_app.database import Database

class TestUser(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.user_service = UserService(self.db)
        self.user_data = {
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password': 'test_password'
        }

    def test_create_user(self):
        user = self.user_service.create_user(self.user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])

    def test_update_user(self):
        user = self.user_service.create_user(self.user_data)
        updated_data = {
            'username': 'updated_user',
            'email': 'updated_user@example.com',
            'password': 'updated_password'
        }
        updated_user = self.user_service.update_user(user.id, updated_data)
        self.assertEqual(updated_user.username, updated_data['username'])
        self.assertEqual(updated_user.email, updated_data['email'])

    def test_delete_user(self):
        user = self.user_service.create_user(self.user_data)
        self.user_service.delete_user(user.id)
        deleted_user = self.user_service.get_user_by_id(user.id)
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()