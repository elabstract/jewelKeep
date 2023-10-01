import unittest
from mobile_app.models.wishlist_item import WishlistItem
from mobile_app.services.wishlist_service import WishlistService

class TestWishlist(unittest.TestCase):

    def setUp(self):
        self.wishlist_service = WishlistService()
        self.wishlist_item = WishlistItem('Diamond Ring', 'A beautiful diamond ring', 'Jewelry Store A')

    def test_create_wishlist_item(self):
        result = self.wishlist_service.createWishlistItem(self.wishlist_item)
        self.assertEqual(result, True)

    def test_update_wishlist_item(self):
        self.wishlist_item.description = 'A beautiful diamond ring with a gold band'
        result = self.wishlist_service.updateWishlistItem(self.wishlist_item)
        self.assertEqual(result, True)

    def test_delete_wishlist_item(self):
        result = self.wishlist_service.deleteWishlistItem(self.wishlist_item)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()