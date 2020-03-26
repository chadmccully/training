# for i in range(1,11):
#     print(i)
#
#
# for ch in "Hello World":
#     print(ch)
#
#
# for word in "Hello World".split():
#     print(word)
#
#
# for item in (3, 6, 9):
#     print(item)

# is_prime(9); //Is a number Prime?
# //H: 5 => True, 7 => Ture, 11 => True, 6 => False

# def is_prime(number):
#     for divisor in range(2, number):
#         if number%divisor == 0:
#             print(f"The number {number} is not a prime number.  Dividing by {divisor} is also possible")
#             return
#     print(f"The number {number} is a prime number.")
#
#
# for num_to_check in (4,7,11,6):
#     is_prime(num_to_check)


#sum_upto_n(6); //sum of numbers upto n?
#//1+2+3+4+5+6
# def sum_of_numbers(number):
#     resulting_total = 0
#     for num_to_add in range(0,number+1):
#         resulting_total = resulting_total + num_to_add
#         print(f"Adding {num_to_add} added to the above now equals {resulting_total}")
#
#
# sum_of_numbers(15)


# def sum_of_divisors(number):
#     divisor_array = []
#     for divisor in range(1, number+1):
#         if number%divisor == 0:
#             divisor_array.append(divisor)
#     print(f"The sum of the divisors of {number} ({divisor_array}) total {sum(divisor_array)}")
#
#
# sum_of_divisors(15)


#print_a_number_triangle(5)
#//1
#//1 2
#//1 2 3
#//1 2 3 4
#//1 2 3 4 5
# def number_triangle(number):
#     row_contents = []
#     for row_to_print in range(1,number+1):
#         for j in range(1, row_to_print+1):
#             print(j, end=' ')
#         print('')
#
#
# number_triangle(10)


#i = 0
#while i < 5:
#    print(i, end=" ")
#    i = i + 1

#print squares up to limit(30)
# for limit = 30, output would be 1 4 9 16
# def print_squares_up_to_limit(max_number):
#     i = 1
#     while i*i <= max_number:
#         print(i*i, end=" ")
#         i = i + 1
#     print()
#
# print_squares_up_to_limit(75)

#print cubes up to limit(30)
# for limit = 30, output would be 1 8 27
# def print_cubes_up_to_limit(max_number):
#     i = 1
#     while i*i*i <= max_number:
#         print(i*i*i, end=" ")
#         i = i + 1
#
#
# print_cubes_up_to_limit(30)



#
# print("Chad's Math Machine")
# value_1 = int(input("Enter value 1: "))
# value_2 = int(input("Enter value 2: "))
# print("Please select a type of operation:")
# print("\n\n1 - Add")
# print("2 - Subtract")
# print("3 - Divide")
# print("4 - Multiply")
# print("5 - Exit")
#
# choice = int(input("Choose Operation: "))
#
# while(choice != 5):
#     if choice == 1:
#         result_value = value_1 + value_2
#     elif choice == 2:
#         result_value = value_1 - value_2
#     elif choice == 3:
#         result_value = value_1 / value_2
#     elif choice == 4:
#         result_value = value_1 * value_2
#     print(f"Your answer is: {result_value}")
#     choice = int(input("Choose Operation: "))

