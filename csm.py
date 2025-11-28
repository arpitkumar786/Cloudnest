import csv
import os

DATA_FILE = "contacts.csv"

# ---------------- CONTACT CLASS ----------------
class Contact:
    def __init__(self, cid, name, phone, email, address):
        self.id = cid
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


# ---------------- FILE HANDLING ----------------
def load_contacts():
    contacts = []
    if not os.path.exists(DATA_FILE):
        return contacts

    with open(DATA_FILE, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 5:
                contacts.append(Contact(
                    int(row[0]), row[1], row[2], row[3], row[4]
                ))
    return contacts


def save_contacts(contacts):
    with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for c in contacts:
            writer.writerow([c.id, c.name, c.phone, c.email, c.address])


# ---------------- UTILITIES ----------------
def next_id(contacts):
    if not contacts:
        return 1
    return max(c.id for c in contacts) + 1


def print_contact(c):
    print(f"{c.id:<5}{c.name:<25}{c.phone:<15}{c.email:<25}{c.address:<30}")


# ---------------- CRUD OPERATIONS ----------------
def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    cid = next_id(contacts)
    contacts.append(Contact(cid, name, phone, email, address))
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    print(f"{'ID':<5}{'Name':<25}{'Phone':<15}{'Email':<25}{'Address':<30}")
    print("-" * 100)
    for c in contacts:
        print_contact(c)


def search_contact(contacts):
    query = input("Enter name / phone / email to search: ").lower()
    found = False
    for c in contacts:
        if query in c.name.lower() or query in c.phone or query in c.email.lower():
            print_contact(c)
            found = True
    if not found:
        print("No matching contact found.")


def update_contact(contacts):
    try:
        cid = int(input("Enter ID to update: "))
    except:
        print("Invalid ID.")
        return

    for c in contacts:
        if c.id == cid:
            print("Leave blank to keep existing value.")
            name = input(f"New Name ({c.name}): ").strip()
            phone = input(f"New Phone ({c.phone}): ").strip()
            email = input(f"New Email ({c.email}): ").strip()
            address = input(f"New Address ({c.address}): ").strip()

            if name:
                c.name = name
            if phone:
                c.phone = phone
            if email:
                c.email = email
            if address:
                c.address = address

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact(contacts):
    try:
        cid = int(input("Enter ID to delete: "))
    except:
        print("Invalid ID.")
        return

    for c in contacts:
        if c.id == cid:
            confirm = input(f"Delete {c.name}? (y/n): ").lower()
            if confirm == 'y':
                contacts.remove(c)
                save_contacts(contacts)
                print("Contact deleted.")
            return

    print("Contact not found.")


# ---------------- MENU ----------------
def menu():
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    return input("Select option (1-6): ")


# ---------------- MAIN PROGRAM ----------------
def main():
    contacts = load_contacts()

    while True:
        choice = menu()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
