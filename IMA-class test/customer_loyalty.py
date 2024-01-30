# 1. customer database
def create_customers_db():
    return {}

# add customer to database
def add_customer(customers, name, contact):
    # name means customer name; contact means customer contact details; 
    # points means customer points; redeemed means customer redeemed points
    if name not in customers:
        customers[name] = {"contact": contact, "points": 0, "redeemed": 0}
    # consider the case that name in customers
    else:
        print("Customers already exist!")

# record transaction points earned   per transaction per customer
def record_points(customers, name, transaction_points):
    if name in customers:
        # consider the case that transaction_points > 0
        if transaction_points > 0:
            customers[name]["points"] += transaction_points
        # consider the case that transaction_points < 0
        else:
            print("loyalty points must be greater than 0")
    # consider the case that name not in customers
    else:
        print("Customers not exist!")



# 2. Loyalty tracking function:
# calculate points earned per customer
def display_transaction_points(name, transaction_points):
    print(f"{name}loyalty points earned by this transaction: {transaction_points}")

# display total points for each customer
def display_total_points(customers, name):
    if name in customers:
        # display total points for each customer
        print(f"{name}total loyalty points: {customers[name]['points']}")
    else:
        print("Customers not exist!")

# 3. customer loyalty management function:
# Offering loyalty rewards
def offer_rewards(customers, name, points_needed):
    if name in customers:
        # consider the case that points_needed > 0
        if customers[name]["points"] >= points_needed:
            customers[name]["points"] -= points_needed
            customers[name]["redeemed"] += points_needed
            print(f"{name}has done redemption by using loyalty points: {points_needed}")
        # consider the case that points_needed < 0
        else:
            print("No enought loyalty points!")
    else:
        print("Customers not exist!")

# display loyalty status:    normal and high level
def display_loyalty_status(customers, name):
    if name in customers:
        status = "normal" if customers[name]["points"] < 1000 else "high level"   #judge the status
        print(f"{name}loyalty status: {status}")
    else:
        print("Customers not exist!")

# Resetting loyalty points after redemption, reset points to 0
def reset_points(customers, name):
    if name in customers:
        customers[name]["points"] = 0
    else:
        print("Customers not exist!")

# 4. Loyalty Reporting System
def loyalty_report(customers):
    # display all customers' loyalty points and redemption status
    for name, info in customers.items():
        print(f"{name}: total loyalty points: {info['points']}, has done redemption: {info['redeemed']}")



def main():
    customers = create_customers_db()
    while True:
        print("\n1. add customers\n2. record loyalty points\n3. display loyalty points\n4. redemption loyalty points for discount\n5. display loyalty status\n6. reset loyalty points\n7. check loyalty reports\n8. Exit")
        choice = input("choose operation: ")
        # consider the case that choice is in 1-8
        if choice == "1":
            name = input("input customer name: ")
            contact = input("input customer contact details: ")
            add_customer(customers, name, contact)
        elif choice == "2":
            name = input("input customer name: ")
            points = int(input("input loyalty points: "))
            record_points(customers, name, points)
            # display loyalty points earned by this transaction
            display_transaction_points(name, points)
        elif choice == "3":
            name = input("input customer name: ")
            display_total_points(customers, name)
        elif choice == "4":
            name = input("input customer name: ")
            points_needed = int(input("input the points want to used for redemption: "))
            offer_rewards(customers, name, points_needed)
        elif choice == "5":
            name = input("input customer name: ")
            display_loyalty_status(customers, name)
        elif choice == "6":
            name = input("input customer name: ")
            reset_points(customers, name)
        elif choice == "7":
            loyalty_report(customers)
        elif choice == "8":
            break
        # consider the case that choice is not in 1-8
        else:
            print("invalid input, please input again!")

if __name__ == "__main__":
    main()


