import time

food_clock = {
    "Pasta": 8,
    "Salad Caesar": 3,
    "Chop": 10
}

def waiter():
    for key, value in food_clock.items():
        cook(key, value)

def cook(order, time_to_prepare):
    print(f"New order: {order}")
    time.sleep(time_to_prepare)
    print(order, " is ready")

waiter()