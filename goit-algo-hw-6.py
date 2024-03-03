class Phone:
    def __init__(self, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Invalid phone number")
        self.number = number

    def __str__(self):
        return self.number


class Birthday:
    def __init__(self, date):
        try:
            self.day, self.month, self.year = map(int, date.split('.'))
        except ValueError:
            raise ValueError("Invalid birthday format")

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"


class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}: {self.phone}"

    def add_birthday(self, birthday):
        self.birthday = birthday


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, birthday=None):
        if name in self.contacts:
            print("Contact already exists")
        else:
            self.contacts[name] = Record(name, phone, birthday)

    def change_contact(self, name, new_phone, new_birthday=None):
        if name not in self.contacts:
            print("Contact not found")
        else:
            self.contacts[name].phone = new_phone
            if new_birthday:
                self.contacts[name].add_birthday(new_birthday)

    def show_phone(self, name):
        if name not in self.contacts:
            print("Contact not found")
        else:
            print(self.contacts[name].phone)

    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(days=7)
        birthdays = []
        for contact in self.contacts.values():
            if contact.birthday and contact.birthday.month == today.month and contact.birthday.day >= today.day:
                if contact.birthday.day <= next_week.day:
                    birthdays.append(contact)
        return birthdays


def parse_input(line):
    command, *args = line.strip().lower().split()
    return command, args


def main():
    book = AddressBook()
    while True:
        line = input("> ")
        command, args = parse_input(line)
        if command == "add-contact":
            name, phone, birthday = args
            try:
                book.add_contact(name, Phone(phone), Birthday(birthday) if birthday else None)
            except ValueError as e:
                print(e)
        elif command == "change-contact":
            name, new_phone, new_birthday = args
            try:
                book.change_contact(name, Phone(new_phone), Birthday(new_birthday) if new_birthday else None)
            except ValueError as e:
                print(e)
        elif command == "show-phone":
            book.show_phone(args[0])
        elif command == "add-birthday":
            name, birthday = args
            try:
                book.contacts[name].add_birthday(Birthday(birthday))
            except ValueError as e:
                print(e)
        elif command == "show-birthday":
            contact = book.contacts.get(args[0])
            if contact and contact.birthday:
                print(contact.birthday)
            else:
                print("Contact not found or birthday not set")
        elif command == "birthdays":
            birthdays = book.get_upcoming_birthdays()
            if birthdays:
                for contact in birthdays:
                    print(contact.name)
            else:
                print("No upcoming birthdays")
        elif command in ("exit", "close"):
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()