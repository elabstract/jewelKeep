```python
from flask import Blueprint, request, jsonify
from mobile_app.services.user_service import UserService
from mobile_app.models.user import UserSchema

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()
user_schema = UserSchema()

@user_controller.route('/user', methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_user = user_service.create_user(user_data)
    return user_schema.dump(new_user), 201

@user_controller.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    return user_schema.dump(user)

@user_controller.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.get_json()
    updated_user = user_service.update_user(user_id, user_data)
    return user_schema.dump(updated_user)

@user_controller.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_service.delete_user(user_id)
    return '', 204
```