def sum_of_squares(numbers):
    try:
        total = 0
        for n in numbers:
            total += int(n) ** 2
        return total
    except ValueError:
        return "Error: List must contain only numbers."

user_input = input("Enter numbers")
nums = user_input.split()

print("Sum of squares:", sum_of_squares(nums))
