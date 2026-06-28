contact = {
    "ALI" : "4353245294",
    "AMAN": "2292303847",
    "REHAN" : "3483729326",
    "RIYA"  : "7463202392"
}
while True:
    print("-----CONTACT BOOK-----")
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT")
    print("3. SEARCH CONTACT")
    print("4. DELETE CONTACT")
    print("5 .EXIT")

    choice = int(input('ENTER YOUR CHOICE '))

    if choice == 1:
        print("ENTER NEW CONTECT ")
        name = input("enter name ").upper()
        number = input("enter number ")
        contact[name] = number
        print(contact)
    elif choice == 2:
        print(contact)
    elif choice == 3:
        name = input("enter contact name: ").upper()
        if name in contact:
            print("PHONE NUMBER",contact[name])
        else:
            print("Contact not found")
    elif choice == 4:
        name = input("ENTER NAME: ").upper()
        if name in contact:
            del contact[name]
            print("contact deleted successfully")
        else:
            print("contact not found ")
    elif choice == 5:
        print("GOOD BYE")

