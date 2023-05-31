def read_contacts():
    contacts = {}
    while True:
        text = input()
        if text.isnumeric():
            break
        name, phone = text.split('-')
        contacts[name] = phone
    return contacts, int(text)

def print_person(contacts, n):
    for _ in range(n):
        name = input()

        if name in contacts:
            print(f"{name} -> {contacts[name]}")
        else:
            print(f'contact {name} not in phonebook')


contacts, n = read_contacts()
print_person(contacts, n)
