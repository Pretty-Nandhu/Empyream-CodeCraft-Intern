class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.preferences = []

    def add_preference(self, category):
        self.preferences.append(category)

    def recommend_products(self, product_database):
        recommended_products = []
        for product in product_database:
            if product.category in self.preferences:
                recommended_products.append(product)
        return recommended_products

product_database = [
    Product("P001", "Laptop", "Electronics", 1000),
    Product("P002", "Smartphone", "Electronics", 800),
    Product("P003", "Headphones", "Electronics", 100),
    Product("P004", "Shirt", "Clothing", 30),
    Product("P005", "Jeans", "Clothing", 50),
    Product("P006", "Shoes", "Footwear", 60),
]

users = []

def register_user():
    user_id = input("Enter user ID: ")
    name = input("Enter your name: ")
    user = User(user_id, name)
    users.append(user)
    print("User registered successfully!")

def enter_preferences(user):
    print("Available categories:")
    categories = set(product.category for product in product_database)
    for category in categories:
        print(category)

    preferences = input("Enter your preferred categories (comma-separated): ").split(",")
    for preference in preferences:
        user.add_preference(preference.strip())
    print("Preferences added successfully!")

def main():
    while True:
        print("\n1. Register\n2. Enter Preferences\n3. Recommend Products\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = input("Enter your user ID: ")
            user = next((u for u in users if u.user_id == user_id), None)
            if user:
                enter_preferences(user)
            else:
                print("User not found.")
        elif choice == "3":
            user_id = input("Enter your user ID: ")
            user = next((u for u in users if u.user_id == user_id), None)
            if user:
                recommended_products = user.recommend_products(product_database)
                print("Recommended Products:")
                for product in recommended_products:
                    print(f"{product.name} - ${product.price}")
            else:
                print("User not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()