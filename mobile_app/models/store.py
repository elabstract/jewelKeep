```python
from sqlalchemy import Column, Integer, String
from mobile_app.database import Base

class Store(Base):
    __tablename__ = 'stores'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    address = Column(String(120))
    items = Column(String(500))

    def __init__(self, name=None, address=None, items=None):
        self.name = name
        self.address = address
        self.items = items

    def __repr__(self):
        return '<Store %r>' % (self.name)
```