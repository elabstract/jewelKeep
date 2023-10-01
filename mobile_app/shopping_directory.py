```python
from flask import Blueprint, render_template, request
from .services.store_service import get_all_stores, get_store_by_id

shopping_directory_bp = Blueprint('shopping_directory', __name__)

@store_data.route('/')
def store_directory():
    stores = get_all_stores()
    return render_template('store_directory.html', stores=stores)

@store_data.route('/<int:store_id>')
def store_detail(store_id):
    store = get_store_by_id(store_id)
    return render_template('store_detail.html', store=store)
```