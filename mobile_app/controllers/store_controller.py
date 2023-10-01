```python
from mobile_app.services.store_service import StoreService
from mobile_app.models.store import StoreSchema

class StoreController:
    def __init__(self):
        self.store_service = StoreService()
        self.store_schema = StoreSchema()

    def create_store(self, store_data):
        validated_data = self.store_schema.load(store_data)
        new_store = self.store_service.create_store(validated_data)
        return new_store

    def update_store(self, store_id, store_data):
        validated_data = self.store_schema.load(store_data)
        updated_store = self.store_service.update_store(store_id, validated_data)
        return updated_store

    def delete_store(self, store_id):
        deleted_store = self.store_service.delete_store(store_id)
        return deleted_store

    def get_store(self, store_id):
        store = self.store_service.get_store(store_id)
        return store

    def get_all_stores(self):
        stores = self.store_service.get_all_stores()
        return stores
```