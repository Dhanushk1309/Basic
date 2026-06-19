def my_decorators(func):
    def wrapper():
        print("Preparing the pizza...")
        func()
        print("Add some Toppings")
    return wrapper
@my_decorators
def my_order():
    print("your pizza is ready")
my_order()
 