import csv
import random
import string

def add_password():
    # TODO: Implement the logic to add a new password
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    with open("passwords.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    print("Password added successfully.")
    pass

def retrieve_password():
    # TODO: Implement the logic to retrieve a password
    password_to_retrieve = input("Enter the username for the password you want to retrieve: ")

    with open("passwords.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == password_to_retrieve:
                print("Password:", row[1])
                break
        else:
            print("Password not found.")
    pass

def update_password():
    # TODO: Implement the logic to update a password
    username_to_update = input("Enter the username for the password you want to update: ")
    new_password = input("Enter the new password: ")

    with open("passwords.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == username_to_update:
                writer.writerow([row[0], new_password])
                print("Password updated successfully.")
            else:
                writer.writerow(row)

    if not any(row[0] == username_to_update for row in rows):
        print("Username not found.")
    pass

def delete_password():
    # TODO: Implement the logic to delete a password
    username_to_delete = input("Enter the username for the password you want to delete: ")

    with open("passwords.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open("passwords.csv", "w", newline="") as file:
        writer = csv.writer(file)
        deleted = False
        for row in rows:
            if row[0] == username_to_delete:
                deleted = True
                print("Password deleted successfully.")
            else:
                writer.writerow(row)

        if not deleted:
            print("Username not found.")
    pass

def generate_password():
    length = int(input("Enter the length of the password: "))
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    print("Generated Password:", password)
    pass

def main():
    while True:
        print("Password Manager")
        print("Enter a number between 1-6:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Generate New Password")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            update_password()
        elif choice == "4":
            delete_password()
        elif choice == "5":
            generate_password()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()