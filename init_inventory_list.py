import pandas as pd
'''I assumed there is some kind of initial file with some kind of existing inventory so i created a very simple csv file with fruits as inventory'''

def load_inventory():
    df = pd.read_csv('../Inventory_iptiQ/Inventory.csv')
    return df


