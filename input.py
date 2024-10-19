from typing import Tuple

def user_input() -> Tuple[str, str, int]:
    while True:
        deal_type: str = input("Do you wanna rent or sale?: ").lower()
        if deal_type not in ["rent", "sale"]:
            print("Please enter rent or sale.")
            continue

        rooms: str = input("Enter number of rooms: ")
        if not rooms.isdigit():
            print("Please enter number of rooms.")
            continue
        try:
            max_price: int = int(input("Enter the maximum rental price: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        break
    return deal_type, rooms, max_price
