expence = []
while True:
    print("-----EXPENCE TRACKING-----")
    print("1. ADD EXPENCE")
    print("2. VIEW EXPENCE")
    print("3. TOTAL EXPENCE")
    print("4. DELETE EXPENCE")
    print("5 .EXIT")
    
    user = int(input("enter your choice : "))
    if user == 1 :
        date = input("enter date : ")
        category = input("enter category : ")
        amount = int(input("enter amount : "))
        new_expence = {
            "Date": date,
            "CATEGORY": category,
            "AMOUNT"  : amount
        }
        expence.append(new_expence)
        print("expence added successfully")
    elif user == 2:
        print(expence)
    elif user == 3:
        total = 0
        for item in expence:
            total = total + item['AMOUNT']
        print(f"total expence is Rs {total}" )
    elif user == 4:
        find = input("enter category :")
        for i ,item in enumerate(expence,start=1):
            print(i,item)
        delete = int(input(" enter no which you want to delete : "))
        expence.pop(delete-1)
        print("expence deleted successfully")

    else:
        print("THANK YOU ")
        break









        
