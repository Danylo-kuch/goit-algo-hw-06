from collections import UserDict
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Номер телефону повинен містити рівно 10 цифр")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        phones_str = ";".join(str(phones) for phones in self.phones)
        return f"Ім'я контакту: {self.name}, номери телефону: {phones_str}"
    
    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone: str):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError (f"Номер {phone} не було знайдено")
    
    def edit_phone(self, old:str, new:str):
        phone_obj = self.find_phone(old)
        if phone_obj:
            self.add_phone(new)
            self.remove_phone(old)
        else:
            raise ValueError("Старий номер не було знайдено")
    
    def find_phone(self, phone:str):
        for phones in self.phones:
            if phones.value == phone:
                return phones
        return None


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise ValueError(f"Контакт {record.name.value} вже існує!")
        else:
            self.data[record.name.value] = record


    def find(self, name: str):
        record = self.data.get(name)
        if not record:
            raise ValueError(f"Контакт {name} не знайдено")
        return record

    
    def delete(self, name: str):
        if self.data.get(name):
            del self.data[name]
        else:
            raise ValueError(f"Ім'я {name} не було знайдено")

            
    def __str__(self):
        result = []
        for record in self.data.values():
            result.append(str(record))
        return "\n".join(result)


def main():
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

if __name__ == "__main__":
    main()
