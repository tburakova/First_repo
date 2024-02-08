#Task_1
path = r"D:\Project\salary.txt"


def total_salary(path):
       try:
           with open(path,"r",encoding="UTF-8") as file1:
              salary=[float(el.strip().split(",")[1]) for el in file1.readlines() if el]
              return (sum(salary),sum(salary)/len(salary))
       except: FileNotFoundError
total, average = total_salary(path)
print(f"Загальна сума: {total}, середня заробіттна плата: {average}")


#Task_2

path = r"D:\Project\cat.txt"

def get_cats_info(path):
    try:
        with open(path, 'r', encoding='UTF-8') as cats:
            list=[]  
            read_cats = cats.readlines()
            for cat in read_cats:
                pars= cat.strip().split(',')
                cat_id, cat_name, cat_age = pars
                list.append({"id": cat_id, "name": cat_name, "age": cat_age})
    except Exception as e:
        print(f"Error: {e}")
    return list
list=get_cats_info(path)

print(*list, sep='\n')


#Task_4
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact update"

def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

def show_all(args, contacts):
       for k,v in contacts.items():
           return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()