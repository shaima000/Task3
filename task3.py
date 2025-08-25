fruit_prices = {
    "apple": 2.5,
    "banana": 1.2,
    "cherry": 3.0,
    "date": 4.0,
    "elderberry": 5.5,
    "watermelon": 7.0,
    "kiwi": 2.8,
    "mango": 3.5,
    "orange": 1.8,
}

fruit = input("enter the name of the fruit: ")
if fruit in fruit_prices:
    print(f"the price of {fruit} is --> ${fruit_prices[fruit]}")
else:
    print("Sorry, this fruit is not available.")
