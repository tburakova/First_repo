from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
       
    def __str__(self):
        return str(self.value) 

class Name(Field): 
    pass

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def is_valid(self):
        if len(str(self.phone)) == 10:
            return (f"self.phone")
        else:
            return (f"Номер не відповідає формату")
        
class Record (Field):
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
        
        self.phones = []    
    
    def add_phone (self):
        for  self.phone in self.phones:
            if self.phone not in self.phones:
                return self.phones.append(self.phone, end= ',')
            else:
                return self.phone == self.phone
            
    def find_phone(self):
        for self.phone in self.phones:
            if self.phone in self.phones:
                return self.phone
            else:
                return f'{self.phone} is not found'
   
    def edit_phones(self):
        [self.phone if self.phone == self.phone else self.phone for self.phone in self.phones]
        return self.phones

    # реалізація класу
    
class AddressBook(UserDict): # реалізація класу
    
    def add_record (self, name, record):
        record = Record(record)
        self.data[name] = record
        for name, record in self.data.items():
            if name and record not in self.data.items:
                self.data.update(name, record)
                return f'{name, record}'
            else:
                print (f'{record}')  

    def find (self, name, record):
        for name, record in self.data.items():
            if name and record in self.data.items():
                return f'{record}'
            
    def  delete (self, name, record):
        for name, record in self.data.items():
            if name and record not in self.data.items:
                self.data.pop (name, record) 
            return f'{record}'
          
__name__ == "__main__"