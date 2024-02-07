import time

def waiter():
    cook("Pasta", 8)
    cook("Salad Caesar", 8)
    cook("Chop", 16)

def cook(order, time_to_prepare):
    print(f"New order: {order}")
    time.sleep(time_to_prepare)
    print(order, " is ready")

waiter()

