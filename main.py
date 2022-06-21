import locale

from item import Item


def main():
    shopping_list = []
    locale.setlocale(locale.LC_ALL, '')
    boolean = True

    while boolean:
        item_name = input("Enter an item to purchase (NA to end): ")

        if item_name.upper() != "NA":
            item_units = input("Units: ")
            item_quantity = int(input("Quantity: "))
            item_price = float(input("Price: "))

            item = Item(item_name, item_units, item_quantity, item_price)

            shopping_list.append(item)
        else:
            break

    print("Shopping List")
    total = 0
    for item in shopping_list:
        item_total = item.price * item.quantity
        print(f"{item.name} {item.units} {item.quantity} {locale.currency(item.price, grouping=True)} {locale.currency(item_total, grouping=True)}")
        total = item_total + total
        print(f"Total: {locale.currency(total, grouping=True)}")


if __name__ == '__main__':
    main()
