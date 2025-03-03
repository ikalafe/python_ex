import argparse
import time


def show_menu():
    menu = {
        "1": ("Pizza", 120000),
        "2": ("Burger", 80000),
        "3": ("Pasta", 100000),
        "4": ("Salad", 50000)
    }
    print("\nRestaurant Menu:")
    for key, (food, price) in menu.items():
        print(f"{key}. {food} - {price} Toman")
    return menu


def parse_arguments():
    parser = argparse.ArgumentParser(description="Restaurant Order CLI")
    parser.add_argument(
        "--items",
        nargs="+",
        help="List of items in the format 'item_id:quantity' (e.g., '1:2 3:1')"
    )
    parser.add_argument(
        "--extras",
        nargs="*",
        help="Optional extras in the format 'item_id:extra_name' (e.g., '1:extra_sauce')"
    )
    parser.add_argument(
        "--show-menu",
        action="store_true",
        help="Display menu and exit"
    )
    return parser.parse_args()


def process_order(args, menu):
    order = {}
    extras = {}

    if args.items:
        for item in args.items:
            try:
                item_id, quantity = item.split(":")
                quantity = int(quantity)
                if item_id in menu and quantity > 0:
                    order[item_id] = order.get(item_id, 0) + quantity
            except ValueError:
                print(f"⚠️ Invalid format for {item}. Correct format: 'item_id:quantity'")

    if args.extras:
        for extra in args.extras:
            try:
                item_id, extra_name = extra.split(":")
                if item_id in menu:
                    extras[item_id] = extra_name
            except ValueError:
                print(f"⚠️ Invalid format for {extra}. Correct format: 'item_id:extra_name'")

    return order, extras


def calculate_total(order, menu, tax_rate=0.09):
    subtotal = sum(menu[item][1] * quantity for item, quantity in order.items())
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total


def print_receipt(order, extras, menu):
    subtotal, tax, total = calculate_total(order, menu)
    print("\n💰 Your Final Receipt:")
    for item, quantity in order.items():
        extra_text = f" + {extras[item]}" if item in extras else ""
        print(f"- {menu[item][0]} × {quantity}{extra_text}: {menu[item][1] * quantity} Toman")
    print(f"\n💵 Subtotal: {subtotal} Toman")
    print(f"📊 Tax (9%): {int(tax)} Toman")
    print(f"🤑 Total: {int(total)} Toman")


def main():
    args = parse_arguments()
    menu = show_menu()

    if args.show_menu:
        return  # نمایش منو و خروج از برنامه

    order, extras = process_order(args, menu)

    if not order:
        print("⛔ No orders placed!")
        return

    print_receipt(order, extras, menu)
    print("⌛ Preparing your order...")
    time.sleep(2)
    print("✅ Your order is ready. Enjoy! 🍕🍔")


if __name__ == "__main__":
    main()
