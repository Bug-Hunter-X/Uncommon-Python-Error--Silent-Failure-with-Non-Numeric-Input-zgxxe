def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty or non-numeric list
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30, 40, 'abc']
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 30, 40, '50']
average = calculate_average(my_numbers)
print(f"The average is: {average}") #this will work now