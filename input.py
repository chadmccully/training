
def do_math(operation, val_1, val_2):
    if operation == 1:
        result_value = val_1 + val_2
    elif operation == 2:
        result_value = val_1 - val_2
    elif operation == 3:
        result_value = val_1 / val_2
    elif operation == 4:
        result_value = val_1 * val_2
    else:
        result_value = "Invalid Choice"
    return result_value

print("Chad's Math Machine")
value_1 = int(input("Enter value 1: "))
value_2 = int(input("Enter value 2: "))
print("Please select a type of operation:")
print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
selection = int(input("Choose Operation:"))

print("Your answer is: ", do_math(selection, value_1, value_2))



