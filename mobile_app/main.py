```python
from flask import Flask, request, jsonify
from mobile_app.controllers.user_controller import UserController
from mobile_app.controllers.wishlist_controller import WishlistController
from mobile_app.controllers.store_controller import StoreController

app = Flask(__name__)

@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    return UserController.create_user(user_data)

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    return UserController.update_user(user_id, user_data)

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)

@app.route('/wishlist', methods=['POST'])
def create_wishlist_item():
    wishlist_data = request.get_json()
    return WishlistController.create_wishlist_item(wishlist_data)

@app.route('/wishlist/<item_id>', methods=['PUT'])
def update_wishlist_item(item_id):
    wishlist_data = request.get_json()
    return WishlistController.update_wishlist_item(item_id, wishlist_data)

@app.route('/wishlist/<item_id>', methods=['DELETE'])
def delete_wishlist_item(item_id):
    return WishlistController.delete_wishlist_item(item_id)

@app.route('/store', methods=['POST'])
def create_store():
    store_data = request.get_json()
    return StoreController.create_store(store_data)

@app.route('/store/<store_id>', methods=['PUT'])
def update_store(store_id):
    store_data = request.get_json()
    return StoreController.update_store(store_id, store_data)

@app.route('/store/<store_id>', methods=['DELETE'])
def delete_store(store_id):
    return StoreController.delete_store(store_id)

if __name__ == '__main__':
    app.run(debug=True)
```