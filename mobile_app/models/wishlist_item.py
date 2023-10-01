```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class WishlistItem(Base):
    __tablename__ = 'wishlist_items'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    store_id = Column(Integer, ForeignKey('stores.id'))
    item_name = Column(String)
    item_description = Column(String)
    item_price = Column(String)

    user = relationship("User", back_populates="wishlist_items")
    store = relationship("Store", back_populates="wishlist_items")
```