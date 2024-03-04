from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Your phone number is incorrect. Please enter a valid 10-digit phone number.")
        super().__init__(value)
    # Перевірка формату номера телефону


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
    # Додає новий телефон до запису

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]
    # Видалення телефону з запису

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone
                break
    # Заміна старого телефону на новий

    def find_phone(self, phone):
        for p in self.phones:
            if str(p) == phone:
                return p
    # Пошук телефону в записі

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[str(record.name)] = record
    # Додає новий запис до адресної книги

    def find(self, name):
        return self.data.get(name)
    # Знаходить запис за ім'ям у адресній книзі

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    # Видаляє запис за ім'ям з адресної книги