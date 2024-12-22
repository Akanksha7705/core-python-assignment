def calctotal(cart):
    total = sum(cart.values())
    if len(cart) > 5 :
        total *= 0.9
    return total


cart = {'Laptop':50000 , 'Headphones':2000, 'Mouse':500, 'Keyboard':1500}
print(f"Cart is: {cart}")
print(f"Total price: {calctotal(cart)}")