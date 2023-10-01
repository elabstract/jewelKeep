```python
from mobile_app.models.user import UserSchema
from mobile_app.database import db_session

user_schema = UserSchema()

def get_all_users():
    users = db_session.query(User).all()
    return user_schema.dump(users, many=True)

def get_user_by_id(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    return user_schema.dump(user)

def create_user(user_data):
    new_user = user_schema.load(user_data, session=db_session)
    db_session.add(new_user)
    db_session.commit()
    return user_schema.dump(new_user)

def update_user(user_id, user_data):
    user = db_session.query(User).filter(User.id == user_id).first()
    for key, value in user_data.items():
        setattr(user, key, value)
    db_session.commit()
    return user_schema.dump(user)

def delete_user(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    db_session.delete(user)
    db_session.commit()
    return user_schema.dump(user)
```