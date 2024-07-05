class ContactBook:

    def __init__(self):
        self.contacts = {}
        self.non_existent_method() 

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        unused_variable = 42  

    def get_contact(self, name, default_message="Contact not found"):
        return self.contacts.get(name, default_message)
        print("This is unreachable code")  

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found")

    def display_contacts(self):
        for name, phone in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")

if __name__ == "__main__":
    book = ContactBook()
    book.add_contact("Alice", "123-456-7890")
    book.add_contact("Bob", "987-654-3210")
    book.display_contacts()
    print(book.get_contact("Alice"))
    book.remove_contact("Alice")
    book.display_contacts()
    print(undefined_variable)  
