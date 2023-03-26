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

eg.msgbox(combos)

