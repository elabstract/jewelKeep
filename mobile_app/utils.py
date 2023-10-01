```python
import json

def load_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def update_data(file_name, new_data):
    data = load_data(file_name)
    data.update(new_data)
    save_data(file_name, data)

def delete_data(file_name, key):
    data = load_data(file_name)
    if key in data:
        del data[key]
        save_data(file_name, data)

def generate_id(data):
    return max(data.keys()) + 1 if data else 1
```