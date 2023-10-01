```python
from mobile_app.database import db_session
from mobile_app.models.store import Store, StoreSchema

store_schema = StoreSchema()

def create_store(store_data):
    new_store = Store(**store_data)
    db_session.add(new_store)
    db_session.commit()
    return store_schema.dump(new_store)

def get_all_stores():
    stores = Store.query.all()
    return store_schema.dump(stores, many=True)

def get_store_by_id(store_id):
    store = Store.query.get(store_id)
    return store_schema.dump(store)

def update_store(store_id, store_data):
    store = Store.query.get(store_id)
    for key, value in store_data.items():
        setattr(store, key, value)
    db_session.commit()
    return store_schema.dump(store)

def delete_store(store_id):
    store = Store.query.get(store_id)
    db_session.delete(store)
    db_session.commit()
    return {'message': 'Store deleted successfully'}
```