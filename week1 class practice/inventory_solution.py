# Inventory Management System
#简易库存系统
# The inventory is stored in a dictionary.
# Keys are item names and values are quantities.
inventory = {}

# Function to add an item to the inventory
def add_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory dictionary.检查是否在库存
    # 2. If it does, increase its quantity.如果有，加数量
    # 3. If not, add the item to the inventory with the given quantity.如果没有，添加item和数量
    if item in inventory:
        inventory[item] += quantity
        # inventory[item] = inventory[item] + quantity
    else:
        inventory[item] = quantity
    print(f"Item '{item}' added / updated. Current quantity: {inventory[item]}")

# Function to view all items in the inventory
def view_inventory():
    # Implementation Instructions:
    # 1. Loop through the inventory dictionary.遍历库存dic
    # 2. Print each item's name and its quantity.
    if not inventory:
        print("The inventory is currently empty.")
        return

    print("Inventory items and quantities are below:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


# Function to update the quantity of an existing item in the inventory
def update_item(item, quantity):
    # Implementation Instructions:
    # 1. Check if the item exists in the inventory.
    # 2. If it does, update its quantity. 如果有，更新库存
    # 3. If the item doesn't exist, print a message indicating it's not found. 如果没有，显示不存在

    if item in inventory:
        inventory[item] = quantity
        print(f"Item '{item}' update quantity: {inventory[item]}")
    else:
        # Item not found in the inventory
        print(f"Item '{item}' it's not found.")

# Main function to manage the inventory
def manage_inventory():
    while True:
        print("\n Inventory Management System")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Item Quantity")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        # Process the user's choice
        # Implementation Instructions:
        # 1. If the choice is '1', prompt the user to enter an item name and quantity,
        #    and then call the add_item function.
        # 2. If the choice is '2', call the view_inventory function.
        # 3. If the choice is '3', prompt the user to enter an item name and new quantity,
        #    and then call the update_item function.
        # 4. If the choice is '4', break the loop to exit the program.
        # 5. For any other input, display an error message.
        if choice == '1':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))

            add_item(item, quantity)

        elif choice == '2':
            view_inventory()


        elif choice == '3':
            item = input("Enter the item name: ")
            quantity = int(input("Enter the new quantity: "))

            update_item(item, quantity)


        elif choice == '4':
            print("Exiting the Inventory Management System.")
            break


        else: #other input is wrong
            print("Invalid choice. Please enter a number 1/2/3/4.")



# 主程序
if __name__ == "__main__":
    manage_inventory()
