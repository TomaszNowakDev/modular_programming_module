# Indicating longer string
def longer_string(a, b):
    longer = ""
    if len(a) > len(b):
        longer = a
    elif len(a) < len(b):
        longer = b
    return longer


length = longer_string(input("Enter first word > "), input("Enter second word > "))
print(length)
