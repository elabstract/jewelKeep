```python
from mobile_app.models.wishlist_item import WishlistItemSchema
from mobile_app.database import db_session

wishlist_data = []

def createWishlistItem(data):
    new_item = WishlistItemSchema(**data)
    db_session.add(new_item)
    db_session.commit()
    wishlist_data.append(new_item)
    return new_item

def updateWishlistItem(item_id, data):
    item = db_session.query(WishlistItemSchema).filter(WishlistItemSchema.id == item_id).first()
    for key, value in data.items():
        setattr(item, key, value)
    db_session.commit()
    return item

def deleteWishlistItem(item_id):
    item = db_session.query(WishlistItemSchema).filter(WishlistItemSchema.id == item_id).first()
    db_session.delete(item)
    db_session.commit()
    wishlist_data.remove(item)
```