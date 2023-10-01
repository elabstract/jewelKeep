```python
from mobile_app.models.wishlist_item import WishlistItemSchema
from mobile_app.database import db

wishlist_data = []

class Wishlist:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        wishlist_data.append(item)
        db.session.add(item)
        db.session.commit()

    def remove_item(self, item_id):
        item = WishlistItemSchema.query.get(item_id)
        if item in self.items:
            self.items.remove(item)
            wishlist_data.remove(item)
            db.session.delete(item)
            db.session.commit()

    def get_items(self):
        return self.items

    def clear_wishlist(self):
        for item in self.items:
            db.session.delete(item)
        db.session.commit()
        self.items = []
        wishlist_data.clear()
```