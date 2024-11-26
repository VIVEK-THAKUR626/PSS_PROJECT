Menu = [
    ["Noodles",30],
    ["Burger",40],
    ["French Fries",50],
    ["Pasta",80],
    ["Pizza",130]
]

def view_menu():
    srNo = 1
    print("--------MENU--------")
    for item in Menu:
        name, price = item
        print(f"{srNo}. {name} - {price}rs")
        srNo += 1
    print("--------------------")

order_placed = []

def place_order(no_of_items):
    print("--------------------------")

    print('''To choose the food item
Just enter the serial no.
of the food item mentioned
in the menu''')

    for _ in range(no_of_items):
        while True:
            try:
                food_item = int(input("Enter food item (serial no.): "))
                if 1 <= food_item <= len(Menu):
                    break
                else:
                    print("Invalid serial number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        while True:
            try:
                quantity = int(input("Enter the quantity: "))
                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")
        
        order_placed.append((food_item, quantity))
    
    total_cost = 0
    for orders in order_placed:
        food_item,quantity = orders
        total_cost += quantity*(Menu[food_item-1][1])

    print("--------------------------")
    print("Order :")
    for orders in order_placed:
        food_item,quantity = orders
        print(f"{Menu[food_item-1][0]} - {quantity}")
    print("--------------------------")
    print("Order Placed successfully")
    print(f"Total Cost : {total_cost}")
    print("--------------------------")

show_menu = input("Want to check the menu (Y/N) : ")

if show_menu == "y" or show_menu == "Y":
    view_menu()
    order = input("Want to place an order (Y/N) : ")
    if order == "y" or order == "Y":
        try:
            no_of_items = int(input("How many different items do you want to order: "))
            if no_of_items > 0:
                place_order(no_of_items)
            else:
                print("Number of items must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("THANK YOU FOR VISITING U-FOOD")
else:
    print("THANK YOU FOR VISITING U-FOOD")