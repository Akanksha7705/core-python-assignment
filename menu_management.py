def add(menu, item):
    if item not in menu:
        menu.append(item)
    else:
        print(f"{item} is already in the menu.")
    return menu


def remove(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} does not exist in the menu.")
    return menu


def check(menu, item):
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]


add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"


updated_menu = add(initial_menu, add_item)
updated_menu = remove(updated_menu, remove_item)
availability = check(updated_menu, check_item)


print("Updated menu:", updated_menu)
print("Availability:", availability)
