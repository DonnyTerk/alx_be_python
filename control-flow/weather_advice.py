#!/usr/bin/python3

# 1. Prompt the user for input and store it in a variable, converting it to lowercase
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Use if/elif/else statements to provide clothing recommendations

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")