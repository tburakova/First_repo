from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, number):
        self.number = number
        if len(number) != 10 or not number.isdigit():
            raise ValueError("Phone number must be 10 digits long")
        super().__init__(number) 

class Birthday:
    def __init__(self, date):
        self.date = date

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phone = Phone(phone)
        self.birthday = None

    def add_birthday(self, date):
        self.birthday = Birthday(date)

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        record = Record(name, phone)
        self.contacts.append(record)

    def change_contact(self, name, new_phone):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone = Phone(new_phone)
                return True
        return False

    def show_phone(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact.phone.number
        return "Contact not found"

    def add_birthday_to_contact(self, name, date):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.add_birthday(date)
                return True
        return False

    def get_upcoming_birthdays(self):
        today = datetime.now()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = []

        for contact in self.contacts:
            if contact.birthday:
                contact_birthday = datetime.strptime(contact.birthday.date, "%d.%m.%Y")
                if today <= contact_birthday <= next_week:
                    upcoming_birthdays.append(contact.name)

        return upcoming_birthdays

def parse_input(input_str):
    parsed_input = input_str.split()
    command = parsed_input[0].lower()

    if command == "add-contact":
        if len(parsed_input) == 3:
            name = parsed_input[1]
            phone = parsed_input[2]
            return ("add_contact", name, phone)
        else:
            return ("invalid",)

    elif command == "change-contact":
        if len(parsed_input) == 3:
            name = parsed_input[1]
            new_phone = parsed_input[2]
            return ("change_contact", name, new_phone)
        else:
            return ("invalid",)

    elif command == "show-phone":
        if len(parsed_input) == 2:
            name = parsed_input[1]
            return ("show_phone", name)
        else:
            return ("invalid",)

    elif command == "add-birthday":
        if len(parsed_input) == 3:
            name = parsed_input[1]
            date = parsed_input[2]
            return ("add_birthday", name, date)
        else:
            return ("invalid",)

    elif command == "show-birthday":
        if len(parsed_input) == 2:
            name = parsed_input[1]
            return ("show_birthday", name)
        else:
            return ("invalid",)

    elif command == "birthdays":
        return ("upcoming_birthdays",)

    elif command == "exit" or command == "close":
        return ("exit",)

    else:
        return ("invalid",)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        parsed_command = parse_input(user_input)

        if parsed_command[0] == "add_contact":
            book.add_contact(parsed_command[1], parsed_command[2])
            print("Contact added successfully")

        elif parsed_command[0] == "change_contact":
            if book.change_contact(parsed_command[1], parsed_command[2]):
                print("Contact updated successfully")
            else:
                print("Contact not found")

        elif parsed_command[0] == "show_phone":
            phone_number = book.show_phone(parsed_command[1])
            print(f"The phone number is: {phone_number}")

        elif parsed_command[0] == "add_birthday":
            if book.add_birthday_to_contact(parsed_command[1], parsed_command[2]):
                print("Birthday added successfully")
            else:
                print("Contact not found")

        elif parsed_command[0] == "show_birthday":
            print("Functionality to show birthdays is not implemented yet")

        elif parsed_command[0] == "upcoming_birthdays":
            upcoming_birthdays = book.get_upcoming_birthdays()
            print("Upcoming birthdays to celebrate next week:")
            for name in upcoming_birthdays:
                print(name)

        elif parsed_command[0] == "exit":
            print("Exiting the program. Goodbye!")
            break

        elif parsed_command[0] == "invalid":
            print("Invalid command. Please try again")

if __name__ == "__main__":
    main()