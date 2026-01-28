import datetime

users = {}
posts = []


def get_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def input_not_empty(msg):
    while True:
        value = input(msg).strip()
        if value == "":
            print("Input cannot be empty. Try again.")
        else:
            return value


def register_user():
    print("\n--- User Registration ---")
    
    while True:
        username = input_not_empty("Enter username: ")
        if username in users:
            print("Username already exists. Try another.")
        else:
            break

    password = input_not_empty("Enter password: ")
    users[username] = password
    print("Registration successful!")

def login_user():
    print("\n--- Login ---")
    
    attempts = 3
    while attempts > 0:
        username = input_not_empty("Username: ")
        password = input_not_empty("Password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            return username
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}")

    print("Too many failed attempts.")
    return None

def create_post(username):
    print("\n--- Create Post ---")
    
    title = input_not_empty("Title: ")
    description = input_not_empty("Description: ")

    choice = input("Use auto date? (y/n): ").lower()
    if choice == "n":
        date = input_not_empty("Enter date (YYYY-MM-DD): ")
    else:
        date = get_date()

    post = {
        "author": username,
        "title": title,
        "description": description,
        "date": date
    }

    posts.append(post)
    print("Post created successfully!")

def view_posts():
    print("\n--- All Posts ---")

    if not posts:
        print("No posts available.")
        return

    for i, post in enumerate(posts, 1):
        print(f"\nPost #{i}")
        print("-" * 30)
        print(f"Author      : {post['author']}")
        print(f"Title       : {post['title']}")
        print(f"Date        : {post['date']}")
        print(f"Description : {post['description']}")
        print("-" * 30)

def search_posts_by_user():
    print("\n--- Search Posts by Username ---")
    
    username = input_not_empty("Enter username: ")

    found = False
    for post in posts:
        if post["author"] == username:
            found = True
            print("\n----------------------------")
            print(f"Author      : {post['author']}")
            print(f"Title       : {post['title']}")
            print(f"Date        : {post['date']}")
            print(f"Description : {post['description']}")
            print("----------------------------")

    if not found:
        print(" No posts found for this user.")

def user_menu(username):
    while True:
        print(f"\n Logged in as: {username}")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            create_post(username)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_posts_by_user()
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def main():
    while True:
        print("\n=== PostBoard App ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            user = login_user()
            if user:
                user_menu(user)
        elif choice == "3":
            print("Exiting PostBoard...")
            break
        else:
            print("Invalid choice.")

# Run App
main()
