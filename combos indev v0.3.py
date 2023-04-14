"""Fast food combos program indev v0.2"""

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
    """filler"""


def add_combos():
    """filler"""


def search_for_combos():
    """filler"""


def delete_combos():
    """filler"""


def edit_combos():
    """filler"""


welcome()
main_menu()
