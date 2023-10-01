```python
import tkinter as tk
from mobile_app.controllers import user_controller, wishlist_controller, store_controller

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Jewelry Wishlist App")

        self.user_profile_frame = tk.Frame(self.window, bd=5)
        self.user_profile_frame.pack(side=tk.LEFT)

        self.wishlist_frame = tk.Frame(self.window, bd=5)
        self.wishlist_frame.pack(side=tk.LEFT)

        self.store_directory_frame = tk.Frame(self.window, bd=5)
        self.store_directory_frame.pack(side=tk.LEFT)

        self.user_controller = user_controller.UserController()
        self.wishlist_controller = wishlist_controller.WishlistController()
        self.store_controller = store_controller.StoreController()

        self.create_user_profile_section()
        self.create_wishlist_section()
        self.create_store_directory_section()

    def create_user_profile_section(self):
        user_data = self.user_controller.get_user_data()
        tk.Label(self.user_profile_frame, text="User Profile").pack()
        tk.Label(self.user_profile_frame, text=f"Username: {user_data['username']}").pack()
        tk.Label(self.user_profile_frame, text=f"Email: {user_data['email']}").pack()

    def create_wishlist_section(self):
        wishlist_data = self.wishlist_controller.get_wishlist_data()
        tk.Label(self.wishlist_frame, text="Wishlist").pack()
        for item in wishlist_data:
            tk.Label(self.wishlist_frame, text=f"Item: {item['name']}, Price: {item['price']}").pack()

    def create_store_directory_section(self):
        store_data = self.store_controller.get_store_data()
        tk.Label(self.store_directory_frame, text="Store Directory").pack()
        for store in store_data:
            tk.Label(self.store_directory_frame, text=f"Store: {store['name']}, Location: {store['location']}").pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```