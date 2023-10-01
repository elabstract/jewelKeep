```python
from mobile_app.models.store import StoreSchema
from mobile_app.database import db

class JewelryStore:
    def __init__(self):
        self.store_data = []

    def createStore(self, store_info):
        new_store = StoreSchema().load(store_info)
        self.store_data.append(new_store)
        db.session.add(new_store)
        db.session.commit()
        return new_store

    def updateStore(self, store_id, updated_info):
        store = self.getStoreById(store_id)
        if store:
            for key, value in updated_info.items():
                setattr(store, key, value)
            db.session.commit()
            return store
        return None

    def deleteStore(self, store_id):
        store = self.getStoreById(store_id)
        if store:
            self.store_data.remove(store)
            db.session.delete(store)
            db.session.commit()
            return True
        return False

    def getStoreById(self, store_id):
        for store in self.store_data:
            if store.id == store_id:
                return store
        return None

    def getAllStores(self):
        return self.store_data
```