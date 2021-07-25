# This program converts kilometers to miles

def convert(km):
    y = km * 0.6214
    return y


distance = convert(float(input("How many kilometers do you want convert to miles? ")))
print(f"That is {distance} miles.")
