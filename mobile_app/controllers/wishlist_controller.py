```python
from flask import Blueprint, request, jsonify
from mobile_app.services import wishlist_service
from mobile_app.models.wishlist_item import WishlistItemSchema

wishlist_controller = Blueprint('wishlist_controller', __name__)
wishlist_schema = WishlistItemSchema()

@wishlist_controller.route('/wishlist', methods=['POST'])
def create_wishlist_item():
    wishlist_data = request.get_json()
    new_wishlist_item = wishlist_service.createWishlistItem(wishlist_data)
    return wishlist_schema.jsonify(new_wishlist_item), 201

@wishlist_controller.route('/wishlist/<id>', methods=['PUT'])
def update_wishlist_item(id):
    wishlist_data = request.get_json()
    updated_wishlist_item = wishlist_service.updateWishlistItem(id, wishlist_data)
    return wishlist_schema.jsonify(updated_wishlist_item), 200

@wishlist_controller.route('/wishlist/<id>', methods=['DELETE'])
def delete_wishlist_item(id):
    wishlist_service.deleteWishlistItem(id)
    return jsonify({'message': 'Wishlist item deleted'}), 200

@wishlist_controller.route('/wishlist', methods=['GET'])
def get_all_wishlist_items():
    wishlist_items = wishlist_service.get_all_wishlist_items()
    return wishlist_schema.jsonify(wishlist_items), 200

@wishlist_controller.route('/wishlist/<id>', methods=['GET'])
def get_wishlist_item(id):
    wishlist_item = wishlist_service.get_wishlist_item(id)
    return wishlist_schema.jsonify(wishlist_item), 200
```