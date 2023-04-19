"""Fast food combos program indev v0.5"""

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



def edit_combos(combo_name):
    while True:
        combo = combos[combo_name]
        msg = f"Current combo you are editing: {combo_name}\n\n"
        msg += "ITEM\tPRICE\n"
        msg += "-" * 20 + "\n"
        for item_name, item_price in combo.items():
            msg += f"{item_name}\t${item_price:.2f}\n"
        eg.msgbox(msg, "Edit Combo")
        action = eg.buttonbox("What would you like to do?", "Editing options", ["Add Item", "Edit Item", "Delete Item", "Rename Combo", "Done"])
        if action == "Done":
            break
        elif action == "Add Item":
            while True:
                item = eg.enterbox("Please enter the name of the item you are adding to the combo:", "Add item")
                if item is None:
                    break
                try:
                    price = float(eg.enterbox(f"Please enter the price of a {item}:", "Price"))
                    if price < 0.5 or price > 100:
                        raise ValueError
                    combo[item] = price
                    break
                except ValueError:
                    eg.msgbox("Please enter a float number between 0.50 and 100.0", "Invalid price")
        elif action == "Edit Item":
            item_name = eg.choicebox("Choose an item to edit:", choices=list(combo.keys()), title="Edit Item")
            if item_name is None:
                continue
            while True:
                try:
                    item_price = float(eg.enterbox(f"Enter new price for {item_name}:", "Enter new price"))
                    if item_price < 0.5 or item_price > 100:
                        raise ValueError
                    combo[item_name] = item_price
                    break
                except ValueError:
                    eg.msgbox("Please enter a float number between 0.50 and 100.0", "Invalid price")
        elif action == "Delete Item":
            item_name = eg.choicebox("Choose an item to delete:", choices=list(combo.keys()), title="Delete Item")
            if item_name is None:
                continue
            del combo[item_name]
        elif action == "Rename Combo":
            while True:
                new_combo_name = eg.enterbox("Enter new name for the combo:", "Rename Combo")
                if new_combo_name is None:
                    break
                if new_combo_name in combos:
                    eg.msgbox("Combo name already exists. Please choose a different name.", "Invalid name")
                    continue
                combos[new_combo_name] = combos.pop(combo_name)
                combo_name = new_combo_name
                break
    items = [f"{item}: {price}" for item, price in combo.items()]
    combo_details = "\n".join(items)
    eg.msgbox(f"The {combo_name.capitalize()} combo has been updated.\n\nNew combo details:\n{combo_details}", "Combo Updated")
    return {combo_name: combo}


def print_combos():
    print(combos)


welcome()
main_menu()
