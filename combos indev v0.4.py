"""Fast food combos program indev v0.4"""

import easygui as eg

combos = {  # made the dictionary
    "Value": {
        "Beef burger": 5.96,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Cheezy": {
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy drink": 1.00
    },
    "Super": {
        "Cheeseburger": 6.69,
        "large fries": 2.00,
        "Smoothie": 2.00
    }
}


def welcome():
    instructions = eg.buttonbox("Welcome to our combo program!\n"
                                "If you are new, or haven't used this program before please select the -Display Instructions- button"
                                ", but if you have used this program before please press -skip-", "Welcome!",
                                ["Display Instructions", "skip"])

    if instructions == "Display Instructions":
        eg.msgbox("As you go through the menu, you will be prompted by messages and multichoice options in boxes, "
                  "like the one you are reading this from now. "
                  "please navigate through the program using the buttons on these boxes.", "Instructions")


def main_menu():
    global combos
    option = eg.buttonbox("What would you like to do?", "Main Menu", ["Add combo", "Find combo", "Delete combo",
                                                                      "Output all", "Exit"])
    if option == "Add combo":
        combos |= add_combos()
        main_menu()
    elif option == "Find combo":
        search_for_combos()
    elif option == "Delete combo":
        delete_combos()
    elif option == "Output all":
        print_combos()
    else:
        eg.msgbox("Thank you for using our program", "Goodbye")


def add_combos():
    combo_name = eg.enterbox("Please enter the name of the combo:", "Combo name")
    new_combo = {}
    add_item = "Yes"
    while add_item == "Yes":
        float_check = "False"
        item = eg.enterbox("Please enter the name of the item you are adding to the combo:", "Add item")
        while float_check == "False":
            price = eg.enterbox(f"Please enter the price of a {item}:", "Price")
            try:
                if float(price) < 0.5 or float(price) > 100:
                    price = "null"
                float_num = float(price)
                float_check = "True"
            except ValueError:
                eg.msgbox("please enter a float number between 0.50 and 100.0")
        new_combo[item] = price
        add_item = eg.buttonbox("Do you want to add another item?", "Add more items", ["Yes", "No"])
    return {combo_name: new_combo}


def search_for_combos():
    print("find combos")


def delete_combos():
    print("delete combos")


def edit_combos():
    print("edit combos")


def print_combos():
    print(combos)


welcome()
main_menu()
