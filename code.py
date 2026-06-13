# Digital Contact Book

contacts = {}

# Add 3 contacts
for i in range(3):
    print(f"\nEnter Contact {i + 1}")
    name = input("Name: ")
    phone = input("Phone Number: ")
    contacts[name] = phone

# Search for a contact
print("\n--- Search Contact ---")
search_name = input("Enter the name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found!")
