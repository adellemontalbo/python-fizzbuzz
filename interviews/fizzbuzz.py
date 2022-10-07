# fizzbuzz is a function which returns the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzbuzz(n):
    list_to_return = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list_to_return.append("FizzBuzz")
        elif i % 3 == 0:
            list_to_return.append("Fizz")
        elif i % 5 == 0:
            list_to_return.append("Buzz")
        else:
            list_to_return.append(str(i))
    return list_to_return


# def fizzbuzz(number):
#     current_number = 1
#     answer = []

#     for current_number in range(1, number + 1):
#         if current_number % 3 == 0:
#             answer.append("Fizz")
#         elif current_number % 5 == 0:
#             answer.append("Buzz")
#         elif current_number % 3 == 0 and current_number % 5 == 0:
#             answer.append("FizzBuzz")
#         else:
#             answer.append(f"{current_number}")
    
#     return answer
