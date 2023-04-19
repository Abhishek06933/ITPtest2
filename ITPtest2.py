PhoneDirectory = {}
def menu():
    print("""
Menu

1. Add a record

2. Search a record

3. Change a record

4. Delete a record

5. Quit
""")
def addRecord():
    name = input("Enter name: ")
    phone = input("Enter your 10-digit phone number: ")
    PhoneDirectory[name] = phone
    print("Record added\n")
    menu()

def searchRecord():
    name = input("Enter name to search: ")
    if name in PhoneDirectory:
        print(name + ": " + PhoneDirectory[name] + "\n")
    else:
        print("Record not found\n")
    menu()

def changeRecord():
    name = input("Enter name: ")
    if name in PhoneDirectory:
        phone = input("Enter new 10-digit phone number: ")
        PhoneDirectory[name] = phone
        print("Record updated\n")
    else:
        print("Record not found\n")
    menu()

def deleteRecord():
    name = input("Enter name: ")
    if name in PhoneDirectory:
        del PhoneDirectory[name]
        print("Record deleted\n")
    else:
        print("Record not found\n")
    menu()

print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")
print("1. Add a record\n2. Search a record\n3. Change a record\n4. Delete a record\n5. Quit\n")
while True:
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addRecord()
    elif choice == 2:
        searchRecord()
    elif choice == 3:
        changeRecord()
    elif choice == 4:
        deleteRecord()
    elif choice == 5:
        break
    else:
        print("Invalid choice\n")
