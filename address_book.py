import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

        if not re.match(r'^\d{10}$', value):
            raise ValueError('Improper phone format. Must be 10 digits ')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

        raise LookupError(f'Phone number {phone} was not found.')

    def edit_phone(self, phone, new_phone):
        for p in self.phones:
            if p.value == phone:
                p.value = new_phone
                return
        raise LookupError(f'Phone number {phone} was not found.')

    def remove_phone(self, phone):
        [self.phones.remove(p) for p in self.phones if p.value == phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name]

    def delete(self, name):
        del self.data[name]
