import time


def show_menu():
    menu = {
        "1": ("پیتزا", 120000),
        "2": ("برگر", 80000),
        "3": ("پاستا", 100000),
        "4": ("سالاد", 50000)
    }
    print("\nمنوی رستوران:")
    for key, (food, price) in menu.items():
        print(f"{key}. {food} - {price} تومان ")
    return menu


def calculate_total(order, menu, tax_rate=0.09):
    subtotal = sum(menu[item][1] * quantity for item, quantity in order.items())
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total


def main():
    print("\U0001F37D️ خوش آمدید به رستوران ما!")
    menu = show_menu()
    order = {}
    extra_options = {}

    order_proccess = True
    while order_proccess:
        choice = input("\nشماره غذای مورد نظر را وارد کنید (یا '0' برای ثبت نهایی سفارش): ")

        if choice == "0":
            if not order:
                print("⛔ شما سفارشی ثبت نکرده‌اید!")
                continue
            order_proccess = False

        if choice in menu:
            try:
                quantity = int(input(f"🔢 چند عدد {menu[choice][0]} می‌خواهید؟ "))
                if quantity <= 0:
                    print("❌ تعداد باید عددی مثبت باشد!")
                    continue

            except ValueError:
                print("❌ لطفاً یک عدد معتبر وارد کنید!")
                continue

            extra = input("آیا سس اضافه می‌خواهید؟ (بله/خیر): ").strip()
            if extra == "بله":
                extra_options[choice] = "سس اضافه"

            if choice in order:
                order[choice] += quantity
            else:
                order[choice] = quantity

            print(f"✅ {quantity} عدد {menu[choice][0]} به سفارش شما اضافه شد.")
        else:
            print("❌ گزینه نامعتبر است. لطفاً یک شماره معتبر وارد کنید.")

    subtotal, tax, total = calculate_total(order, menu)
    print("\n💰 فاکتور نهایی شما:")
    for item, quantity in order.items():
        extra_text = f" + {extra_options[item]}" if item in extra_options else ""
        print(f"- {menu[item][0]} × {quantity}{extra_text}: {menu[item][1] * quantity} تومان")

    print(f"💵 قیمت کل: {subtotal} تومان")
    print(f"📊 مالیات (۹٪): {int(tax)} تومان")
    print(f"🤑 مبلغ پرداختی: {int(total)} تومان")
    print("⌛ سفارش شما در حال آماده‌سازی است...")
    time.sleep(2)
    print("✅ سفارش شما آماده شد. نوش جان! 🍕🍔")


if __name__ == "__main__":
    main()
