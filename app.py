import sys

def calculate_total(price, quantity):
    return price * quantity

def main():
    while True:
        print("\n=== Shopping Bill Calculator (v1) ===")
        print("1. Calculate New Bill Item")
        print("2. Exit")
        try:
            choice = input("Enter choice (1-2): ").strip()
            if choice == '2':
                print("Exiting application. Goodbye!")
                sys.exit(0)
            if choice != '1':
                print("Invalid choice!")
                continue
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            if price < 0 or quantity < 0:
                print("Price and quantity must be positive values!")
                continue
            total = calculate_total(price, quantity)
            print(f"Total Bill Amount: ${total:.2f}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except (KeyboardInterrupt, SystemExit):
            break

if __name__ == "__main__":
    main()
