#Task_1

def caching_fibonacci():
    cache = dict()
    def fibonacci(n):
       if n <= 0: return 0
       if n==1: return 1
       if n in cache: return cache[n]

       cache[n]= fibonacci(n - 1) + fibonacci(n - 2)
       return cache[n]
    return fibonacci

f=caching_fibonacci()
print(f(15))
print(f(10))

#Task_2
from functools import reduce
from typing import Callable
import re
def generator_numbers(text: str):
    numbers=map(float,filter(lambda x: re.match(r"\d+[\.,]{0,1}\d+.",x),text.split(" ")))
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable):
    return reduce(lambda x,y:x+y ,func(text))

if __name__=="__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

#Task_4
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "No such name found"
        except IndexError:
            return "Not found"
        except Exception as e:
            return f"Error: {e}"

    return inner

@input_error

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact update"

@input_error

def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'

@input_error

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