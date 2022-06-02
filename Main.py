from init_inventory_list import *
from Inventory_Functions import *

'''Implementation for the Inventory management done with Pandas'''
df = load_inventory()
print("########### Welcome to iptiQ Inventory Service############")

while(True):
    print("1. Display Current Inventory")
    print("2. Add Items to the Inventory")
    print("3. Delete Items from the Inventory")
    print("4. Update Items in the inventory")
    print("5. Exit")

    print("Please Enter Your input 1-5: ")
    action = int(input())
    if (action == 1):
        print(df)
    elif(action == 2):
        df = add(df)
    elif(action == 3):
        df = delete(df)
    elif(action == 4):
        df = update(df)
    elif(action == 5):
        print("Until Next time")
        break
    else:
        print("Invalid input please give a number 1-5")


