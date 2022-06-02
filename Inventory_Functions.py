'''Initialize our main functions for this Mock Implementation'''

def add(df):
    print("Enter the Item you wish to add to the inventory:")
    name = input()
    if name in df.values:
        print('\nThis Item already exists on the inventory')
        print(df.loc[df['Name'] == name])
        return df
    else:
        print("Enter the Quantity: ")
        quantity = input()
        print("Enter the Price: ")
        price = input()
        new_row = {'Name':name, 'Quantity':quantity, 'Price':price}
        df_new = df.append(new_row, ignore_index=True)
        print(df_new)
    return df_new

def delete(df):
    print("Enter the Item you wish to delete from the inventory:")
    name = input()
    if name not in df.values:
        print('\nThis Item does not exist on the inventory')
        return df
    else:
        df_new = df.drop(df[(df['Name'] == name)].index)
        df_new = df_new.reset_index(drop=True) #Reseting the index counter
        print('\n Item Deleted')
        print(df_new)
    return df_new


def update(df):
    print("Enter the Item you wish to update from the inventory:")
    name = input()
    if name not in df.values:
        print('\nThis Item does not exist on the inventory')
        return df
    else:
        cond = True
        while (cond):
            print("What do you wish to update Price , Quantity or Both ?: ")
            action = input()
            if action == 'Price' or action == 'Quantity' or action == 'Both':
                cond = False
        if action == 'Price':
            print('Enter new price: ')
            price = input()
            df.loc[df["Name"] == name, "Price"] = price
        elif action == 'Quantity':
            print('Enter new quantity: ')
            quantity = input()
            df.loc[df["Name"] == name, "Quantity"] = quantity
        else:
            print('Enter new price: ')
            price = input()
            df.loc[df["Name"] == name, "Price"] = price
            print('Enter new quantity: ')
            quantity = input()
            df.loc[df["Name"] == name, "Quantity"] = quantity

    print(df)
    return df











